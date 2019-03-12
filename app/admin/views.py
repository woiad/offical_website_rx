#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, url_for, request, send_from_directory, flash, redirect, session
from werkzeug.urls import url_parse
from app import app, db
from .form import articleForm, discountForm, serverForm, trentForm, userForm, pwdForm
import os, uuid, datetime
from flask_ckeditor import upload_fail, upload_success
from app.models import Article, Uploadimg, Discount, Server, Product, User
import re
from functools import wraps

def change_name(name):
    lastName = os.path.splitext(name)
    newName = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + lastName[-1]
    return newName


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    try:
        os.rmdir(re_path())
    except OSError:
        pass


def extract_src(str):
    imgList = re.findall(r'<img.*? />', str, re.S)
    srcList = []
    for tag in imgList:
        src = re.search(r'.+?src="(\S+)"', tag)
        srcList.append(src.group(1))
    return srcList


def compare_src(old_srclist, new_srclist):
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(app.config['IMG_DIR'], dir)
    for src in old_srclist:
        if src not in new_srclist:
            split_text = src.split('/')
            delete_file(os.path.join(path, split_text[-1]))


def two_one_dim(list):
    src_list = []
    for src in list:
        src_list.append(src[0])
    return src_list


def re_path():
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(app.config['IMG_DIR'], dir)
    return path


# 登陆装饰器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kw):
        if 'account' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kw)
    return decorated_function


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = userForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name = form.data['user_name']).first()
        if not user:
            flash('用户名不存在！')
            return redirect(url_for('login'))
        if user.check_password(form.data['password']):
            user.ip = request.remote_addr
            session['account'] = user.user_name
            session['ip'] = request.remote_addr
            session['login_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.session.add(user)
            db.session.commit()
            next_pages = request.args.get('next')
            if not next_pages or url_parse(next_pages).netloc != url_parse(request.url).netloc:
                next_pages = url_for('admin_ind')
            print(next_pages)
            return redirect(next_pages)
        else:
            flash('密码错误!')
            return redirect(url_for('login'))
    return render_template('admin/login.html', form=form)


@app.route('/admin/pwd', methods=['POST', 'GET'])
@admin_login_req
def pwd():
    form = pwdForm()
    if form.validate_on_submit():
        print(11)
        user = User.query.filter_by(user_name = session['account']).first()
        if not user.check_password(form.data['old_pwd']):
            flash('旧密码错误!', 'error')
            return redirect(url_for('pwd'))
        if form.data['old_pwd'] == form.data['confirm_pwd']:
            flash('新旧密码不能一致!', 'error')
            return redirect(url_for('pwd'))
        user.set_password(form.data['confirm_pwd'])
        db.session.add(user)
        db.session.commit()
        flash('修改成功', 'ok')
    return render_template('admin/pwd.html', form=form)


@app.route('/admin/logout')
@admin_login_req
def logout():
    session.pop("account", None)
    session.pop("ip", None)
    session.pop("login_time", None)
    return redirect(url_for('login'))

@app.route('/admin/index')
@admin_login_req
def admin_ind():
    return render_template('admin/index.html')

@app.route('/admin/article_add', methods=['GET', 'POST'])
@admin_login_req
def article_add():
    form = articleForm()
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        img_src_list = Uploadimg.query.with_entities(Uploadimg.src).filter_by(dir=dir).all()
        compare_src(two_one_dim(img_src_list), extract_src(form.data['article_content']))
        if not os.path.exists(re_path()):
            os.mkdir(re_path())
        f = form.data['img']
        filename = change_name(form.data['img'].filename)
        f.save(os.path.join(re_path(), filename))
        article = Article(title=form.data['title'], info=form.data['info'],\
                  cover_img=os.path.join(dir, filename), release_time=form.data['release_time'], \
                  click_count=form.data['click_count'], article_content=form.data['article_content'],\
                  article_type=form.data['article_type'])
        db.session.add(article)
        db.session.commit()

        flash('添加成功', 'ok')
        uploadimg = Uploadimg.query.filter_by(dir=dir).all()
        [db.session.delete(src) for src in uploadimg]
        db.session.commit()
        return redirect(url_for('article_add'))
    return render_template('admin/article_add.html', form=form)


@app.route('/admin/article_list', methods=['GET', 'POST'])
@admin_login_req
def article_list():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('admin/article_list.html', articles=articles)

@app.route('/admin/article_edit/<int:id>', methods=['POST', 'GET'])
@admin_login_req
def article_edit(id):
    id = id
    article = Article.query.filter_by(id=id).first()
    form = articleForm(article_type=article.article_type)
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        article_count = Article.query.filter_by(title=form.data['title']).count()
        if article_count == 1 and article.title != form.data['title']:
            flash('文章标题重复', 'error')
            return redirect(url_for('article_edit', id=article.id))
        if form.data['img']:
            f = form.data['img']
            filename = change_name(form.data['img'].filename)
            print(filename)
            delete_file(os.path.join(app.config['IMG_DIR'], article.cover_img))
            f.save(os.path.join(re_path(), filename))
            article.cover_img = os.path.join(dir, filename)
        compare_src(extract_src(article.article_content), extract_src(form.data['article_content']))
        article.title = form.data['title']
        article.info = form.data['info']
        article.release_time = form.data['release_time']
        article.click_count = form.data['click_count']
        article.article_content = form.data['article_content']
        article.article_type = form.data['article_type']
        flash('修改成功', 'ok')
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article_edit', id=article.id))
    return render_template('admin/article_edit.html', form=form, article=article)


@app.route('/admin/article_del/<int:id>')
@admin_login_req
def article_del(id):
    id = id
    path = os.path.join(app.config['IMG_DIR'], datetime.datetime.now().strftime('%Y-%m-%d'))
    article = Article.query.filter_by(id=id).first()
    delete_file(os.path.join(app.config['IMG_DIR'], article.cover_img))
    imgList = extract_src(article.article_content)
    for src in imgList:
        delete_file(os.path.join(path, src.split('/')[-1]))
    db.session.delete(article)
    db.session.commit()
    flash('删除成功', 'ok')
    return  redirect(url_for('article_list'))



@app.route('/admin/disocunt_add', methods=['GET', 'POST'])
@admin_login_req
def discount_add():
    form = discountForm()
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        img_src_list = Uploadimg.query.with_entities(Uploadimg.src).filter_by(dir=dir).all()
        compare_src(two_one_dim(img_src_list), extract_src(form.data['article_content']))
        f = form.data['img']
        filename = change_name(f.filename)
        if not os.path.exists(re_path()):
            os.mkdir(re_path())
        f.save(os.path.join(re_path(), filename))
        discount = Discount(title=form.data['title'], info=form.data['info'],
                            cover_img=os.path.join(dir, filename), start_time=form.data['start_time'],
                            end_time = form.data['end_time'], active=form.data['active'],
                            discount_content=form.data['article_content'])
        db.session.add(discount)
        db.session.commit()
        flash('添加成功', 'ok')
        uploadimg = Uploadimg.query.filter_by(dir=dir).all()
        [db.session.delete(src) for src in uploadimg]
        db.session.commit()
        return redirect(url_for('discount_add'))
    return render_template('admin/discount_add.html', form = form)


@app.route('/admin/discount_list', methods=['GET', 'POST'])
@admin_login_req
def discount_list():
    page = request.args.get('page', 1, type=int)
    discounts = Discount.query.paginate(page, app.config['SHOW_DATA'], False)
    return render_template('admin/discount_list.html', discounts=discounts)


@app.route('/admin/discount_edit/<int:id>', methods=['POST', 'GET'])
@admin_login_req
def discount_edit(id):
    id = id
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    discount = Discount.query.filter_by(id=id).first()
    form = discountForm(active=discount.active)
    if form.validate_on_submit():
        discount_count = Discount.query.filter_by(title=form.data['title']).count()
        if discount_count == 1 and discount.title != form.data['title']:
            flash('优惠标题重复', 'error')
            return redirect(url_for('discount_edit', id=discount.id))
        if form.data['img']:
            f = form.data['img']
            filename = change_name(form.data['img'].filename)
            delete_file(os.path.join(app.config['IMG_DIR'], discount.cover_img))
            f.save(os.path.join(re_path(), filename))
            discount.cover_img = os.path.join(dir, filename)
        compare_src(extract_src(discount.discount_content), extract_src(form.data['article_content']))
        discount.title = form.data['title']
        discount.info = form.data['info']
        discount.start_time = form.data['start_time']
        discount.end_time = form.data['end_time']
        discount.discount_content = form.data['article_content']
        discount.active = form.data['active']
        flash('修改成功', 'ok')
        db.session.add(discount)
        db.session.commit()
        return redirect(url_for('discount_edit', id=discount.id))
    return render_template('admin/discount_edit.html', form=form, discount=discount)


@app.route('/admin/discount_del/<int:id>')
@admin_login_req
def discount_del(id):
    id = id
    discount = Discount.query.filter_by(id=id).first()
    delete_file(os.path.join(app.config['IMG_DIR'], discount.cover_img))
    imgList = extract_src(discount.discount_content)
    for src in imgList:
        path = src.split('/')[-1]
        delete_file(os.path.join(re_path(), path))
    db.session.delete(discount)
    db.session.commit()
    flash('删除成功', 'ok')
    return  redirect(url_for('discount_list'))


@app.route('/files/<filename>')
def uploaded_files(filename):
    dir = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return send_from_directory(url_for('static', filename='uploads/' + dir + '/' + filename), filename, as_attachment=True)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    print(request.files.get('upload'))
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='图片格式有误!')
    filename = change_name(f.filename)
    dir = datetime.datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(app.config['IMG_DIR'], dir)
    if not os.path.exists(path):
        os.mkdir(path)
    f.save(os.path.join(path, filename))
    if os.path.exists(os.path.join(path, filename)):
        uploadimg = Uploadimg(dir=dir, src='/static/uploads/' + dir + '/' +filename)
        db.session.add(uploadimg)
        db.session.commit()
    url_for('uploaded_files', filename=filename)
    return upload_success(url=url_for('static', filename='uploads/' + dir + '/' + filename))



@app.route('/admin/server_add', methods=['GET', 'POST'])
@admin_login_req
def server_add():
    form = serverForm()
    if form.validate_on_submit():
        server_count = Server.query.filter_by(title=form.data['title']).first()
        if server_count:
            flash('添加失败，该名称已存在！', 'error')
            return redirect(url_for('server_add'))
        server = Server(title=form.data['title'], cpu=form.data['cpu'], memory=form.data['memory'], \
                        disk=form.data['disk'], bdwidth=form.data['bdwidth'], \
                        price=form.data['price'], server_type=form.data['server_type'], \
                        server_region=form.data['server_region'])
        db.session.add(server)
        db.session.commit()
        flash('添加成功', 'ok')
        return redirect(url_for('server_add'))
    return render_template('/admin/server_add.html', form=form)


@app.route('/admin/server_list', methods=['GET', 'POST'])
@admin_login_req
def server_list():
    server_list = ['服务器租用', '高防服务器', '热门机型']
    page = request.args.get('page', 1, type=int)
    servers = Server.query.order_by(Server.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('admin/server_list.html', servers=servers, server_list=server_list)


@app.route('/admin/server_edit', methods=['GET', 'POST'])
@admin_login_req
def server_edit():
    id = request.args.get('id')
    server = Server.query.filter_by(id=id).first()
    form = serverForm(server_type=server.server_type)
    if form.validate_on_submit():
        server_count = Server.query.filter_by(title=form.data['title']).count()
        if server_count == 1 and server.title != form.data['title']:
            flash('修改失败，该名称已存在！', 'error')
            return redirect(url_for('server_edit'))
        server.title = form.data['title']
        server.cpu = form.data['cpu']
        server.memory = form.data['memory']
        server.disk = form.data['disk']
        server.bdwidth = form.data['bdwidth']
        server.price = form.data['price']
        server.server_type = form.data['server_type']
        server.server_region = form.data['server_region']
        db.session.add(server)
        db.session.commit()
        flash('修改成功', 'ok')
        return redirect(url_for('server_edit', id=server.id))
    return render_template('admin/server_edit.html', form=form, server=server)


@app.route('/admin/server_delete')
@admin_login_req
def server_delete():
    id  =request.args.get('id')
    server = Server.query.filter_by(id=id).first()
    db.session.delete(server)
    db.session.commit()
    flash('删除成功', 'ok')
    return redirect(url_for('server_list'))


@app.route('/admin/product_add', methods=['GET', 'POST'])
@admin_login_req
def product_add():
    form = trentForm()
    if form.validate_on_submit():
        pro_count = Product.query.filter_by(title=form.data['title']).count()
        if pro_count == 1:
            flash('添加失败，该名称已存在!', 'error')
            return redirect(url_for('product_add'))
        product = Product(title=form.data['title'], ip_num=form.data['ip_num'],\
                          defends=form.data['defends'], bdwidth=form.data['bdwidth'],\
                          price=form.data['price'], circuit_type=form.data['circuit_type'], \
                          pro_type=form.data['pro_type'], standard=form.data['standard'])
        db.session.add(product)
        db.session.commit()
        flash('添加成功', 'ok')
        return redirect(url_for('product_add'))
    return render_template('admin/rent.html', form=form)



@app.route('/admin/product_list', methods=['GET', 'POST'])
@admin_login_req
def product_list():
    cir_list = ['电信', '国际路线', '双线', '三线', 'BGP']
    type_list = ['服务器托管', '机柜租用']
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('admin/rent_list.html', products=products, cir_list=cir_list, type_list=type_list)



@app.route('/admin/product_edit', methods=['GET', 'POST'])
@admin_login_req
def product_edit():
    id = request.args.get('id')
    product = Product.query.filter_by(id=id).first()
    form = trentForm(circuit_type=product.circuit_type, pro_type=product.pro_type)
    if form.validate_on_submit():
        pro_count = Product.query.filter_by(title=form.data['title']).count()
        if pro_count == 1 and product.title != form.data['title']:
            flash('修改失败,名字已存在','error')
            return redirect(url_for('product_edit', id=product.id))
        product.title = form.data['title']
        product.ip_num = form.data['ip_num']
        product.defends = form.data['defends']
        product.bdwidth = form.data['bdwidth']
        product.price = form.data['price']
        product.circuit_type = form.data['circuit_type']
        product.pro_type = form.data['pro_type']
        product.standard = form.data['standard']
        db.session.add(product)
        db.session.commit()
        flash('修改成功', 'ok')
        return redirect(url_for('product_edit', id=product.id))
    return render_template('admin/rent_edit.html', product=product, form=form)



@app.route('/admin/product_del', methods=['GET', 'POST'])
@admin_login_req
def product_del():
    id = request.args.get('id')
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    flash('删除成功', 'ok')
    return redirect(url_for('product_list'))
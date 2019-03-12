#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, request, url_for
from . import home
from app import app, db
from app.models import Server, Article, Discount, Product
import re, math
from sqlalchemy import and_, or_

@app.template_filter('extract_num')
def extract_num(str):
    price = re.sub(r'\D+', '', str)
    return price


@app.template_filter('extract_unit')
def extract_unit(str):
    unit = re.sub(r'\d+', '', str)
    return unit


def two_one_dim(list):
    src_list = []
    for src in list:
        src_list.append(src[0])
    return src_list

@app.route('/')
@app.route('/index')
def index():
    hot_server_list = Server.query.filter_by(server_type=2).order_by(Server.id.desc()).limit(6).all()
    adv_list = Article.query.filter_by(article_type=4).order_by(Article.id.desc()).limit(5).all()
    new_list = Article.query.filter_by(article_type=3).order_by(Article.id.desc()).limit(5).all()
    return render_template('home/index.html', title='首页', hot_server_list=hot_server_list, adv_list=adv_list, new_list=new_list)


@app.route('/server-list', methods=['GET'])
def server_List():
    title = request.args.get('title_name')
    path = request.args.get('path_name')
    page = request.args.get('page', 1, type=int)
    server_type = ['普通服务器', '高防服务器']
    servers = Server.query.filter_by(server_type=server_type.index(title)).order_by(Server.id.desc()).paginate(page, 9, False)
    return render_template('home/product/server-list.html', title=title, path=path, servers=servers)


@app.route('/trustee-list', methods=['GET'])
def product_List():
    title = request.args.get('title_name')
    path = request.args.get('path_name')
    page = request.args.get('page', 1, type=int)
    circuit = request.args.get('circuit')
    pro_type = ['服务器托管', '机柜租用']
    circuit_type = ['电信', '国际路线', '双线', '三线', 'BGP']
    products = Product.query.filter(and_(Product.pro_type==pro_type.index(path), Product.circuit_type==circuit_type.index(circuit))).order_by(Product.id.desc()).paginate(page, 9, False)
    return render_template('home/product/rent_trustee.html', title=title, path=path, products=products, circuit=circuit)


@app.route('/service-add', methods=['GET'])
def service_add():
    return render_template('home/service-add/views/service-add.html', title='增值服务')

@app.route('/vistor', methods=['GET'])
def vistor_room():
    return render_template('home/vistor-room/room-list/vist.html', title='参观锐讯机房')

@app.route('/vistor-detail', methods=['GET'])
def vistor_detail():
    room_name = request.args.get('roomName')
    if room_name == 'fs':
        return render_template('home/vistor-room/room-detail/room-fs.html', title='佛山顺德电信机房')
    elif room_name == 'lm':
        return render_template('home/vistor-room/room-detail/room-lm.html', title='美国机房')


@app.route('/discount_sales', methods=['GET'])
def discount():
    page = request.args.get('page', 1, type=int)
    discounts = Discount.query.order_by(Discount.id.desc()).paginate(page, 8, False)
    return render_template('home/discount-sales/sales-list/sales.html', title='优惠促销', discounts = discounts)


@app.route('/discount_detail', methods=['GET'])
def discount_detail():
    id = request.args.get('id', type=int)
    discount = Discount.query.filter_by(id=id).first()
    return render_template('home/discount-sales/discount_detail.html', title='优惠促销详情', discount = discount)


@app.route('/help', methods=['GET'])
def help():
    page = request.args.get('page', 1, type=int)
    faq_list = Article.query.filter_by(article_type=2).order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('home/help-content/views/help.html', title='帮助中心', faq_list=faq_list)



@app.route('/beian')
def beian():
    name = request.args.get('name')
    if name == 'care':
        return render_template('home/help-content/beian/ba-flow.html', title='网站备案注意事项')
    elif name == 'flow':
        return render_template('home/help-content/beian/ba-flow-1.html', title='备案流程')
    else:
        return render_template('home/help-content/beian/ba-need-know.html', title='网站备案须知')

nav_data = [
    {'name': '公司介绍', 'href':'contact_us', 'active': 'int'},
    {'name': '资质证书', 'href':'qua_book', 'active': 'book'},
    {'name': '员工风采', 'href':'staff', 'active': 'staff'},
    {'name': '新闻资讯', 'href':'new_information', 'active': 'news'},
    {'name': '商务合作', 'href':'busine_cooperation', 'active': 'coop'},
    {'name': '支付方式', 'href':'pay_way', 'active': 'pay'},
    {'name': '联系我们', 'href':'connect_us', 'active': 'connect'}
]

@app.route('/contact-us')
def contact_us():
    return render_template('home/contact-us/views/intro-company.html', title='公司介绍', nav_data=nav_data)


@app.route('/qua-book')
def qua_book():
    return render_template('home/contact-us/views/certi-book.html', title='资质证书', nav_data=nav_data)

@app.route('/staff')
def staff():
    page = request.args.get('page', 1, type=int)
    staff_list = Article.query.filter_by(article_type=0).order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('home/contact-us/views/staff.html', title='员工风采', nav_data=nav_data, staff_list=staff_list)


@app.route('/news_information')
def new_information():
    page = request.args.get('page', 1, type=int)
    news = Article.query.filter_by(article_type=1).order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('home/contact-us/views/news-information.html', title='新闻资讯', nav_data=nav_data, news=news)


@app.route('/news_information_adv')
def new_information_adv():
    page = request.args.get('page', 1, type=int)
    advs = Article.query.filter_by(article_type=4).order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('home/contact-us/views/news-information-adv.html', title='最新公告', nav_data=nav_data, advs=advs)


@app.route('/news_information_list')
def new_information_list():
    page = request.args.get('page', 1, type=int)
    lists = Article.query.filter_by(article_type=3).order_by(Article.id.desc()).paginate(page, app.config['SHOW_DATA'], False)
    return render_template('home/contact-us/views/news-information-list.html', title='新闻资讯', nav_data=nav_data, lists=lists)


@app.route('/busine_cooperation')
def busine_cooperation():
    return render_template('home/contact-us/views/busine-cooperation.html', title='商务合作', nav_data=nav_data)


@app.route('/pay-way')
def pay_way():
    return render_template('home/contact-us/views/pay.html', title='支付方式', nav_data=nav_data)


@app.route('/connect-us')
def connect_us():
    return render_template('home/contact-us/views/connect-us.html', title='联系我们', nav_data=nav_data)


@app.route('/article_detail')
def article_detail():
    id = request.args.get('id')
    article = Article.query.filter_by(id=id).first()
    article_list = Article.query.filter_by(article_type=article.article_type).order_by(Article.id.desc()).all()
    title_list = []
    for item in article_list:
        title_list.append(item.title)
    ind = title_list.index(article.title)
    next_ind = None
    pre_ind = None
    if ind - 1 >= 0:
        next_ind = ind - 1
    if ind + 1 < len(title_list):
        pre_ind = ind + 1
    if  pre_ind:
        pre_article = Article.query.filter_by(title=title_list[pre_ind]).first()
    else:
        pre_article = None
    if  next_ind or next_ind == 0:
        next_article = Article.query.filter_by(title=title_list[next_ind]).first()
    else:
        next_article = None
    return render_template('/home/contact-us/article_detail.html', article=article,
                           title=article.title, pre_article=pre_article, next_article=next_article)


@app.route('/search_result', methods=['GET', 'POST'])
def search_result():
    str = request.form.get('search_str') or request.args.get('str')
    page = request.args.get('page', 1, type=int)
    article_list = []
    show_artilce = []
    products = []
    articles = Article.query.filter(or_(Article.title.ilike('%' +str + '%'), Article.article_content.ilike('%' +str + '%'))).all()
    server_list = Server.query.filter(Server.title.ilike('%' + str + '%')).all()
    product_list = Product.query.filter(Product.title.ilike('%' + str + '%')).all()
    for product in product_list:
        products.append(product)
    for server in server_list:
        products.append(server)
    for article in articles:
        article_list.append(article)
    art_total = len(article_list)
    if article_list and len(article_list) > 9:
        if page - 1 > 0:
            star_index = (page - 1) * 10 - 1
        else:
            star_index = 0
        show_artilce = article_list[star_index: page * 10 - 1]
    elif article_list and len(article_list) <= 9:
        show_artilce = article_list
    art_total_page = math.ceil(art_total / app.config['SHOW_DATA'])
    pages = break_page(art_total_page, page)
    return render_template('/home/search.html', articles=show_artilce, art_total_page=art_total_page, pages=pages,
                           current_page = page, str=str, art_total=art_total, pro_total = len(products))

@app.route('/search_pro', methods=['GET', 'POST'])
def search_pro():
    page = request.args.get('page', 1, type=int)
    str = request.form.get('search_str') or request.args.get('str')
    products = []
    show_product  =[]
    art_total = []
    articles = Article.query.filter(or_(Article.title.ilike('%' +str + '%'), Article.article_content.ilike('%' +str + '%'))).all()
    server_list = Server.query.filter(Server.title.ilike('%' + str + '%')).all()
    product_list = Product.query.filter(Product.title.ilike('%' + str + '%')).all()
    for article in articles:
        art_total.append(article)
    for product in product_list:
        products.append(product)
    for server in server_list:
        products.append(server)
    if products and len(products) > 9:
        if page - 1 > 0:
            star_index = (page - 1) * 10 - 1
        else:
            star_index = 0
        show_product = products[ star_index   : page * 10 - 1]
    elif products and len(products) <= 9:
        show_product = products
    all_page = math.ceil(len(products) / 9)
    pages = break_page( all_page , page)
    return render_template('/home/search_pro.html', art_total=len(art_total), str=str, pro_total=len(products),
                           show_product = show_product, pages=pages, current_page = page, all_page=all_page)


def break_page(all_page, current_page):
    pages = []
    if current_page + 5  < all_page:
        for page in range(1, current_page + 5):
            pages.append(page)
        pages.append('...')
        pages.append(all_page)
    else:
        for page in range(1, all_page + 1):
            pages.append(page)
    length = len(pages) - 8
    if length > 1:
        for i in range(1, length):
            pages.pop(1)
        pages.insert(1, '...')
    return pages

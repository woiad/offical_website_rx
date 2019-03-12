#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField,\
            SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask_ckeditor import CKEditorField


class userForm(FlaskForm):
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')],
                            render_kw={'class':'form-control', 'placeholder': '请输入用户名'})
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '请输入密码'})
    submit = SubmitField(label='登陆', render_kw={'class': 'btn btn-primary btn-block btn-flat'})


class pwdForm(FlaskForm):
    old_pwd = PasswordField(label='旧密码', validators=[DataRequired('旧密码不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '请输入旧密码'})
    new_pwd = PasswordField(label='新密码', validators=[DataRequired('新密码不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '请输入新密码'})
    confirm_pwd = PasswordField(label='确认密码', validators=[DataRequired('请输入确认密码'), EqualTo('new_pwd', message='两次密码不一致')],
                            render_kw={'class': 'form-control', 'placeholder': '请输入新密码'})
    submit = SubmitField(label='提交', render_kw={'class': 'btn btn-primary'})

class articleForm(FlaskForm):
    title = StringField(label='文章标题', validators=[DataRequired('标题不能为空')],
                        render_kw={'class': 'form-control', 'placeholder': '请输入文章标题'})
    info = TextAreaField(label='文章简介', validators=[DataRequired('简介不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入文章简介'})
    img = FileField(label='文章封面', validators=[DataRequired('封面不能为空')],
                        render_kw={'id':'input_logo', 'placeholder': '请输入文章封面'})
    release_time = StringField(label='发布时间', validators=[DataRequired('时间不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入发布时间'})
    article_type = SelectField(label='文章类型', coerce=int, choices=[(0, '员工风采'), (1, '锐讯动态'),\
                                                          (2, '常见问题'), (3, '新闻资讯'), (4, '最新公告')],
                         render_kw={'class': 'form-control'})
    click_count = StringField(label='浏览次数', validators=[DataRequired('浏览次数不能为空')],
                              render_kw={'class': 'form-control', 'placeholder':'浏览次次数不能为空'})
    article_content = CKEditorField(label='文章内容', validators=[DataRequired('文章内容不能为空')],
                                    render_kw={'class': 'form-control', 'placeholder': '请输入文章内容'})
    submit = SubmitField(label='添加', render_kw={'class': 'btn btn-primary'})


class discountForm(FlaskForm):
    title = StringField(label='优惠标题', validators=[DataRequired('标题不能为空')],
                        render_kw={'class': 'form-control', 'placeholder': '请输入优惠标题'})
    info = TextAreaField(label='优惠简介', validators=[DataRequired('简介不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入文章简介'})
    img = FileField(label='优惠封面', validators=[DataRequired('封面不能为空')],
                        render_kw={'id':'input_logo', 'placeholder': '请输入优惠封面'})
    start_time = StringField(label='开始时间', validators=[DataRequired('开始时间不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入开始时间', 'id': 'input_stime'})
    end_time = StringField(label='结束时间', validators=[DataRequired('结束时间不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '请输入结束时间', 'id': 'input-etime'})
    article_content = CKEditorField(label='文章内容', validators=[DataRequired('文章内容不能为空')],
                                    render_kw={'class': 'form-control', 'placeholder': '请输入文章内容', 'id': 'input_content'})
    active = SelectField(label='活动是否结束',coerce=int, choices=[(1, '是'), (2, '否')],
                         render_kw={'class': 'form-control'})
    submit = SubmitField(label='添加', render_kw={'class': 'btn btn-primary'})


class serverForm(FlaskForm):
    title = StringField(label='服务器名字', validators=[DataRequired('名字不能为空')],
                        render_kw={'class': 'form-control', 'placeholder': '请输入服务器名字'})
    cpu = StringField(label='CPU', validators=[DataRequired('CPU不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入CPU'})
    memory = StringField(label='内存', validators=[DataRequired('内存不能为空')],
                        render_kw={'class':'form-control', 'placeholder': '请输入服务器内存'})
    disk = StringField(label='硬盘', validators=[DataRequired('硬盘不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入硬盘'})
    bdwidth = StringField(label='带宽', validators=[DataRequired('带宽不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '请输入带宽'})
    price = StringField(label='价格(多个价格之间用空格隔开)', validators=[DataRequired('价格不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '请输入价格'})
    server_type = SelectField(label='服务器类型', coerce=int, choices=[(0, '服务器租用'), (1, '高防服务器'),\
                              (2, '热门机型')], render_kw={'class': 'form-control'})
    server_region = StringField(label='服务器所在地', validators=[DataRequired('服务器所在地不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '服务器所在地'})
    submit = SubmitField(label='添加', render_kw={'class': 'btn btn-primary'})


class trentForm(FlaskForm):
    title = StringField(label='产品名字', validators=[DataRequired('名字不能为空')],
                        render_kw={'class': 'form-control', 'placeholder': '请输入产品名字'})
    ip_num = StringField(label='IP个数', validators=[DataRequired('IP个数不能为空')],
                        render_kw={'class':'form-control', 'placeholder': '请输入IP个数'})
    defends = StringField(label='防御', validators=[DataRequired('防御不能为空')],
                         render_kw={'class': 'form-control', 'placeholder': '请输入防御'})
    bdwidth = StringField(label='带宽', validators=[DataRequired('带宽不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '请输入带宽'})
    price = StringField(label='价格(多个价格之间用空格隔开)', validators=[DataRequired('价格不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '请输入价格'})
    circuit_type = SelectField(label='线路类型', coerce=int, choices=[(0, '电信'), (1, '国际路线'),\
                              (2, '双线'), (3, '三线'), (4, 'BGP')], render_kw={'class': 'form-control'})
    pro_type = SelectField(label='产品类型', coerce=int, choices=[(0, '服务器托管'), (1, '机柜租用')],
                               render_kw={'class': 'form-control'})
    standard = StringField(label='规格', validators=[DataRequired('规格不能为空')],
                       render_kw={'class': 'form-control', 'placeholder': '规格'})
    submit = SubmitField(label='添加', render_kw={'class': 'btn btn-primary'})

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    info = db.Column(db.String(256))
    release_time = db.Column(db.String(128), index=True)
    click_count = db.Column(db.String(64), index=True)
    article_content = db.Column(db.Text)
    article_type = db.Column(db.Integer, index=True)
    cover_img = db.Column(db.String(64), index=True)


class Discount(db.Model):
    __table__name = 'discount'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    info = db.Column(db.String(256))
    start_time = db.Column(db.String(128), index=True)
    end_time = db.Column(db.String(128), index=True)
    discount_content = db.Column(db.Text)
    cover_img = db.Column(db.String(64), index=True)
    active = db.Column(db.Integer, index=True)


class Server(db.Model):
    __searchable__ = ['title']
    __tablename__ = 'server'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    cpu = db.Column(db.String(32))
    memory = db.Column(db.String(32), index=True)
    disk = db.Column(db.String(32), index=True)
    bdwidth = db.Column(db.String(32), index=True)
    price = db.Column(db.String(64), index=True)
    server_type = db.Column(db.Integer, index=True)
    server_region = db.Column(db.String(64))



class Product(db.Model):
    __searchable__ = ['title']
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    bdwidth = db.Column(db.String(32))
    ip_num = db.Column(db.String(32), index=True)
    defends = db.Column(db.String(32), index=True)
    price = db.Column(db.String(64), index=True)
    circuit_type = db.Column(db.Integer, index=True)
    standard = db.Column(db.String(32), index=True)
    pro_type = db.Column(db.Integer, index=True)



class Uploadimg(db.Model):
    __tablename__ = 'uploadimg'

    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(600), index=True)
    dir = db.Column(db.String(32), index=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    ip = db.Column(db.String(64), index=True)

    def __repr__(self):
        return "<User %s>" %self.name

    def set_password(self, password):
        self.password = generate_password_hash(password)
        print(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
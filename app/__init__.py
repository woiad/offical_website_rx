#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging.handlers import RotatingFileHandler
import os, logging
from flask_whooshee import Whooshee
from flask_whooshalchemyplus import index_all


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
whooshee = Whooshee(app)
app.config.from_object(config)
with app.app_context():  # 手动索引
    index_all(app)


from .admin import admin as admin_blueprint
from .home import home as home_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)

from app import models


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/mistake.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('project startup')

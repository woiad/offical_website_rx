#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class config(object):
    SECRET_KEY = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woiad1219@localhost:3306/website_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CKEDITOR_SERVE_LOCAL = False
    CKEDITOR_PKG_TYPE = 'full'
    CKEDITOR_HEIGHT = 400
    CKEDITOR_FILE_UPLOADER = 'upload'
    IMG_SIZE = 1024 * 1024 * 2
    SHOW_DATA = 9
    MAX_SEARCH_RESULTS = 50
    IMG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/uploads')
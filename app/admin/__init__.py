#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.views
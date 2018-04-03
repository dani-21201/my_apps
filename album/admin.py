# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from album.models import Category, Photo

admin.site.register(Category)
admin.site.register(Photo)
# Register your models here.

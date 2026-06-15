from django.contrib import admin
from .models import Book

# تسجيل جدول الكتب في لوحة التحكم
admin.site.register(Book)
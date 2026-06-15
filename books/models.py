from django.db import models
from django.contrib.auth.models import User

# 1. جدول الكتب
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الكتاب")
    author = models.CharField(max_length=100, verbose_name="المؤلف")
    is_available = models.BooleanField(default=True, verbose_name="متاح للاستعارة")

    def __str__(self):
        return self.title

# 2. جدول الاستعارات
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="الكتاب")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستعير")
    loan_date = models.DateField(auto_now_add=True, verbose_name="تاريخ الاستعارة")
    return_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الإرجاع")
    is_returned = models.BooleanField(default=False, verbose_name="تم الإرجاع")

    def __str__(self):
        return f"{self.user.username} استعار {self.book.title}"
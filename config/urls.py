"""
URL configuration for config project.
... (باقي التعليق لا يهمكِ حذفه أو بقاؤه)
"""
from django.contrib import admin
from django.urls import path, include  # <-- [تعديل 1]: أضفنا include هنا

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')), # <-- [تعديل 2]: أضفنا هذا السطر هنا
]
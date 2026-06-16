from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # هذا الرابط يربط المشروع بملف الـ urls الخاص بتطبيق الـ books
    path('', include('books.urls')), 
]

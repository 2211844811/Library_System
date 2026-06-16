from django.urls import path  # <--- هذا السطر ضروري جداً
from . import views           # <--- وهذا السطر يربط الملف بـ views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('book/add/', views.add_book, name='add_book'),
    path('my-loans/', views.my_loans, name='my_loans'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
]
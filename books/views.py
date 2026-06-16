from django.shortcuts import render, redirect
from .models import Book  # 1. استيراد الموديل الحقيقي

def book_list(request):
    # استقبال قيمة البحث من الشريط
    query = request.GET.get('q') 
    
    # جلب كل الكتب كقاعدة أساسية
    books = Book.objects.all()
    
    # إذا كانت هناك قيمة في البحث، قم بتصفية النتائج
    if query:
        # البحث في العنوان (title) باستخدام __icontains لجعل البحث غير حساس لحالة الأحرف
        books = books.filter(title__icontains=query)
        
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, book_id):
    # 3. استبدال البحث في القائمة بـ get() من قاعدة البيانات
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def borrow_book(request, book_id):
    # 4. البحث عن الكتاب وتغيير حالته في قاعدة البيانات
    book = Book.objects.get(id=book_id)
    if book.is_available:
        book.is_available = False
        book.save()  # ضرورية جداً لحفظ التغيير
    return redirect('book_list')

def add_book(request):
    # (هنا سنضع كود الـ ModelForm لاحقاً)
    return render(request, 'books/book_form.html')

def my_loans(request):
    # 5. تصفية (Filter) الكتب غير المتاحة من قاعدة البيانات
    loaned_books = Book.objects.filter(is_available=False)
    return render(request, 'books/my_loans.html', {'books': loaned_books})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')

def search_books(request):
    query = request.GET.get('q') # يأخذ الكلمة من شريط البحث
    if query:
        books = Book.objects.filter(title__icontains=query) # يبحث في العناوين
    else:
        books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

def return_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.is_available = True
    book.save()
    return redirect('my_loans')
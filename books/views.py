from django.shortcuts import render, redirect

BOOKS_DATA = [
    {'id': 1, 'title': 'مقدمة في البرمجة', 'author': 'أحمد علي', 'is_available': True},
    {'id': 2, 'title': 'تعلم Django للمبتدئين', 'author': 'سارة محمد', 'is_available': False},
]

def book_list(request):
    return render(request, 'books/list.html', {'books': BOOKS_DATA})

def book_detail(request, book_id):
    book = next((b for b in BOOKS_DATA if b['id'] == book_id), None)
    return render(request, 'books/book_detail.html', {'book': book})

def borrow_book(request, book_id):
    book = next((b for b in BOOKS_DATA if b['id'] == book_id), None)
    if book: book['is_available'] = False
    return redirect('book_list')

def add_book(request):
    return render(request, 'books/book_form.html')

def my_loans(request):
    loaned_books = [b for b in BOOKS_DATA if not b['is_available']]
    return render(request, 'books/my_loans.html', {'books': loaned_books})
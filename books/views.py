from django.shortcuts import render

def book_list(request):
    # دالة بسيطة تقوم باستدعاء صفحة عرض الكتب التي صممتِها
    return render(request, 'books/list.html')
from django.shortcuts import render, redirect
# from django.db.models import Count
from .models import *

def index(request):
    if 'logged_in' not in request.session:
        return redirect('/')
    this_book = Book.objects.last()
    context = {
        'recent_book': this_book,
        'reviews': [],
        'books_reviewed': [],
        'this_user': User.objects.get(id=request.session['user_id']),
    }
    if this_book:
        reviews = this_book.book_reviews.all()
        if reviews:
            context['reviews'] = reviews
    try:
        books = Book.objects.exclude(id=this_book.id)
        print(books)
        for book in books:
            if book.book_reviews.all():
                context['books_reviewed'].append(book)
    except:
        pass
    return render(request, 'books.html', context)

def add(request):
    if request.method == 'GET':
        context = {
            'all_authors': Author.objects.all(),
        }
        return render(request, 'add.html', context)
    
    # request.method == 'POST'
    this_user = User.objects.get(id=request.session['user_id'])
    if request.POST['auth_name']:
        this_author = Author.objects.create(name=request.POST['auth_name'])
    this_book = Book.objects.create(title=request.POST['title'], author=this_author)
    this_review = Review.objects.create(review_text=request.POST['review'], rating=request.POST['rating'], user=this_user, book=this_book)
    return redirect(f'/books/{this_book.id}')

def display_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    reviews = this_book.book_reviews.all()
    author = this_book.author
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'this_book': this_book,
        'reviews': reviews,
        'this_user': User.objects.get(id=request.session['user_id']),
        'author': author,
    }
    return render(request, 'disp_book.html', context)

def add_review(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_review = Review.objects.create(review_text=request.POST['review'], rating=request.POST['rating'], user=this_user, book=this_book)
    return redirect(f'/books/{this_book.id}')

def display_user(request, user_id):
    this_user = User.objects.get(id=user_id)
    # sums=Order.objects.aggregate(Sum('quantity_ordered'), Sum('total_price'))
    review_count = this_user.user_reviews.count()
    reviews = this_user.user_reviews.all()
    context = {
        'this_user': this_user,
        'review_count': review_count,
        'books': [],
    }
    for review in reviews:
        if review.book.book_reviews.all:
            context['books'].append(review.book)
    return render(request, 'disp_user.html', context)

def delete_review(request, review_id):
    this_review = Review.objects.get(id=review_id)
    this_book_id = this_review.book.id
    this_review.delete()
    return redirect(f'/books/{this_book_id}')
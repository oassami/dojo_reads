from django.db import models
from login_app.models import User

# class BookManager(models.Manager):
    # def addValidation(self, post_data):
    #     errors={}
    #     if not post_data['title']:
    #         errors['title'] = 'Title is required.'
    #     if len(post_data['description']) < 5:
    #         errors['description'] = 'Description must be at least 5 characters'
    #     try:
    #         self.get(title=post_data['title'])
    #         errors['title'] = "This title already exists!"
    #     except:
    #         pass
    #     return errors

    # def updateValidation(self, post_data):
    #     errors={}
    #     if not post_data['title']:
    #         errors['title'] = 'Title is required.'
    #     if len(post_data['description']) < 5:
    #         errors['description'] = 'Description must be at least 5 characters'
    #     return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = BookManager()

class Review(models.Model):
    review_text = models.TextField(max_length=1000)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = BookManager()


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('<int:book_id>', views.display_book),
    path('review/add/<int:book_id>', views.add_review),
    path('user/<int:user_id>', views.display_user),
    path('review/delete/<int:review_id>', views.delete_review)
]

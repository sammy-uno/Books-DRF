from django.contrib import admin
from book_app.models import Book, Review

admin.site.register(Book)
# admin.site.register(StreamPlatform)
admin.site.register(Review)
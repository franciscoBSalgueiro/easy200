from django.contrib import admin

# Register your models here.

# from .models import Question

# Register your models here.

# admin.site.register(Question)

from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)


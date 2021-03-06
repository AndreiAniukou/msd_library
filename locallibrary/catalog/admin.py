from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'due_back', 'id']
    list_filter = ['status', 'due_back']

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


#admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
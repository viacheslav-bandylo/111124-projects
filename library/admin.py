from django.contrib import admin
from library.models import (
    Author,
    Book,
    Category,
    Library,
    Member,
    Post,
    Borrow,
    Review,
    AuthorDetail,
    Event,
    EventParticipant,
)


# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Library)
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Borrow)
admin.site.register(Review)
admin.site.register(AuthorDetail)
admin.site.register(Event)
admin.site.register(EventParticipant)


# # custom admin register for Book
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
    # # displayed fields
#     list_display = ('title', 'author', 'rating_display')


#     def rating_display(self, obj):
#         return obj.rating

#     rating_display.short_description = "Rating"

# @admin.register(Library)
# class LibraryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'location', 'website')

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
    # # displayed fields
#     list_display = ('title', 'description', 'timestamp', 'library')
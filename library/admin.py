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
    User,
    UserInfo,
    Actor,
    Director,
    Movie,
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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ['age']
    list_display = ('first_name', 'last_name', 'country', 'rating')
    search_fields = ['country', 'last_name']
    list_filter = ['rating']
    fields = ['rating', 'country']
    list_per_page = 2

    def set_rating_to_0(self, request, queryset):
        queryset.update(rating=0)

    set_rating_to_0.short_description = 'Set users rating to 0'
    actions = [set_rating_to_0]


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 2

class DirectorAdmin(admin.ModelAdmin):
    inlines = [MovieInline]


admin.site.register(UserInfo)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director, DirectorAdmin)


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
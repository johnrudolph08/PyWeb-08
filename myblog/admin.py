from django.contrib import admin
from myblog.models import Post, Category
from django.contrib import admin

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ('posts',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

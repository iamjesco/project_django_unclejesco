from django.contrib import admin
from .models import Post, Category

# Register your models here.

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'slug',
		'created',
		'author',
		'category',
		'status',
	)
	list_filter = ('status',)
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}
















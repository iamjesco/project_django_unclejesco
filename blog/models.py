from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name
	
	# def get_absolute_url(self):
	# 	return reverse('blog-feed')


category_choices = Category.objects.all().values_list('name', 'name')
category_list = [item for item in category_choices]


class Post(models.Model):
	STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
	
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	content = HTMLField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField()
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
	category = models.CharField(max_length=50, choices=category_list, default='Choose category')
	featured = models.BooleanField(default=False)
	
	class Meta:
		ordering = ('-created',)
	
	# def get_absolute_url(self):  # Needed to redirect after creating a new post
	# 	# return reverse('blog-post', kwargs={'slug': self.slug})
	# 	return reverse('blog-feed')
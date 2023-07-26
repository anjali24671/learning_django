from django.contrib import admin

# Register your models here.
# Django now knows that it should display our posts app and its database model Post on the admin page.
from .models import Post
admin.site.register(Post)
from django.contrib import admin
from . models import Stock

# Register your models here.
# in order for models to appear in the admin section you must register them

admin.site.register(Stock)


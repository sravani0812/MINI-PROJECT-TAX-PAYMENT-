from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Book)
admin.site.register(Payment)
admin.site.register(Donor)
admin.site.register(Product)
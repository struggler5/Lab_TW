from django.contrib import admin
from .models import * 

admin.site.register(User)
admin.site.register(Stock_item)
admin.site.register(Transaction)
# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Tablet)
admin.site.register(In)
admin.site.register(Order)
admin.site.register(Order_Item)
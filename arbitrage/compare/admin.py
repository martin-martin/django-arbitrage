from django.contrib import admin
from compare.models import Exchange, Asset, Market, Trade

# Register your models here.
admin.site.register(Exchange)
admin.site.register(Asset)
admin.site.register(Market)
admin.site.register(Trade)

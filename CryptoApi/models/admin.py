from django.contrib import admin
from .models import TradingStrategy, Pattern, FirebaseToken

admin.site.register(TradingStrategy)
admin.site.register(Pattern)
admin.site.register(FirebaseToken)

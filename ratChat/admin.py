from django.contrib import admin
from ratChat.models import RatRoom, RatMessages, RatSticker


# Register your models here.

admin.site.register(RatRoom)
admin.site.register(RatMessages)
admin.site.register(RatSticker)

from django.contrib import admin
from .models import Link,Direction

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class DirectionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Link,LinkAdmin)
admin.site.register(Direction,DirectionAdmin)

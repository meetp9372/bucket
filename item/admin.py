from django.contrib import admin
from item import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)


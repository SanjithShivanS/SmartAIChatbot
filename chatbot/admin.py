from django.contrib import admin
from .models import Category, FAQ, ChatLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    list_filter = ('category',)
    search_fields = ('question', 'answer')

@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ('user_query', 'timestamp')
    readonly_fields = ('user_query', 'bot_response', 'timestamp')

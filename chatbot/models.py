from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class FAQ(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='faqs')
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question[:50]}..."

class ChatLog(models.Model):
    user_query = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query: {self.user_query[:30]} at {self.timestamp}"

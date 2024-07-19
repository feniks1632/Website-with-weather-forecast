from django.db import models


class SearchHistory(models.Model):
    # Или используйте ForeignKey для связи с User
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)
    count_city = models.IntegerField(default=1)

from django.db import models


class SearchHistory(models.Model):
    # Или используйте ForeignKey для связи с User
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)
    count_city = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} искал погоду в {self.city} в {self.search_time} {self.count_city} раз"

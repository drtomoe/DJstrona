from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse     #potrzebne do przekierowywania na nową stronę po zapisaniu np. Posta, zwraca url jako str


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  #dodaje tylko czas pierwszej publikacji
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #jeśli skasujesz Usera to:

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

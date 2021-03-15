from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject=models.CharField(max_length=500)
    last_update=models.DateTimeField(auto_now_add=True)
    starter=models.ForeignKey(User,on_delete=models.CASCADE,related_name="topics")
    board=models.ForeignKey(Board,on_delete=models.CASCADE,related_name="topics")

    def __str__(self):
        return self.subject
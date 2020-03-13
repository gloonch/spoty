from django.db import models


# Create your models here.
class User(models.Model):
    # autoincrement and ok field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # nickname and email are required for first time creating
    nickname = models.TextField(default="guest", null=False)
    email = models.EmailField(default="000000000", unique=True, null=False)
    # token is made when ...
    # token is made when nick_name and phone_number
    token = models.TextField(unique=True, null=True, default="")
    created_at = models.TimeField(auto_created=True, auto_now=True)

    # TODO one to many rel with spots
    # TODO one to many rel with saved spots
    def __str__(self):
        return self.nickname


class Spot(models.Model):
    # autoincrement and ok field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # latitude text
    latitude = models.TextField(default="00000", null=False)
    # longitude text
    longitude = models.TextField(default="00000", null=False)
    # description about the spot
    description = models.TextField(default="00000", null=False)
    # like and dislike for feedbacks
    likes = models.IntegerField(default=0, null=False)
    dislikes = models.IntegerField(default=0, null=False)
    # TODO make a mechanism for sharing this spot


class SavedSpot(models.Model):
    # autoincrement and ok field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # latitude text
    latitude = models.TextField(default="00000", null=False)
    # longitude text
    longitude = models.TextField(default="00000", null=False)

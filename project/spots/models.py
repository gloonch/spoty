from django.db import models


# Create your models here.
# TODO


class SavedSpot(models.Model):
    spots = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spots', related_name='+')

    class Meta:
        managed = False
        db_table = 'saved_spot'


class Spot(models.Model):
    latitude = models.TextField()
    longitude = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', related_name='+')
    description = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    comments = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spot'

    def __str__(self):
        return "{} {},{}".format(self.user.name, self.latitude, self.longitude)


class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    token = models.TextField()
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now=True)
    spots = models.ForeignKey('spot', models.DO_NOTHING, null=True, db_column='spots', related_name='+')
    followings = models.ForeignKey('self', models.DO_NOTHING, null=True, db_column='followings', related_name='+')

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.name

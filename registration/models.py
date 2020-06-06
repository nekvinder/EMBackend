from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Login(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)


class Event(TimeStampMixin):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Group(models.Model):
    name = models.TextField(max_length=50, blank=True, unique=True)
    eventId = models.ForeignKey(
        Event, on_delete=models.PROTECT)
    registration_type = models.IntegerField()


class IdCard(models.Model):
    imagepath = models.FileField(upload_to='registration/')


class Registration(TimeStampMixin):
    fullname = models.TextField(max_length=50)
    mobile = models.TextField(max_length=10)
    email = models.EmailField(max_length=50)
    registration_type = models.IntegerField()
    idcard = models.ForeignKey(IdCard, on_delete=models.SET_NULL, null=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IdCard(models.Model):
    imagepath = models.FileField(upload_to='registration/')


class Group(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True)


class Registration(TimeStampMixin):
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    registration_type = models.IntegerField()
    idcard = models.ForeignKey(IdCard, on_delete=models.SET_NULL, null=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

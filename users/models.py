from django.db import models

class User(models.Model):
    account      = models.CharField(max_length=100)
    password     = models.CharField(max_length=100)
    name         = models.CharField(max_length=100)
    email        = models.CharField(max_length=100)
    points       = models.DecimalField(decimal_places=3, max_digits=10, default="100000")
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
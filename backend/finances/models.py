from django.db import models


class Budget(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        "auth.User", related_name="budgets", on_delete=models.CASCADE
    )

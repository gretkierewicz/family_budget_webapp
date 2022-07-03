from django.db import models


class Budget(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        "auth.User", related_name="budgets", on_delete=models.CASCADE
    )
    shared_with = models.ManyToManyField(
        "auth.User",
        blank=True,
        related_name="shared_budgets",
        through="BudgetSharedWith",
    )


class BudgetSharedWith(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

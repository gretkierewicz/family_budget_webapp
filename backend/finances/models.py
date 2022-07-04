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


class CashFlow(models.Model):
    CASH_FLOW_TYPES = [
        ("IN", "Income"),
        ("EX", "Expense"),
    ]

    budget = models.ForeignKey(
        Budget, related_name="cash_flows", on_delete=models.CASCADE
    )
    type = models.CharField(max_length=2, choices=CASH_FLOW_TYPES)
    name = models.CharField(max_length=128)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.type}: {self.amount}"

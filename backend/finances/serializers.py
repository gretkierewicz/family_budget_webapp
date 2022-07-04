from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from backend.finances.models import Budget, BudgetSharedWith, CashFlow


class CashFlowSerializer(NestedHyperlinkedModelSerializer):
    class Meta:
        model = CashFlow
        fields = "__all__"
        extra_kwargs = {"amount": {"min_value": 0}}

    parent_lookup_kwargs = {"budget_pk": "budget__pk"}


class ShareBudgetWithSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = BudgetSharedWith
        fields = ["username"]


class SharedBudgetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Budget
        fields = ["url", "owner", "name"]
        extra_kwargs = {"url": {"view_name": "shared_budgets-detail"}}


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    """
    source: https://gist.github.com/ph3b/98b9aeaff4f86527dc5a523f321cac7e
    """

    shared_with = ShareBudgetWithSerializer(source="budgetsharedwith_set", many=True)
    cash_flows = CashFlowSerializer(read_only=True, many=True)

    class Meta:
        model = Budget
        fields = ["url", "name", "shared_with", "cash_flows"]

    @staticmethod
    def process_shared_list(budget, users_list):
        for user in users_list:
            new_user = User.objects.get(username=user.get("username"))
            BudgetSharedWith(budget=budget, user=new_user).save()

    @transaction.atomic
    def create(self, validated_data):
        # not elegant, but validation adds that record and it breaks create method
        validated_data.pop("budgetsharedwith_set")
        instance = Budget.objects.create(**validated_data)
        self.process_shared_list(instance, self.initial_data.get("shared_with", []))

        instance.save()
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        BudgetSharedWith.objects.filter(budget=instance).delete()
        self.process_shared_list(instance, self.initial_data.get("shared_with", []))

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

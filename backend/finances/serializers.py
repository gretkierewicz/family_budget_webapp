from rest_framework import serializers

from backend.finances.models import Budget


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Budget
        fields = ["url", "name", "owner"]

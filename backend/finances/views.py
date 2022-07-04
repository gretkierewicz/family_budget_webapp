from rest_framework import mixins, permissions, viewsets
from rest_framework_nested.viewsets import NestedViewSetMixin

from backend.finances.models import Budget, CashFlow
from backend.finances.serializers import (
    BudgetSerializer,
    CashFlowSerializer,
    SharedBudgetSerializer,
)


class BudgetView(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SharedBudgetView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Budget.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SharedBudgetSerializer

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(shared_with=user)


class CashFlowView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = CashFlow.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CashFlowSerializer

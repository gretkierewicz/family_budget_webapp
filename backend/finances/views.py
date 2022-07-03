from rest_framework import permissions, viewsets

from backend.finances.models import Budget
from backend.finances.serializers import BudgetSerializer


class BudgetView(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

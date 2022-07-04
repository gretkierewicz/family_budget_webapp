"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from backend.api_auth import views as auth_views
from backend.finances import views as finance_views

router = routers.DefaultRouter()
router.register(r"register", auth_views.RegisterView, basename="register")
router.register(r"user", auth_views.UserView)
router.register(r"budgets", finance_views.BudgetView)
router.register(
    r"shared_budgets", finance_views.SharedBudgetView, basename="shared_budgets"
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api_auth/", include("rest_framework.urls", namespace="rest_framework")),
]

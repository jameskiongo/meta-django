from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    # path("menu-items/", views.MenuItemView.as_view()),
    path("menu-items/<int:pk>", views.single_item),
    path("menu-items", views.menu_items),
    path("secret/", views.secret),
    path("api-token-auth/", obtain_auth_token),
    path("manager-view/", views.manager_view),
    path("throttle-check/", views.throttle_check),
    path("throttle-check-auth/", views.throttle_check_auth),
]

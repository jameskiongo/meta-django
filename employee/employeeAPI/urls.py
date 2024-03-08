from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.task_items),
    path("tasks/<int:id>", views.single_task),
    path("employee/", views.employee_items),
]

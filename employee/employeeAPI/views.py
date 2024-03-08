from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer


@api_view(["GET", "POST"])
def task_items(request):
    if request.method == "GET":
        tasks = Task.objects.select_related("employee").all()
        serialized_task = TaskSerializer(tasks, many=True)
        return Response(serialized_task.data)
    if request.method == "POST":
        serialized_task = TaskSerializer(data=request.data)
        serialized_task.is_valid(raise_exception=True)
        serialized_task.save()
        return Response(serialized_task.data, status.HTTP_201_CREATED)


@api_view()
def single_task(request, id):
    task = get_object_or_404(Task, pk=id)
    serialized_task = TaskSerializer(task)
    return Response(serialized_task.data)


@api_view(["GET", "POST"])
def employee_items(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        serialized_employee = EmployeeSerializer(employee, many=True)
        return Response(serialized_employee.data)
    if request.method == "POST":
        serialized_employee = EmployeeSerializer(data=request.data)
        serialized_employee.is_valid(raise_exception=True)
        serialized_employee.save()
        return Response(serialized_employee.data, status.HTTP_201_CREATED)

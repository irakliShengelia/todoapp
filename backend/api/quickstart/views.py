from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_documentation = {
        'GET: Task List': '/task-list/',
        'GET: Task Details': '/task/<str:pk>/',
        'POST: Create a new Task': '/task-create/',
        'PATCH: Update a Task': '/task-update/<str:pk>/',
        'DEL: Delete a Task': '/task-update/<str:pk>/',
    }
    return Response(api_documentation)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    except:
        return Response([], 404)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['PATCH'])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    except task.DoesNotExist:
        message = "No Tasks Could be found the the provided id"
        return Response({'message': message},404)

@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({"message": "Task Deleted successfully"}, 200)
    except task.DoesNotExist:
        message = "No Tasks Could be found the the provided id"
        return Response({'message': message},404)
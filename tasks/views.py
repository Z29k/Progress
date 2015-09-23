from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.models import Task 
from tasks.serializers import TaskSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def task_list(request):
	"""
	List all tasks, or create a new task
	"""
	if request.method == 'GET':
		tasks = Task.objects.all()
		serializer = TaskSerializer(tasks, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TaskSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

def task_detail(request, pk):
	"""
	Retrieve, update, or delete a task
	"""
	try:
		task = Task.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TaskSerializer(task)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TaskSerializer(task, data=data)
		if serializer.is_valid():
			seralizer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		task.delete()
		return HttpResponse(status=204)
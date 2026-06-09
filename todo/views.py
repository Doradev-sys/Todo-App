from django.shortcuts import render, redirect
from .models import Task

# ------------------------
# HOME PAGE (SHOW + ADD TASK)
# ------------------------
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')

        if title:  # avoid empty tasks
            Task.objects.create(title=title)

        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


# ------------------------
# DELETE TASK (DATABASE)
# ------------------------
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
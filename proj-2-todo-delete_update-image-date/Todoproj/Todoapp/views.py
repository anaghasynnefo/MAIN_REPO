from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm


def Home(req):
    tasks=Task.objects.all()
    print(req.method)

    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get("priority",'')
        date=req.POST.get('date','')
        image=req.FILES['image']
        print (image)
        todo=Task(task=task,priority=priority,date=date)
        todo.save()
    return render(req,"index.html",{"tasks":tasks})

def Update(req,id):
    task=Task.objects.get(id=id)
   
   
    # if req.method=="POST":
    #     task=req.POST.get('task','')
    #     priority=req.POST.get("priority",'')
    #     Task.objects.filter(id=id).update(task=task,priority=priority)
    #     return redirect('home')


    f=TodoForm(req.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect("home")
    return render(req,'update.html',{"task":task,'f':f})
   

    

# def Delete(req,id):
#     tasks=Task.objects.get(id=id)
#     if req.method=="POST":
#         Task.objects.filter(id=id).delete()
#         return redirect('home')
#     return render(req,'delete.html',{"tasks":tasks})
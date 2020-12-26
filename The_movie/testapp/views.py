from django.shortcuts import render
from .models import movie
from .forms import MovieForm


# Create your views here.
def indexview(request):
    return render(request,"testapp/index.html")


def addmovieview(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request,'testapp/addmovie.html',{'form':form})

    if request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            print("Print validation completed.")
            print(form.cleaned_data['rdate'])
            print(form.cleaned_data['moviename'])
            print(form.cleaned_data['hero'])
            print(form.cleaned_data['heroiene'])
            print(form.cleaned_data['rating'])
            form.save()
    return render(request,'testapp/addmovie.html',{'form':form})
            #return indexview(request)



# def addmovieview(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return indexview(request)

#     else:
#         form = MovieForm()
#     return render(request,'testapp/addmovie.html',{'form':form})





















 
        

from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def photo(request):
    return render(request, 'main/photo.html')

def words(request):
    return render(request, 'main/words.html')
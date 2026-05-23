from django.shortcuts import render
import requests
def user_list(request):
    response=requests.get("https://jsonplaceholder.typicode.com/users/")
    users=response.json()
    return render(request,"users.html",{"users":users})
# Create your views here.

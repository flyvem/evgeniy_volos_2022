from django.shortcuts import render

# def about(request):
#     a = 5+6
#     return render(request,'about.html',{'gretting':a})

def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request,'reverse.html',{'word':reverse})

def home(request):
    return render(request, 'home.html')
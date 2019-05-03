from django.shortcuts import render
from peoplebook.peoples import peoples

# Create your views here.
def users_list(request, display='small'):
    context = {
        'display': display,
        'users': peoples
    }
    return render(request,'peoplebook/users_list.html', context)

def users_detail(request, name):
    context = {
        'user': peoples[name],
    }

    return render(request,'peoplebook/users_detail.html', context)
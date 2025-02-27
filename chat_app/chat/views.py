
# Create your views here.
from django.shortcuts import render

def room(request, room_name):
    return render(request, 'chat/room.html', {
        "room_name": room_name,
        "username": request.user.username if request.user.is_authenticated else "",  # Pass username
    })

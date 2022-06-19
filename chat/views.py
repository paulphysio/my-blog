from theblog.forms import msgForm
from theblog.models import ChatMessage, Friend, Profile
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context  = {"user":user, "friends":friends}
    return render(request, "chat/index.html", context)

def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    chats = ChatMessage.objects.all()
    profile = Profile.objects.get(id = friend.profile.id)
    form = msgForm()
    if request.method == "POST":
        form = msgForm(request.POST)
        if form.is_valid():
            chatMessage =  form.save(commit=False)
            chatMessage.msg_sender = user
            chatMessage.msg_receiver = profile
            chatMessage.save()

            return redirect("detail", pk=friend.profile.id)
    context  = {
        "friend":friend,
         "form":form,
         "user":user,
         "profile":profile,
         "chats":chats
        }
    return render(request, "chat/detail.html", context)
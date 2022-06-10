from django.shortcuts import render
from appTwo.models import User


# Create your views here.
def index(request):
    context_dict = {'title_text': 'It`s working', 'body_text': 'Use links to see user list!'}
    return render(request, 'appTwo/index.html', context_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context=user_dict)

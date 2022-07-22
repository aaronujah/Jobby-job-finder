from multiprocessing import context
from django.shortcuts import render, redirect

from .models import Company, Job, User



def JobCollect(name, website):
    user = User.objects.get(id=request.user.id)

    
    context = {'industry': industry}
    return context

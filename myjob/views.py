from http import client
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

from .models import Company, Job, User
from .forms import CompanyForm, UserForm, MyUserCreationForm

# Create your views here.

def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'This User does not exist')

        user = authenticate (request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Email OR Password is Incorrect')

    context = {'page':page}
    return render(request, 'myjob/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home') 

def registerPage(request):
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    
    return render(request, 'myjob/login_register.html', {'form':form})


@login_required(login_url='login')
def home(request):
    user = User.objects.get(id=request.user.id)
    jobs = Job.objects.filter(client=user)
    saves = jobs.filter(saved=True)
    companies = Company.objects.filter(user=user)
    job_set = Job.objects.order_by('company') 

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if request.method == 'POST':
        job.saved = not job.saved
        job.save()
   
    jobs_get = jobs.filter(
        Q(industry__icontains=q) |
        Q(company__name__icontains=q) |
        Q(name__icontains=q) |
        Q(location__icontains=q) |
        Q(description__icontains=q) |
        Q(saved__icontains=q) 
        )

    job_count = jobs_get.count()

    context = {'jobs': jobs, 'jobs_get': jobs_get, 'job_count': job_count, 'companies': companies, 'saves': saves, 'user': user, "job_set": job_set} 
    return render(request, 'myjob/home.html', context)

@login_required(login_url='login')
def job(request, pk):
    user = User.objects.get(id=request.user.id)
    job = Job.objects.get(id=pk)
    jobs = Job.objects.filter(client=user)
    saves = jobs.filter(saved=True)
    companies = Company.objects.filter(user=user)
        
    if request.method == 'POST':
        job.saved = not job.saved
        job.save()
    
    context = {'job': job, 'jobs': jobs, 'saves': saves, 'companies': companies }
    
    return render(request, 'myjob/job.html', context)

@login_required(login_url='login')
def userProfile(request):
    user = User.objects.get(id=request.user.id)
    jobs = Job.objects.filter(client=user)
    companies = Company.objects.filter(user=user)

    context = {'user':user, 'jobs': jobs, 'companies': companies}
    return render(request, 'myjob/profile.html', context)

@login_required(login_url='login')
def createCompany(request):
    form = CompanyForm()
    user = User.objects.get(id=request.user.id)
    
    if request.method == 'POST':
        Company.objects.create(
            user=request.user,
            website=request.POST.get('website'),
            name=request.POST.get('name'),
        )
        return redirect('user-profile')
          
    context = {'form': form}
    return render(request, 'myjob/company_form.html', context)

@login_required(login_url='login')
def updateCompany(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)

    if request.user != company.user:
        return HttpResponse("You're not allowed to do this" )

    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.website = request.POST.get('website')
        company.logo = request.POST.get('logo')
        company.save()
        return redirect('user-profile')    

    context = {'form': form}
    return render(request, 'myjob/company_form.html', context)

@login_required(login_url='login')
def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)

    if request.user != company.user:
        return HttpResponse("You're not allowed to do this" )
    
    if request.method == 'POST':
        company.delete()
        return redirect('home')

    return render(request, 'myjob/delete.html', {'obj':company})

@login_required(login_url='login')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)

    if request.user != job.user:
        return HttpResponse("You're not allowed to do this" )
    
    if request.method == 'POST':
        job.delete()
        return redirect('home')

    return render(request, 'myjob/delete.html', {'obj':job})

@login_required(login_url='login')
def deleteSaved(request, pk):
    save = Job.objects.get(id=pk).filter(saved=True)


    if request.user != save.user:
        return HttpResponse("You're not allowed to do this" )
    
    if request.method == 'POST':
        save.delete()
        return redirect('home')

    return render(request, 'myjob/delete.html', {'obj':save})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form =UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'myjob/update-user.html', {'form': form})

@login_required(login_url='login')
def companiesPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    user = User.objects.get(id=request.user.id)
    jobs = Job.objects.filter(client=user)
    companies_all = user.company_set.all()
    companies = companies_all.filter(name__icontains=q)
    return render(request, 'myjob/companies.html', {'companies': companies, 'jobs': jobs})

@login_required(login_url='login')
def savedPage(request):
    user = User.objects.get(id=request.user.id)
    jobs = user.job_set.all()
    saves = jobs.saved
    
    return render(request, 'myjob/saved.html', {'saves': saves})


# def createJob(request):
#     user = User.objects.get(id=pk)  
#     companies = user.company_set.all()

#     for company in companies:
#         company_name = company.name
#         website = company.website
#         input = JobCollect(company_name, website)

#         industry_all = Industry.objects.all()
#         if industry_name not  in industry_all:
#             industry, created = Industry.objects.get_or_create(name=industry_name)
        
#         Job.objects.create(
#             client=request.user,
#             industry=industry,
#             name=name,
#             company=company,
#             description=description,
#             information=information,
#             location=location,
#             url=url  
#         )
#         return redirect('home') 

#     context = {'form': form}
#     return render(request, 'myjob/home.html', context)
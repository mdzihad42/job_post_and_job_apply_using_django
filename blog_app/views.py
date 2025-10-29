from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from blog_app.models import*
from django.contrib.auth.hashers import check_password

def registerPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        user_exists=UserInfoModel.objects.filter(username=username).exists()
        if user_exists:
            return redirect('registerPage')
        if password==confirm_password:
            UserInfoModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type
            )
            return redirect('loginPage')
    return render(request,'auth/register.html')
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('homePage')
    return render(request,'auth/login.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required
def changePassword(request):
    if request.method=="POST":
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        Confirm_new_password=request.POST.get('Confirm_new_password')
        if check_password(old_password,request.user.password):
            if new_password==Confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
            return redirect('loginPage')
    return render(request,'auth/change_password.html')
@login_required
def jobAddPage(request):
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        location=request.POST.get('location')
        description=request.POST.get('description')
        skills_required=request.POST.get('skills_required')
        salary=request.POST.get('salary')
        application_deadline=request.POST.get('application_deadline')
        employeeModel(
            job_title=job_title,
            company_name=company_name,
            location=location,
            description=description,
            skills_required=skills_required,
            salary=salary,
            application_deadline=application_deadline,
        ).save()
        return redirect('jobPostPage')
    return render(request,'job/jobAdd.html')

@login_required
def jobPostPage(request):
    query = request.GET.get('query', '')
    if query:
        jobs = employeeModel.objects.filter(
            job_title__icontains=query
        ) | employeeModel.objects.filter(
            location__icontains=query
        ) | employeeModel.objects.filter(
            skills_required__icontains=query
        )
    else:
        jobs = employeeModel.objects.all()

    return render(request, 'job/job_post.html', {'job_data': jobs})

@login_required
def applyJob(request):
    if request.user.user_type == 'Employee':
        apply_data=job_seekerModel.objects.all()
    else:
        apply_data=job_seekerModel.objects.filter(created_by=request.user)
    return render(request,'apply/applyjob.html',{'apply_data':apply_data})
def applyJobDlt(request,id):
    job_seekerModel.objects.get(id=id).delete()
    return redirect('applyJob')
def Shortlisted(request,id):
    short=job_seekerModel.objects.get(id=id)
    if short.job_stataus == 'Pending':
        short.job_stataus='Shortlisted'
    elif short.job_stataus == 'Rejected':
        short.job_stataus='Shortlisted'
    
    short.save()
    return redirect('applyJob')
def Rejected(request,id):
    short=job_seekerModel.objects.get(id=id)
    if short.job_stataus == 'Pending':
        short.job_stataus='Rejected'
    elif short.job_stataus == 'Shortlisted':
        short.job_stataus='Rejected'
    short.save()
    return redirect('applyJob')
@login_required
def applyAdd(request):
    if request.method=='POST':
        cv=request.FILES.get('cv')
        job_seekerModel(
            cv=cv,
            created_by=request.user,
            job_stataus='Pending',
        ).save()
        return redirect('homePage')
    return render (request,'apply/applyadd.html')
def jobEdit(request,id):
    edit_data=employeeModel.objects.get(id=id)
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        location=request.POST.get('location')
        description=request.POST.get('description')
        skills_required=request.POST.get('skills_required')
        salary=request.POST.get('salary')
        application_deadline=request.POST.get('application_deadline')
        employeeModel(
            id=id,
            job_title=job_title,
            company_name=company_name,
            location=location,
            description=description,
            skills_required=skills_required,
            salary=salary,
            application_deadline=application_deadline
        ).save()
        return redirect('jobPostPage')
    return render(request,'job/job_edit.html',{'edit_data':edit_data})

def jobDlt(request,id):
    employeeModel.objects.get(id=id).delete()
    return redirect('jobPostPage')


def homePage(request):
    job_data=employeeModel.objects.all()
    return render(request,'master/base.html',{'job_data':job_data})
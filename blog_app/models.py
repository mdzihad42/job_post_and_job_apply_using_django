from django.db import models
from django.contrib.auth.models import AbstractUser
class UserInfoModel(AbstractUser):
    user=[
        ('Employee','Employee' ),
        ('Job_Seeker','Job_Seeker'),

    ]
    user_type=models.CharField(choices=user , max_length=30,null=True)
    
    def __str__(self):
        return self.username
    
    
class employeeModel(models.Model):
    job_title = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    description = models.TextField()
    skills_required = models.TextField()
    salary = models.CharField(max_length=100,null=True)
    application_deadline = models.DateField()  

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
class job_seekerModel(models.Model):
    status=[
        ('Pending','Pending'),
        ('Shortlisted','Shortlisted'),
        ('Rejected','Rejected'),
    ]
    cv=models.FileField(null=True,upload_to='job/file')
    created_by=models.ForeignKey(UserInfoModel, null=True,on_delete=models.CASCADE)
    publishdate=models.DateTimeField(auto_now_add=True, null=True)
    job_stataus=models.CharField(choices=status,max_length=20, null=True)
    
    
    
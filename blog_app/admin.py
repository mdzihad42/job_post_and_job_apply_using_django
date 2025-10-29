from django.contrib import admin
from blog_app.models import*
admin.site.register([UserInfoModel,job_seekerModel, employeeModel])

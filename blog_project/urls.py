from blog_app.views import*
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerPage/',registerPage,name='registerPage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('changePassword/',changePassword,name='changePassword'),
    path('',homePage,name='homePage'),
    
    
    path('jobAddPage/',jobAddPage,name='jobAddPage'),
    path('jobPostPage/',jobPostPage,name='jobPostPage'),
    path('jobDlt/<int:id>',jobDlt,name='jobDlt'),
    path('jobEdit/<int:id>',jobEdit,name='jobEdit'),
    
    path('applyAdd/',applyAdd,name='applyAdd'),
    path('applyJob/',applyJob,name='applyJob'),
    path('applyJobDlt/<int:id>',applyJobDlt,name='applyJobDlt'),
    
    path('Shortlisted/<int:id>',Shortlisted,name='Shortlisted'),
    path('Rejected/<int:id>',Rejected,name='Rejected'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

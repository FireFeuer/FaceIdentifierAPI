from django.contrib import admin
from django.urls import path
from .views import UploadImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', UploadImageView.as_view(), name='upload'),
]

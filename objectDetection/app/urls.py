from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('upload/', image_upload, name='image_upload'),
    path('image_info/<int:image_id>/', image_info, name='image_info'),

]

from django.urls import path
from app_templates import views

# Template tagging
app_name = 'app_templates'

# url patterns

urlpatterns = [
    path('other/', views.other, name='other'),
    path('url_templates_info/', views.url_templates_info, name='url_templates_info'),
]

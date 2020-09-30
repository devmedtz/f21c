from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.StudentFormView.as_view(), name='application-form'),
    path('ajax/load-logo/', views.load_logos, name='ajax_load_logos'),
    path('ajax/load-fee/', views.load_fee, name='ajax_load_fee'),
    path('ajax/load-forms/', views.load_forms, name='ajax_load_forms'),  # <-- this one here
     # <-- this one here
    path('success/<str:student_id>/', views.success, name='success'),
    path('pdf/<str:student_id>/', views.GeneratePdf.as_view(), name='pdf'),
]

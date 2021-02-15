from django.urls import path
from .import views

app_name = 'admins'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('add-school/', views.SchoolCreate.as_view(), name='add-school'),
    path('schools/', views.SchoolListView.as_view(), name='schools'),
    path('school/<int:pk>/edit/', views.SchoolUpdateView.as_view(), name='edit-school'),
    path('school/<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='delete-school'),
    path('app-fee/', views.ApplicationFeeView.as_view(), name='app-fee'),
    path('app-fee/list', views.ApplicationFeeListView.as_view(), name='app-fee-list'),
    path('app-fee/<int:pk>/edit/', views.ApplicationFeeUpdate.as_view(), name='app-fee-edit'),
    path('app-fee/<int:pk>/delete/', views.ApplicationFeeDelete.as_view(), name='app-fee-delete'),
    path('students/', views.StudentsListView.as_view(), name='students'),
    path('update/<int:pk>/update/', views.StudentUpdate.as_view(), name='update-student'),
    path('pdf/<int:id>/', views.GeneratePdfViews.as_view(), name='pdf'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('student/export/excel/', views.ExportStudentsCsv.as_view(), name='student-export-excel'),
    path('week_ago_application/', views.week_ago_application, name='week_ago_application'),
]
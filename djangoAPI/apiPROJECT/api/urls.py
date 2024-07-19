from django.urls import path
from . import views
urlpatterns = [
    path('', views.ApiOverview),
    path('courses/', views.get_courses, name="ViewCourses"),
    path('courses/add/', views.add_course, name="AddCourse"),
    path('courses/<str:id>/update', views.update_course, name="UpdateCourse"),
    path('courses/<str:id>/delete', views.delete_course, name="DeleteCourse"),
]
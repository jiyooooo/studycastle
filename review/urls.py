from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('write/', views.WriteView.as_view(), name="write"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/update', views.UpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name="delete"),

]
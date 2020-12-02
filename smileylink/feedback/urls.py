from django.urls import path

from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_id>/', views.detail, name='detail'),
    path('edit/<int:account_id>', views.edit, name='edit'),
]

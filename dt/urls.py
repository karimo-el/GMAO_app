from django.urls import path
from . import views

urlpatterns = [
    path('',views.handel_work_request, name = 'handel_work_request'),
    path('<int:id>', views.handel_view_work_request, name = 'handel_view_wr'),
    path('add/', views.handel_new_wr, name= 'add_wr'),
    path('edit/<int:id>/',views.handel_edit_wr, name = 'edit_wr' ),
    path('delete/<int:id>/', views.handel_delete_wr, name = ("delete_wr")),

] 
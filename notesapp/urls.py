
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BasePage),
    path('home/', views.Index),
    path('addnewnote/', views.AddNewNotes),
    path('editnote/<int:id>/', views.UpdateNote),
    path('deletenote/<int:id>/', views.DeleteNote),
]



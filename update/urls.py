from django.urls import path
from .import views
urlpatterns = [
  path('',views.Main,name='Addmployee'),
  path('/add',views.Uploadform,name='Uploadform'),
  path('add/<id>/',views.Detailed_View,name='Detailed_View'),
  path('update/<id>/',views.UpdateForm,name='update'),
  path('delete/<id>/',views.Delete,name='delete'),
 
]
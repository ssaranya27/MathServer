from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofcylinder/',views.cylinderarea,name="areaofcylinder"),
    path('',views.cylinderarea,name="areaofcylinderroot")
]

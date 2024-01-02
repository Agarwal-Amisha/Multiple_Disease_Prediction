from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
        path("",views.index,name='home'),
        path("heart.html",views.heart,name='heart'),
        path("diabetes.html",views.diabetes,name='diabetes'),
        path("cancer.html",views.cancer,name='cancer'),
        path("heart_result.html",views.heart_result,name='heart_result'),
        path("diabetes_result.html",views.diabetes_result,name='diabetes_result'),
        path("cancer_result.html",views.cancer_result,name="cancer_result")
]
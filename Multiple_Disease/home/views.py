from django.shortcuts import render,HttpResponse
import pickle
from joblib import load
import sklearn

# Create your views here.
def index(request):
    return render(request,"index.html")

def heart(request):
    return render(request,"heart.html")

def diabetes(request):
    return render(request,"diabetes.html")

def cancer(request):
    return render(request,"cancer.html")

def heart_result(request):
        heart_model = pickle.load(open("static/heart_prediction.sav", 'rb'))

        lis1 = [
            float(request.GET['Age']),
            float(request.GET['Sex']),
            float(request.GET['Cheast Pain Type']),
            float(request.GET['Resting Blood Pressure']),
            float(request.GET['Serum Cholestrol in mg/dl']),
            float(request.GET['Fasting Blood Sugar']),
            float(request.GET['Resting Electrocardiographic results']),
            float(request.GET['maximum heart rate achieved']),
            float(request.GET['Excercise Induced Angina']),
            float(request.GET['ST depression induced by excercise']),
            float(request.GET['Slope of the peak ST segment']),
            float(request.GET['Major Vessel colored by florosopy']),
            float(request.GET['thal']),
        ]
        print(lis1)
        ans = heart_model.predict([lis1])
        if ans[0]==0:
            diagnosis_res = 'The Person does not have a Heart Disease' 
        else:
            diagnosis_res ='The Person has a Heart Disease'

        return render(request, "heart_result.html", {'ans': diagnosis_res})

def diabetes_result(request):
    diabetes_model=pickle.load(open("static/diabetes_prediction.sav",'rb'))
    
    lis2= [
        float(request.GET['Pregnancies']),
        float(request.GET['Glucose']),
        float(request.GET['BP']),
        float(request.GET['ST']),
        float(request.GET['Insulin']),
        float(request.GET['BMI']),
        float(request.GET['DPF']),
        float(request.GET['Age']),
    ]    
    print(lis2)
    ans=diabetes_model.predict([lis2])
    diagnosis_res=''
    if ans[0]==0:
        diagnosis_res = 'The Person does not have Diabetes' 
    else:
        diagnosis_res ='The Person has Diabetes'

    return render(request, "diabetes_result.html", {'ans': diagnosis_res})

def cancer_result(request):
    cancer_model=pickle.load(open("static/cancer_prediction.sav",'rb'))
    lis3= [
        float(request.GET['rm']),
        float(request.GET['pm']),
        float(request.GET['am']),
        float(request.GET['cm']),
        float(request.GET['cpm']),
        float(request.GET['rs']),
        float(request.GET['as']),
        float(request.GET['rw']),
        float(request.GET['pw']),
        float(request.GET['aw']),
        float(request.GET['cpw']),
    ]    
    print(lis3)
    ans=cancer_model.predict([lis3])
    diagnosis_res=''
    if ans[0]==0:
        diagnosis_res = 'The Person does not have cancer' 
    else:
        diagnosis_res ='The Person has cancer'

    return render(request, "cancer_result.html", {'ans': diagnosis_res})   
     
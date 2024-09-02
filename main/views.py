from django.shortcuts import render
from insurance_prediction.forms import FeedbackForm
from main.models import FeedbackModel

import joblib
model = joblib.load('static/insurance/random_forest_regressor')
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def predict(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        children = int(request.POST.get('children'))
        bmi = float(request.POST.get('bmi'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))
        pred = model.predict([[age, sex, bmi, children, smoker, region]])
        
        return render(request, 'predict.html', {'output': round(pred[0])})
    
    else:
        return render(request, 'predict.html')

def contact(request):
    fm = FeedbackForm()
    if request.method == 'POST':
        em = request.POST.get('email')
        msg = request.POST.get('message')
        contact = FeedbackModel(email=em,message=msg)
        contact.save
        print(em, msg)
        
    return render(request, 'contact.html', {'form':fm})


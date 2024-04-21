from django.shortcuts import render
from classification.models import Prediction
from classification.forms import PredictionForm
from classification.utils import sun_predict
import matplotlib.pyplot as plt 
# Create your views here.


def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Prediction.objects.last()
            pred = sun_predict(img.image.path)
            img.prediction = pred 
            img.save()            
        return render(request, "classification/predict.html", {"form": form, "img":img, "pred": pred})

    # Get 
    form = PredictionForm()
    return render(request, "classification/predict.html", {"form": form})



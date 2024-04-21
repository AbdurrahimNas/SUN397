from django.forms import ModelForm
from classification.models import Prediction 

class PredictionForm(ModelForm):

    class Meta:
        model=Prediction
        fields = ["image"]



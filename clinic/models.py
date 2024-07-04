from django.db import models
from django.contrib.auth.models import User
from sklearn.ensemble import RandomForestClassifier
import joblib
from django import forms
from django.contrib import admin
import random
import string

# Create your models here.
def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9)) 
#Table Farmer
class Farmer(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    farm_id = models.CharField(max_length=9, default=generate_random_code, db_index=True, editable = False)
    N = models.FloatField(max_length=15)
    P = models.FloatField(max_length=15)
    K = models.FloatField(max_length=15)
    temperature = models.FloatField(max_length=15)
    humidity = models.FloatField(max_length=15)
    ph = models.FloatField(max_length=15)
    rainfall = models.FloatField(max_length=15)
    label = models.CharField(max_length=100, blank=True,editable=False)
    complete = models.BooleanField(default=False, editable = False)
    created = models.DateTimeField(auto_now_add=True)
    #Function to load the model
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/model_agri-ai.joblib')
        self.label = ml_model.predict([[self.N, self.P, self.K, self.temperature, self.humidity, self.ph, self.rainfall]])
        return super().save(*args, *kwargs)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['complete']


    
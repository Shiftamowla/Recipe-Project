from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Custom_user(AbstractUser):
    USER=[
        ('viewers','Viewers'),
        ('creator','Creator')
    ]

    user_type=models.CharField(choices=USER,max_length=100,null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    
class viewersProfileModel(models.Model):
    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='viewersProfile')
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    
    
    def __str__(self):
        return f"{self.user.username}"   
    
class CreatorProfileModel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE,related_name='bloggersProfile')
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    
    def __str__(self):
        return f"{self.user.username}"
    

class RecipePostModel(models.Model):
    
    Tag=[
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non-Vegetarian'),

    ]
    Level=[
        ('high','high'),
        ('medium','Medium'),
        ('low','Low'),

    ]
    CATEGORY=[
        ('breakfast','breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),

    ]
    
    user=models.ForeignKey(Custom_user,on_delete=models.CASCADE,null=True)
    
    RecipeTitle=models.CharField(max_length=500,null=True)
    Nutritional_Info=models.CharField(max_length=500,null=True)
    Ingredients=models.CharField(max_length=1000,null=True)
    Instructor=models.CharField(max_length=1000,null=True)
    Category=models.CharField(choices=CATEGORY, max_length=100,null=True)
    Tag=models.CharField(choices=Tag, max_length=100,null=True)
    DifficultyLevel=models.CharField(choices=Level, max_length=100,null=True)
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    PreparetionTime = models.DateTimeField(default=timezone.now,null=True)
    CookingTime = models.DateTimeField(default=timezone.now,null=True)
    TotalTime = models.DateTimeField(default=timezone.now,null=True)
    
    def __str__(self):
        return f"{self.RecipeTitle} "
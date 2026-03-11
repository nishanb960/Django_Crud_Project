from django.db import models
class Students(models.Model):
    name= models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    
    def _str_(self):
        return self.name
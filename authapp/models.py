from django.db import models
class ContactModel(models.Model):
    n_ame=models.CharField(max_length=25)
    e_mail=models.EmailField(max_length=25)
    p_hone=models.CharField(max_length=25)

    def __str__(self):
        return self.e_mail
    
class diettrack(models.Model):
    d_ate=models.CharField(max_length=25)
    meal=models.CharField(max_length=25)
    calories=models.CharField(max_length=25)
    height=models.CharField(max_length=25)
    weight=models.CharField(max_length=25)
    waterintake=models.CharField(max_length=25)
    notes=models.CharField(max_length=200)

    def __str__(self):
        return self.d_ate


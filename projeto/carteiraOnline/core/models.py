from django.db import models
import datetime
from django.utils import timezone
# Create your models here.




class Conta(models.Model):
    nr_conta_text = models.CharField(max_length=200)
    money_text = models.CharField(max_length=200)

    localidade_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=200)
    nr_telemovel_text = models.CharField(max_length=11)

    premium = models.BooleanField()


    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nr_conta_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




# class Money_euros(models.Model):
#     money_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.money_text
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text


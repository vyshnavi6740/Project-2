from django.db import models

# Create your models here.
class Usermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "usermodel"

class Accuracymodel(models.Model):
    svm_acc = models.CharField(max_length=100)
    rfc_acc = models.CharField(max_length=100)
    gbc_acc = models.CharField(max_length=100)
    dnn_bert_acc = models.CharField(max_length=100)
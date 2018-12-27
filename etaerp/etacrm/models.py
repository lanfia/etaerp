from django.db import models
fr

class Customer(models.Model):
    customer_reference_number = models.CharField('Customer Reference Number', max_length=20)
    private_or_company = models.BooleanField()



class Contact(models.Model):
    customer_reference_number = models.Foreignkey()

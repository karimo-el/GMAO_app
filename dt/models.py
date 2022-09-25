from django.db import models

class Agents(models.Model):
    CHOICES = (("Electrique","Electrique"), ("Mecanique","Mecanique"), ("Exploitation","Exploitation"), ("Securité", "Securité"), ("BDM", "BDM"))
    First_Name = models.CharField(max_length = 100, verbose_name = 'Nom')
    Last_Name = models.CharField(max_length = 100, verbose_name = 'Prenom')
    Function = models.CharField(max_length = 100, verbose_name = 'Function')
    Service  = models.CharField(choices =CHOICES, max_length = 20, verbose_name = "Service" )


# Create your models here.
def from_500():
    '''
    Returns the next default value for the `ones` field,
    starts from 500
    '''
    # Retrieve a list of `YourModel` instances, sort them by
    # the `ones` field and get the largest entry
    largest = work_request.objects.all().order_by('number_DT').last()
    if not largest:
        # largest is `None` if `YourModel` has no instances
        # in which case we return the start value of 500
        return 1
    # If an instance of `YourModel` is returned, we get it's
    # `ones` attribute and increment it by 1
    return largest.number_DT + 1

class work_request(models.Model):
    CHOICES = (("Electrique","Electrique"), ("Mecanique","Mecanique"), ("Commun","Commun"))
    number_DT= models.PositiveIntegerField(verbose_name = 'N°_DT', default=from_500)
    first_name = models.CharField(max_length =20, verbose_name = 'Nom')
    last_name = models.CharField(max_length = 20, verbose_name = 'Prenom')
    equipement = models.CharField(max_length = 20, verbose_name = 'Equipement')
    installation = models.CharField(max_length = 20, verbose_name = 'Installation')
    anomlie = models.TextField(max_length =500, verbose_name = 'Anomalie')
    service_conserne = models.CharField(choices= CHOICES, max_length = 20, verbose_name = 'Service consernée')
    Status = models.CharField( max_length=10, verbose_name = 'Action')
    date_creation = models.DateField()
    date_modifie = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.equipement


# class raport_intervention(models.Model):
#     pass
    
    

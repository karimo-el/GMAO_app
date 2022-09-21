from django.db import models

# Create your models here.


class work_request(models.Model):
    number_DT= models.PositiveIntegerField(verbose_name = 'N°_DT')
    first_name = models.CharField(max_length =20, verbose_name = 'Nom')
    last_name = models.CharField(max_length = 20, verbose_name = 'Prenom')
    equipement = models.CharField(max_length = 20, verbose_name = 'Equipement')
    installation = models.CharField(max_length = 20, verbose_name = 'Installation')
    anomlie = models.TextField(max_length =500, verbose_name = 'Anomalie')
    service_conserne = models.CharField(max_length = 20, verbose_name = 'Service consernée')
    Status = models.CharField(max_length = 20, verbose_name = 'Action')
    date_creation = models.DateTimeField()
    date_modifie = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.equipement


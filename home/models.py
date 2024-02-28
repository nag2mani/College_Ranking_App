from django.db import models
from django.contrib.auth.models import User

class Colleges_model(models.Model):
    # title = models.CharField(max_length=1000)
    # link = models.URLField()
    Original_Rank = models.IntegerField()
    New_Rank = models.IntegerField()
    Change = models.IntegerField()
    College = models.CharField(max_length=255)
    Fees = models.DecimalField(max_digits=10, decimal_places=2)
    Faculty = models.CharField(max_length=255)
    SS = models.DecimalField(max_digits=10, decimal_places=2)
    FSR = models.DecimalField(max_digits=10, decimal_places=2)
    FQE = models.DecimalField(max_digits=10, decimal_places=2)
    FRU = models.DecimalField(max_digits=10, decimal_places=2)
    PU = models.DecimalField(max_digits=10, decimal_places=2)
    QP = models.DecimalField(max_digits=10, decimal_places=2)
    IPR = models.DecimalField(max_digits=10, decimal_places=2)
    FPPP = models.DecimalField(max_digits=10, decimal_places=2)
    GPH = models.DecimalField(max_digits=10, decimal_places=2)
    GUE = models.DecimalField(max_digits=10, decimal_places=2)
    GMS = models.DecimalField(max_digits=10, decimal_places=2)
    GPHD = models.DecimalField(max_digits=10, decimal_places=2)
    RD = models.DecimalField(max_digits=10, decimal_places=2)
    WD = models.DecimalField(max_digits=10, decimal_places=2)
    ESCS = models.DecimalField(max_digits=10, decimal_places=2)
    PCS = models.DecimalField(max_digits=10, decimal_places=2)
    PR = models.DecimalField(max_digits=10, decimal_places=2)
    xx = models.DecimalField(max_digits=10, decimal_places=2)
    Total = models.DecimalField(max_digits=10, decimal_places=2)


# class Job(models.Model):
#     company_name = models.CharField(max_length=1000)
#     skills = models.CharField(max_length=10000)
#     posted_date = models.CharField(max_length=1000, null=True)
#     apply_link = models.URLField()


from django.db import models


# Create your models here.
class StaffProfile(models.Model):  # Staff information
    staff_no = models.IntegerField(primary_key=True)
    staff_name = models.TextField(max_length=200)
    designation = models.CharField(max_length=10)
    reporting_officer = models.IntegerField()

    def __str__(self):
        return str(self.staff_no) + '-' + self.staff_name




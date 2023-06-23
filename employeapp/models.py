from django.db import models

# Create your models here.
class adminmodel(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)



class Designation(models.Model):
    AsignDesignation=models.CharField(max_length=60,)

    def __str__(self):
        return self.AsignDesignation


class Team(models.Model):
    Createteam=models.CharField(max_length=60,)
    def __str__(self):
        return self.Createteam

class EmployeeModel(models.Model):
        EmployeeID = models.CharField(max_length=60, default=None, null=True)
        Firstname = models.CharField(max_length=60, null=True)
        Lastname = models.CharField(max_length=60, null=True)
        email = models.EmailField()
        designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
        team = models.ForeignKey(Team, on_delete=models.CASCADE)
        salary = models.IntegerField()
        phonenumber = models.IntegerField()

        def save(self, *args, **kwargs):
            if not self.EmployeeID:
                last_object = self.__class__.objects.last()
                if last_object:
                    last_id = int(last_object.EmployeeID.split('-')[1])
                    new_id = f"EMP-{str(last_id + 1).zfill(3)}"
                else:
                    new_id = "EMP-001"
                self.EmployeeID = new_id

            super().save(*args, **kwargs)

        def __str__(self):
            return self.Firstname
    # def save(self, *args, **kwargs):
    #     if not self.EmployeeID:
    #         highest_id = EmployeeModel.objects.aggregate(models.Max('id'))['id__max']
    #         new_id = "EMP-001"
    #
    #         if highest_id:
    #             highest_id = int(highest_id.split('-')[1])
    #             new_id = f"EMP-{str(highest_id + 1).zfill(3)}"
    #
    #         self.EmployeeID = new_id
    #     else:
    #         id_number = int(self.EmployeeID.split('-')[1])
    #         if id_number < 999:
    #             self.EmployeeID = f"EMP-{str(id_number + 1).zfill(3)}"
    #
    #     super(EmployeeModel, self).save(*args, **kwargs)


class leavetype(models.Model):
    ltype=models.CharField(max_length=60)

    def __str__(self):
        return self.ltype


class leave(models.Model):
    user=models.ForeignKey(EmployeeModel,on_delete=models.CASCADE)
    fromm=models.DateField()
    to=models.DateField()
    type=models.ForeignKey(leavetype,on_delete=models.CASCADE)
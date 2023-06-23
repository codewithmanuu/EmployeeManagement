from django.forms import ModelForm
from.models import *
class adminform(ModelForm):
    class Meta:
        model=adminmodel
        fields='__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        exclude =("EmployeeID",)



class desigForm(ModelForm):
    class Meta:
        model=Designation
        fields='__all__'


class teamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class leaveForm(ModelForm):
    class Meta:
        model=leave
        fields =('fromm','to')

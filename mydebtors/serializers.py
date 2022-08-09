from rest_framework import serializers
from .models import *


class StudentSerializer (serializers.ModelSerializer):
    reg_number = serializers.CharField(read_only = True)
    
    class Meta:
        model = Student
        fields = ['id','reg_number','first_name', 'last_name','middle_name', 'gender', 'student_class', 'passport', 'nationality', 'state', 'address', 'date_of_birth']

    def save(self, **kwargs):
        user = self.context['user']
        self.instance = Student.objects.create(school = user, **self._validated_data)

        return self.instance
    

class SponsorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'




class AddDebtSerializer (serializers.ModelSerializer):
    class Meta:
        model = Debt
        

class DebtSerializer (serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    class Meta:
        model = Debt
        fields = '__all__'


class BioDataSerializer (serializers.Serializer):
    student = StudentSerializer()
    sponsor = SponsorSerializer()
    finance = DebtSerializer()
        


from rest_framework import serializers
from django.core.exceptions import ValidationError
from core.models import School
from .models import *

class AddStudentSerializer (serializers.ModelSerializer):
    reg_number = serializers.CharField(read_only = True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Student
        fields = ['id','reg_number','first_name', 'last_name','middle_name', 'gender', 'student_class', 'passport', 'nationality', 'state', 'address', 'date_of_birth']

    def save(self, **kwargs):
        
    
        self.instance = Student.objects.create(school_id = self.context['school_id'], **self._validated_data)

        return self.instance
    
class StudentSerializer (serializers.ModelSerializer):
    outstanding_fee = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField(read_only = True)
    reason_for_debt = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username') 
    class Meta:
        model = Student
        fields = ['id','reg_number', 'first_name', 'middle_name', 'last_name', 'student_class', 'passport', 'outstanding_fee','school','reason_for_debt', 'debts',] #

    def get_outstanding_fee(self, student:Student):
        try:
            debt = Debt.objects.get(student = student)
        except Debt.DoesNotExist:
            return None

        return debt.outstanding_fee

    def get_reason_for_debt (self, student):

        try:
            debt = Debt.objects.get(student = student)
        except Debt.DoesNotExist:
            return None

        return debt.category

    def get_school (self, student):

        return student.school.name


class ClearedDebtorsSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField(read_only = True)
    outstanding_fee = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Student
        fields = ['id','first_name', 'middle_name', 'last_name', 'student_class', 'passport', 'outstanding_fee','school'] 
        
    def get_school (self, student):

        return student.school.name

    def get_outstanding_fee(self, student:Student):
        try:
            debt = Debt.objects.get(student = student)
        except Debt.DoesNotExist:
            return None
        return debt.outstanding_fee


class SponsorSerializer (serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Sponsor
        fields = '__all__'




class AddDebtSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Debt
        

class DebtSerializer (serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Debt
        fields = ['id', 'session', 'term', 'total_fee', 'outstanding_fee', 'category', 'status', 'student', 'date_created', 'date_updated']


class BioDataSerializer (serializers.ModelSerializer):
    sponsor = SponsorSerializer()
    debts = DebtSerializer(many = True)
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Student
        fields = ['id','reg_number', 'first_name', 'middle_name', 'last_name', 'student_class','sponsor', 'debts']
        


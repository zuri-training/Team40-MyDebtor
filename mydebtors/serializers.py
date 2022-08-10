from warnings import catch_warnings
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from core.models import School
from .models import *

class AddStudentSerializer (serializers.ModelSerializer):
    reg_number = serializers.CharField(read_only = True)
    
    class Meta:
        model = Student
        fields = ['id','reg_number','first_name', 'last_name','middle_name', 'gender', 'student_class', 'passport', 'nationality', 'state', 'address', 'date_of_birth']

    def save(self, **kwargs):
        user = self.context['user']
        self.instance = Student.objects.create(user = user, **self._validated_data)

        return self.instance
    
class StudentSerializer (serializers.ModelSerializer):
    outstanding_fee = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField(read_only = True)
    reason_for_debt = serializers.SerializerMethodField()

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

        User = get_user_model()

        try:
            user_obj = User.objects.get(id = student.user.id)

            school = School.objects.get(user = user_obj)

        except:
            return None
        
        return school.name


class ClearedDebtorsSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField(read_only = True)
    outstanding_fee = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id','first_name', 'middle_name', 'last_name', 'student_class', 'passport', 'outstanding_fee','school',] #
        
    def get_school (self, student):

        User = get_user_model()

        try:
            user_obj = User.objects.get(id = student.user.id)
            school = School.objects.get(user = user_obj)
        except:
            return None
        return school.name

    def get_outstanding_fee(self, student:Student):
        try:
            debt = Debt.objects.get(student = student)
        except Debt.DoesNotExist:
            return None
        return debt.outstanding_fee


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
        fields = ['id', 'session', 'term', 'total_fee', 'outstanding_fee', 'category', 'status', 'student', 'date_created', 'date_updated']


class BioDataSerializer (serializers.ModelSerializer):
    # student = StudentSerializer()
    sponsor = SponsorSerializer()
    debts = DebtSerializer(many = True)
    class Meta:
        model = Student
        fields = ['id','reg_number', 'first_name', 'middle_name', 'last_name', 'student_class','sponsor', 'debts']
        


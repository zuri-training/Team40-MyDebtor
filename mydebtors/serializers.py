from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import *


class SchoolSerializer (serializers.ModelSerializer):
    debtors = serializers.SerializerMethodField()
    cleared_debtors = serializers.SerializerMethodField()
    contenders = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'reg_number', 'name',
                  'category', 'state', 'LGA', 'logo', 'address', 'debtors', 'cleared_debtors', 'contenders']

    def get_debtors(self, school):
        return school.students.count()

    def get_cleared_debtors(self, school):
        cleared = Student.objects.filter(
            debts__status='resolved', school=school)
        return cleared.count()

    def get_contenders(self, school):
        return school.complaints.count()


class PrincipalSerializer (serializers.ModelSerializer):
    #user = serializers.IntegerField(read_only =True)
    class Meta:
        model = Principal
        fields = ['id', 'name', 'gender', 'date_of_birth', 'address',
                  'id_type', 'id_number', 'CAC', 'letter', 'id_card']

    def save(self, **kwargs):

        user = self.context['user']

        self.instance = Principal.objects.create(
            user=user, **self.validated_data)

        return self.instance


class AddStudentSerializer (serializers.ModelSerializer):
    reg_number = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'gender',
                  'student_class', 'passport', 'nationality', 'state', 'address', 'date_of_birth']

    def save(self, **kwargs):

        self.instance = Student.objects.create(
            school_id=self.context['school_id'], **self.validated_data)

        return self.instance


class StudentSerializer (serializers.ModelSerializer):
    outstanding_fee = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField(read_only=True)
    reason_for_debt = serializers.SerializerMethodField()
    sponsor_name = serializers.SerializerMethodField()
    sponsor_NIN = serializers.SerializerMethodField()
    debt_status = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'reg_number', 'first_name', 'middle_name', 'last_name', 'student_class',
                  'passport', 'outstanding_fee', 'school', 'reason_for_debt', 'debt_status', 'sponsor_name', 'sponsor_NIN']

    def get_outstanding_fee(self, student: Student):
        try:
            debt = Debt.objects.get(student=student)
        except Debt.DoesNotExist:
            return None

        return debt.outstanding_fee

    def get_reason_for_debt(self, student):

        try:
            debt = Debt.objects.get(student=student)
        except Debt.DoesNotExist:
            return None

        return debt.category

    def get_debt_status(self, student):
        try:
            debt = Debt.objects.get(student=student)
        except Debt.DoesNotExist:
            return None

        return debt.status

    def get_school(self, student):

        return student.school.name

    def get_sponsor_name(self, student):
        if student.sponsor.first_name is not None:
            return student.sponsor.first_name+" " + student.sponsor.last_name
        return None

    def get_sponsor_NIN(self, student):
        if student.sponsor.NIN is not None:
            return student.sponsor.NIN
        return None


class ClearedDebtorsSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField(read_only=True)
    outstanding_fee = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'middle_name', 'last_name',
                  'student_class', 'passport', 'outstanding_fee', 'school']

    def get_school(self, student):

        return student.school.name

    def get_outstanding_fee(self, student: Student):
        try:
            debt = Debt.objects.get(student=student)
        except Debt.DoesNotExist:
            return None
        return debt.outstanding_fee


class SponsorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class AddDebtorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['session', 'term', 'total_fee',
                  'outstanding_fee', 'category', 'student']

    def save(self, **kwargs):
        user = self.context['user']
        school = School.objects.get(user=user)

        self.instance = Debt.objects.create(
            school=school, **self.validated_data)

        return self.instance


class DebtSerializer (serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Debt
        fields = ['id', 'session', 'term', 'total_fee', 'outstanding_fee',
                  'category', 'status', 'student', 'date_created', 'date_updated']


class BioDataSerializer (serializers.ModelSerializer):
    sponsor = SponsorSerializer()
    debts = DebtSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'reg_number', 'first_name', 'middle_name',
                  'last_name', 'student_class', 'sponsor', 'debts']


class MakeComplaintSerializer (serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['description', 'proof']

    def save(self, **kwargs):
        debt = self.context['debt']
        user = self.context['user']
        school = self.context['school']

        self.instance = Complaint.objects.create(
            user=user, debt=debt, school=school, **self.validated_data)


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'description', 'proof', 'debt', 'school', 'user']

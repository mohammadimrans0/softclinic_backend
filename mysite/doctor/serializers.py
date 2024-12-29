from rest_framework import serializers
from .models import Specialization, Designation, AvailableTime, Doctor, Review
from django.contrib.auth.models import User

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name']

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    designation = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Designation.objects.all()
    )
    specialization = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Specialization.objects.all()
    )
    available_time = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AvailableTime.objects.all()
    )
    class Meta:
        model = Doctor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
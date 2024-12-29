from rest_framework import viewsets, filters, pagination
from rest_framework.permissions import IsAuthenticated

from .models import Specialization, Designation, AvailableTime, Doctor, Review
from .serializers import SpecializationSerializer, DesignationSerializer, AvailableTimeSerializer, DoctorSerializer, ReviewSerializer

# Create your views here.
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)

        return query_set    

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]


class Pagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = Pagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
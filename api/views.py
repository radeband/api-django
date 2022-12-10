from rest_framework import generics, status, viewsets, mixins
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.viewsets import ModelViewSet, generics
# from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin


from .models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class FacilityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilitySerializer
    # TODO: return category_title
    queryset = Facility.objects.all()



from rest_framework import filters

class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
# class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer

    def get_queryset(self):
        type_ids = self.request.query_params.getlist('facility', '')
        # return CompanyBenefits.objects.filter(facility_type__in=type_ids).distinct('company__id')
        return Company.objects.filter(company_benefits__benefit_id__in=type_ids).distinct('id')

    # request [facility_id, type_id]
    # filter_fields = ('facility')
    # search_fields = ['company_facility_types__facility_type_id']
    # filter_backends = (filters.SearchFilter,)
    # queryset = Company.objects.filter(company_facility_types__facility_type_id__overlap=type_ids)
    
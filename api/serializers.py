from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ['id', 'title']


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'title', 'category_title', 'benefits']

    category_title = serializers.ReadOnlyField(source='category.title')
    benefits = BenefitSerializer(many=True, read_only=True)


class CompanyBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBenefit
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'longitude', 'latitude', 'logo', 'company_benefits']

    company_benefits = CompanyBenefitSerializer(many=True, read_only=True)

class CompanySummerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    # company = CompanySerializer()
    # company = CompanySummerySerializer()
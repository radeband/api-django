import uuid
from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "categories"

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1024, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Facility(models.Model):
    class Meta:
        db_table = "facilities"

    title = models.CharField(max_length=255)
    essentiality = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='facilities')


class Benefit(models.Model):
    class Meta:
        db_table = "benefits"

    title = models.CharField(max_length=255)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='benefits')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Company(models.Model):
    class Meta:
        db_table = "companies"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CompanyBenefit(models.Model):
    class Meta:
        db_table = "company_benefits"

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_benefits")
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, related_name="benefits")
    # facility_title = models.CharField(max_length=255)
    # facility_type_title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)

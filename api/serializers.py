from rest_framework import serializers
from .models import Bank, Branch
from rest_framework import serializers, exceptions


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch 
        fields = ('id','ifsc','branch','address','city','district','state','bank_id')
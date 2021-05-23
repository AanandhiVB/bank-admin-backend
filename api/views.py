from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BranchSerializer
from .models import Bank, Branch
# Create your views here.


@api_view(['GET'])
def autocomplete(request):
    
    if request.method == 'GET':
      
        branch   = request.GET.get('q', '').upper()
        limit    = request.GET.get('limit', 0)
        offset   = request.GET.get('offset', 0)
        branches = Branch.objects.filter(branch__contains=branch).order_by('ifsc')[int(offset) : int(offset) + int(limit)]
        
        if branches.exists():

            branch_list = BranchSerializer(branches,many=True)
            return Response({"success": True,
                            "response": {"branches": branch_list.data},
                            "details" : {"message": "Details of branches with the name "+branch+" has been returned"}}, status=status.HTTP_200_OK)

        else:
            return Response({"success": False,
                            "response": "No details found!",
                            "details" : {"message": "No branch details with the name "+branch+" has been found"}}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def search(request):
    
    if request.method == 'GET':
       
        match  = request.GET.get('q', '').upper()
        limit  = request.GET.get('limit', 0)
        offset = request.GET.get('offset', 0)

        ifsc_match      = Branch.objects.filter(ifsc__contains=match)
        branch_match    = Branch.objects.filter(branch__contains=match)
        address_match   = Branch.objects.filter(address__contains=match)
        city_match      = Branch.objects.filter(city__contains=match)
        district_match  = Branch.objects.filter(district__contains=match)
        state_match     = Branch.objects.filter(state__contains=match)
        bankname_match  = Branch.objects.filter(bank__name__contains=match)
        distinct_matches = (ifsc_match | branch_match | address_match | city_match | district_match | state_match | bankname_match).distinct().order_by('ifsc')[int(offset) : int(offset) + int(limit)]
        
        if distinct_matches.exists():

            match_list = BranchSerializer(distinct_matches,many=True)
            return Response({"success": True,
                            "response": {"branches": match_list.data},
                            "details" : {"message": "Bank details with the match "+match+" has been returned"}}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False,
                            "response": "No details found!",
                            "details" : {"message": "No bank details with the match "+match+" has been found"}}, status=status.HTTP_400_BAD_REQUEST)


import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from VaccineApp.models import Human
from VaccineApp.serializers import HumanSerializer

import xlwt


# Create your views here.

@csrf_exempt
def human_api(request, id=0):
    if request.method == 'GET':
        human = Human.objects.all()
        human_serializer = HumanSerializer(human, many=True)
        return JsonResponse(human_serializer.data, safe=False)
    elif request.method == 'POST':
        human_data = JSONParser().parse(request)
        human_serializer = HumanSerializer(data=human_data)
        if human_serializer.is_valid():
            human_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(human_serializer.errors)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        human_data = JSONParser().parse(request)
        human = Human.objects.get(HumanId=human_data['HumanId'])
        human_serializer = HumanSerializer(human, data=human_data)
        if human_serializer.is_valid():
            human_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        human = Human.objects.get(HumanId=id)
        human.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def save_file(request):
    human = Human.objects.all()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0

    cols = ['firstName', 'lastName', 'dateOfBirth', 'address', 'City', 'zipCode', 'landLine', 'cellularPhone',
            'infected', 'conditions']

    for col_num in range(len(cols)):
        ws.write(row_num, col_num, cols[col_num])

    rows = human.values_list('firstName', 'lastName', 'dateOfBirth', 'address', 'City', 'zipCode', 'landLine',
                             'cellularPhone', 'infected', 'conditions')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    wb.save(response)
    return response

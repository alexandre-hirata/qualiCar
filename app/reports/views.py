from django.shortcuts import render
from django.http import HttpResponse

from tablib import Dataset

from json2xml import json2xml
from json2xml.utils import readfromstring

from reports.resources import PartResource

from qualiCar_API.models import Part

def export_data (request):
    if request.method == 'POST':
        # Get option from form
        file_format = request.POST ['file-format']
        part_resource = PartResource ()
        dataset = part_resource.export ()

        if file_format == 'CSV':
            response = HttpResponse (dataset.csv, content_type='text/csv')
            response ['Content-Disposition'] = 'attachment; filename="part_exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse (dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="part_exported_data.json"'
            return response
        elif file_format == 'XLS':
            response = HttpResponse (dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="part_exported_data.xls"'
            return response
        elif file_format == 'XML':
            # This step is using json2xml library
            # To do so, the code converts to JSON to convert (again) to XML
            xml_output = json2xml.Json2xml (readfromstring (dataset.json)).to_xml()

            response = HttpResponse (xml_output, content_type='application/xml')
            response['Content-Disposition'] = 'attachment; filename="part_exported_data.xml"'
            return response


    return render (request, 'forms/export.html')


def import_data(request):
    if request.method == 'POST':
        # Get option from form
        file_format = request.POST ['file-format']
        part_resource = PartResource ()
        dataset = Dataset ()
        new_part = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load (new_part.read().decode('utf-8'),format='csv')
            # Testing data import
            result = part_resource.import_data (dataset, dry_run = True)
        elif file_format == 'JSON':
            imported_data = dataset.load (new_part.read().decode('utf-8'),format='json')
            # Testing data import
            result = part_resource.import_data (dataset, dry_run = True)

        if not result.has_errors():
            # Import now
            part_resource.import_data (dataset, dry_run = False)

    return render(request, 'forms/import.html')

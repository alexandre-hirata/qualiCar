from import_export import resources
from qualiCar_API.models import Part


class PartResource (resources.ModelResource):

    class Meta:
        model = Part

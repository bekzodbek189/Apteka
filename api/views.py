from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['POST'])
def Tablet_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        selling_price = request.POST['selling_price']
        date_srg = request.POST['date_srg']
        img = request.FILES['img']
        return Response(TabletSerializer(Tablet.objects.create(name=name, price=price, selling_price=selling_price, date_srg=date_srg, img=img)).data)
    return Response("Error")
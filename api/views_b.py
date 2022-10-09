from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['POST'])
def ADD(request):
    if User.status == 2:
        product = request.POST['product']
        quantity = request.POST['quantity']
        query = In.objects.create(product_id=product, quantity=quantity)
        return Response(InSerializer(query).data)






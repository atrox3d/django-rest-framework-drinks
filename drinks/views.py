from django.http import HttpRequest, JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request:HttpRequest):
    # get all drinks 
    drinks = Drink.objects.all()
    
    # serialize them 
    serializer = DrinkSerializer(drinks, many=True)

    # return json
    return JsonResponse(serializer.data, safe=False)



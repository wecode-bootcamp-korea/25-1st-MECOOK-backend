import json

from django.http           import JsonResponse
from django.views          import View
from django.db.models      import Q

from .models               import *
from carts.models          import Carts
from users.models          import User
from users.utils           import login_decorator

class OrderView(View):
    @login_decorator
    def get(self, request):
        try:
            selected_items = request.GET.getlist('item', None)
            user           = request.user
            items          = Carts.objects.filter(user=user)
            total          = 0

            for item in items:
                if str(item.id) in selected_items:
                    a      = int(item.product.origin_price_KRW)
                    b      = item.quantity
                    total += a * b
            user.points -= total
            user.save()
            items.delete()

            return JsonResponse({'message': 'point_off'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'key_error'}, status=400)
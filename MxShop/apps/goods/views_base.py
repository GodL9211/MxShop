from django.views.generic.base import View
from .models import Goods

class goods(View):
    def get(self, request):
        goods = Goods.objects.all()
        response_list = []
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category '] = good.category.name
            response_list.append(json_dict)
        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(response_list),content_type="application/json")




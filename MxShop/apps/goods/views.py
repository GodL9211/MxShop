from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.models import Goods
from goods.serializers import GoodsSeriliazer
from rest_framework import generics
from rest_framework import mixins
# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# class GoodsListView(APIView):
#     def get(self, request, format=None ):
#         goods = Goods.objects.all()[0:2]
#         goods_seriliazer = GoodsSeriliazer(goods, many=True)
#         return Response(goods_seriliazer.data)
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 100

# class GoodsListViewSet(generics.GenericAPIView, mixins.ListModelMixin):
class GoodsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSeriliazer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("name", "shop_price")
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price", 0)
    #     if price_min:
    #         queryset = Goods.objects.filter(shop_price__gt=int(price_min))
    #     return queryset
    # def get(self,request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

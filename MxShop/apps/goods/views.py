from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSeriliazer, CategorySeriliazer, IndexCategorySerializer
from rest_framework import generics
from rest_framework import mixins
# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


from django.views import View

from .goodsfilters import GoodsFilter

"""
class GoodsListView(APIView):
    def get(self, request, format=None ):
        goods = Goods.objects.all()[0:2]
        goods_seriliazer = GoodsSeriliazer(goods, many=True)
        return Response(goods_seriliazer.data)
"""

class GoodsPagination(PageNumberPagination):
    page_size = 12  # 每页数目
    page_size_query_param = "page_size"  # 前端发送的每页数目关键字名，默认为None
    page_query_param = "page"  # 前端发送的页数关键字名，默认为"page"
    max_page_size = 100  # 前端最多能设置的每页数量

# class GoodsListViewSet(generics.GenericAPIView, mixins.ListModelMixin):
class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页,分页，过滤，搜索，排序
    """
    """
    对get的参数影响
    ^goods/(?P<uuid>[0-9a-f]{32})/$ [name='goods-detail']
    ^goods/(?P<uuid>[0-9a-f]{32})\.(?P<format>[a-z0-9]+)/?$ [name='goods-detail']
    lookup_field = 'uuid'
    lookup_url_kwarg ='uuid'
    lookup_value_regex = '[0-9a-f]{32}'
    """
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSeriliazer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ("name", "shop_price")  # 未使用filter_class自定义过滤器时使用
    filter_class = GoodsFilter  # 使用自定义过滤器
    search_fields = ("name", 'goods_brief', 'goods_desc')  # 搜索字段, =name表示精确搜索，也可以使用正则
    ordering_fields = ("sold_num", "shop_price" )

    """
    def get_queryset(self):
        queryset = Goods.objects.all()  # 并不会立即去数据库取数据，for循环时才执行取数据 
        price_min = self.request.query_params.get("price", 0)
        if price_min:
            queryset = Goods.objects.filter(shop_price__gt=int(price_min))
        return queryset
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    """

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """"
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySeriliazer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer
from goods.models import Goods, GoodsCategory, Banner, GoodsCategoryBrand, IndexAd
from rest_framework import serializers

from django.db.models import Q

"""
class GoodsSeriliazer(serializers.Serializer):

    name = serializers.CharField(required=True,max_length=100)
    click_number = serializers.IntegerField(default=0)
"""

class CategorySeriliazer3(serializers.ModelSerializer):
    """
    三级分类
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySeriliazer2(serializers.ModelSerializer):
    """
    二级分类
    """
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySeriliazer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySeriliazer(serializers.ModelSerializer):
    """
    一级分类
    """
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySeriliazer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSeriliazer(serializers.ModelSerializer):
    category = CategorySeriliazer()  # 覆盖嵌套category
    class Meta:
        model = Goods
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'


class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySeriliazer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id)
        if ad_goods:
            goods_ins = ad_goods[0].goods
            goods_json = GoodsSeriliazer(goods_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
            category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSeriliazer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = '__all__'

from goods.models import Goods, GoodsCategory
from rest_framework import serializers

# class GoodsSeriliazer(serializers.Serializer):
#
#     name = serializers.CharField(required=True,max_length=100)
#     click_number = serializers.IntegerField(default=0)




class CateGoryseriliazer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSeriliazer(serializers.ModelSerializer):
    category = CateGoryseriliazer()
    class Meta:
        model = Goods
        fields = "__all__"
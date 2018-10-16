from datetime import datetime
from django.db import models

from extra_apps.DjangoUeditor.models import  UEditorField

# Create your models here.

class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名",help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别", help_text="父类目级别", related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类别", null=True, blank=True, related_name="brands")
    name = models.CharField(max_length=30, default="", verbose_name="品牌名")
    desc = models.CharField(max_length=30, default="", verbose_name="品牌描述")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    image = models.ImageField(max_length=200, upload_to="brands/", verbose_name="品牌图片")

    class Meta:
        verbose_name = "品牌名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    click_number = models.IntegerField(default=0, verbose_name="点击数")
    sold_num  = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存量")
    shop_price = models.FloatField(default=0, verbose_name="本店销售价格")
    name = models.CharField(max_length=100, verbose_name="商品名")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    goods_desc = UEditorField(verbose_name="内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default="")
    goods_prief = models.TextField(verbose_name="商品简介")
    ship_free = models.BooleanField(default=False, verbose_name="是否承担运费")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热卖")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    goods_front_image = models.ImageField(upload_to="goods/images", null=True, blank=True, verbose_name="")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
    # image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name =  "轮播的商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
 
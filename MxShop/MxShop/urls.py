"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
# from goods.views_base import goods
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
# from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from goods.views import GoodsListViewSet, CategoryViewset, IndexCategoryViewset

import xadmin

router = DefaultRouter()
# router = SimpleRouter()

router.register(r"goods", GoodsListViewSet, 'goods',)
router.register(r"categorys", CategoryViewset, 'categorys',)
router.register(r"indexgoods", IndexCategoryViewset, 'indexgoods',)
# goods_list = GoodsListViewSet.as_view({
#     "get": "get"
# })


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'docs/', include_docs_urls(title="慕学生鲜")),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 上传文件url
    url(r"", include(router.urls)),
    url(r'api-token-auth/', views.obtain_auth_token)
    # url(r'^goods/$', goods.as_view())
    # url(r'^goods/$', goods_list)
]

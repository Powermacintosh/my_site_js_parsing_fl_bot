from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
router = SimpleRouter()

router.register('api/fl', OrderView)

urlpatterns = [
path('', index, name='index_url'),
path('fl/today/', index_today, name='index_today_url'),
path('fl/<str:slug>/', FlDetail.as_view(), name='fl_detail_url'),
path('fl/<str:slug>/update/', FlUpdate.as_view(), name='fl_update_url'),
path('tags/', tags_list, name='tags_list_url'),
path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]


urlpatterns += router.urls
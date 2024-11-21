from django.urls import path
from .views import (
    CheckListApi,
    CheckListDetailsApi,
    CheckListItemApi,
    CheckListItemDetailApi,
)


urlpatterns = [
    path('api/checklists/', CheckListApi.as_view(), name='checklist'),
    path('api/checklists/<int:pk>/', CheckListDetailsApi.as_view(), name='checklist_details'),


    path('api/checklist-items/', CheckListItemApi.as_view(), name='checklist_item'),
    path('api/checklist-items/<int:pk>/', CheckListItemDetailApi.as_view(), name='checklist_item'),
]

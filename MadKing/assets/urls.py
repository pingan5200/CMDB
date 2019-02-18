from django.urls import path
from . import views


urlpatterns = [
    path('report/asset_with_no_asset_id/', views.asset_with_no_asset_id, name='acquire_asset_id'),
    path('report/', views.asset_report),
    path('new_assets/approval/', views.new_assets_approval, name="new_assets_approval")
]
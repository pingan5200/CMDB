from django.contrib import admin
from assets import models
from django.http import HttpResponseRedirect


# Register your models here.

class BaseAdmin(object):
    """自定义admin类"""
    choice_fields = []
    fk_fields = []
    dynamic_fk = None
    dynamic_list_display = []
    dynamic_choice_fields = []
    m2m_fields = []


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id','asset_type','sn','name','manufactory','management_ip','idc','business_unit','admin','trade_date','status')
    filter_horizontal = ('tags',)


@admin.register(models.NewAssetApprovalZone)
class NewAssetApprovalZoneAdmin(admin.ModelAdmin):
    list_display = ('sn','asset_type','manufactory','model','cpu_model','cpu_count','cpu_core_count','ram_size','os_distribution','os_release','date','approved','approved_by','approved_date')
    list_filter = ('asset_type', 'date')
    search_fields = ('sn',)
    # 添加选项
    actions = ['approve_selected_objects']

    # 选项功能
    def approve_selected_objects(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        print(selected)
        ids = ",".join(selected)
        return HttpResponseRedirect(f'/asset/new_assets/approval/?ids={ids}')

    # 选项描述
    approve_selected_objects.short_description = "批准入库"


# @admin.register(models.EventLog)
# class EventLogAdmin(admin.ModelAdmin):
#     list_display = ('name', 'colored_event_type', 'asset', 'component', 'detail', 'date', 'user')
#     search_fields = ('asset',)
#     list_filter = ('event_type', 'component', 'date', 'user')


admin.site.register(models.UserProfile)
admin.site.register(models.Asset)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IDC)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Manufactory)
admin.site.register(models.Tag)
admin.site.register(models.Software)
admin.site.register(models.RaidAdaptor)
admin.site.register(models.SecurityDevice)
admin.site.register(models.EventLog)



from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from assets import core, models
from assets import utils


# Create your views here.
@csrf_exempt
@utils.token_required
def asset_report(request):
    # print(request.GET)
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            print("----asset data valid:")
            ass_handler.data_inject()
            # return HttpResponse(json.dumps(ass_handler.response))

        return HttpResponse(json.dumps(ass_handler.response))
        # return render(request,'assets/asset_report_test.html',{'response':ass_handler.response})
        # else:
        # return HttpResponse(json.dumps(ass_handler.response))

    return HttpResponse('--test--')


@csrf_exempt
def asset_with_no_asset_id(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        res = ass_handler.get_asset_id_by_sn()

        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        return HttpResponse(json.dumps(res))


def new_assets_approval(request):
    if request.method == 'POST':
        # copy传来的id，用于以后可以修改
        request.POST = request.POST.copy()
        # 获取post传来的数据
        approved_asset_list = request.POST.getlist('approved_asset_list')
        # 从待审批表中读取多条记录
        approved_asset_list = models.NewAssetApprovalZone.objects.filter(id__in=approved_asset_list)

        response_dic = {}
        for obj in approved_asset_list:
            # 修改传来的的数据，把待审批表记录中的data字段数据保存在post里的‘asset_data’中
            request.POST['asset_data'] = obj.data
            # 创建一个Aseet实例，初始化实例，把request数据传进去
            ass_handler = core.Asset(request)
            # 1.待审批表数据创建asset_id，稍后把asset_id存入正式库
            # 2.检查待审批表数据合法，合法的话获取正式库Asset对象记录变为全局对象，返回true
            # 3.待审批表的数据保存为全局
            # 4.检查待审批数据是否为新资产
            # 4.待审批表数据正式入库
            # 5.待审批表批准为true
            # 6.保存待审批表
            if ass_handler.data_is_valid_without_id():
                # 正式入库
                ass_handler.data_inject()
                # 待审批表批准为true
                obj.approved = True
                # 保存待审批表
                obj.save()

            response_dic[obj.id] = ass_handler.response
        return render(request, 'assets/new_assets_approval.html',
                      {'new_assets': approved_asset_list, 'response_dic': response_dic})
    else:
        ids = request.GET.get('ids')
        print(ids)
        ids_list = ids.split(',')
        print(ids_list)
        new_assets = models.NewAssetApprovalZone.objects.filter(id__in=ids_list)
        print('22')
        return render(request, 'assets/new_assets_approval.html', {'new_assets': new_assets})
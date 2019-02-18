CMDB平台开发:
1.服务器资产信息保存到CMDB

2.资产信息变化更新到CMDB

3.信息先保存到服务审批表，审批后才正式入库

4.服务端审批后，客户端下次发送的资产信息不需要审批,直接入库

5.服务端接收资产信息实现api认证


逻辑：

# # # # 第一次 客户把资产信息提交到api保存到待审批表
# # # # NedStark.py   report_asset
# # # # 客户端 发资产信息
# # # # report_asset(客户端收集信息，load_asset_id本地文件没有asset_id,  __submit_data提交收集信息到服务器api)-----1->asset_with_no_asset_id {get_asset_id_by_sn--->mandatory_check获取不到正式库Asset对象(因为没有asset_id)--->save_new_asset_to_approval_zone保存数据到审批区}------2-------->返回客户端this is a new asset,needs IT admin's approval to create the new asset id
# # # # 服务端 审批区批准
new_assets_approval待审批区------------>data_is_valid_without_id待审批表数据创建asset_id { mandatory_check验证字段，获取正式库Asset对象} ---------->data_inject正式入库


-------------------------------------------------------------------------------------------------------------------------------------

# # # # 第二次 客户把资产信息提交到api返回asset_id
# # # # NedStark.py   report_asset
# # # # 客户端 发资产信息
# # # # report_asset(客户端收集信息，load_asset_id本地文件没有asset_id, __submit_data提交收集信息到服务器api)----->asset_with_no_asset_id { get_asset_id_by_sn--->mandatory_check获取正式库Asset对象(因为有asset_id) }-------->返回客户端asset_id---->__update_asset_id客户端在本地创建var/.asset_id保存资产id

----------------------------------------------------------------------------------------------------------------------------------------

第三次 客户把变化的资产信息提交到api到正式库
# # # # NedStark.py   report_asset
# # # # 客户端 发资产信息
# # # # report_asset(客户端收集信息，load_asset_id本地文件有asset_id, __submit_data提交收集信息到服务器api)------>asset_report { data_is_valid--> mandatory_check验证字段，获取正式库Asset对象 } ----->data_inject正式入库----->返回给客户端

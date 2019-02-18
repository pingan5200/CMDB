# CMDB平台开发:
1.服务器资产信息保存到CMDB

2.资产信息变化更新到CMDB

3.信息先保存到服务审批表，审批后才正式入库

4.服务端审批后，客户端下次发送的资产信息不需要审批,直接入库

5.服务端接收资产信息实现api认证

# 逻辑：
#### 第一次 客户把资产信息提交到api保存到待审批表
#### 客户端 发资产信息
#### NedStark.py   report_asset
#### 服务端 审批区批准

#### 第二次 客户把资产信息提交到api返回asset_id
#### 客户端 发资产信息
#### NedStark.py   report_asset
#### 服务端 返回asset_id

#### 第三次 客户把变化的资产信息提交到api到正式库
#### 客户端 发资产信息

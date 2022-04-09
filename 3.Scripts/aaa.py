import f5.bigip
from f5.bigip import ManagementRoot
#连接F5设备
mgmt = f5.bigip.ManagementRoot('10.99.100.40', 'admin', 'Admin@123')
#新建POOL
pool1 = mgmt.tm.ltm.pools.pool.create(name='pool9',monitor = 'tcp',description="This is My Python pool!",partition='Common')
#加载POOL信息
pool_1 = mgmt.tm.ltm.pools.pool.load(partition='Common', name='pool1')

#添加POOL备注
pool_1.description = "This is my pool"
pool_1.update()

#新建POOL1的member
m1 = pool_1.members_s.members.create(partition='Common', name='192.168.101.50:80')
m2 = pool_1.members_s.members.create(partition='Common', name='192.168.101.51:80')

#新建VS
vs5 = mgmt.tm.ltm.virtuals.virtual.create(name='vs5',partition='Common',description = 'This is my pool!',pool = 'pool1',destination = '195.1.1.5:80',ipProtocol = 'tcp',mask = '255.255.255.255',persist= 'cookie',profiles = 'fasthttp')
#profiles = 'fasthttp'时，TYPE为 Performance(HTTP),此时会话保持只能是persist= 'cookie'。
#profiles = 'tcp'时，TYPE为 Standard,此时会话保持不能是persist= 'cookie'。
#profiles = 'fastL4'时，TYPE为 Forwarding,此时会话保持不能是persist= 'cookie'。


#轮询POOL1的名称
pool_collection = mgmt.tm.ltm.pools.get_collection()
pools = mgmt.tm.ltm.pools

for pool in pool_collection:
     print(pool.name)

#修改MEMBER状态
m11 = pool_1.members_s.members.load(partition='Common', name='192.168.101.50:80')
#获取member名称
m11.name
#修改MEMBER状态
m11.modify(session = 'user-enabled')
m11.modify(session = 'user-disabled')
m11.update

#修改VS状态
vs1 = mgmt.tm.ltm.virtuals.virtual.create(name='vs1',partition='Common',pool = 'pool1',destination = '195.1.1.1:80',ipProtocol = 'tcp',mask = '255.255.255.255')
vs_1 = mgmt.tm.ltm.virtuals.virtual.load(name = 'vs1')
#启用状态
vs_1.modify(enabled = 'Ture') 
#禁用状态
vs_1.modify(disabled = 'Ture') 

#删除VS
vs5pro = mgmt.tm.ltm.virtuals.virtual.load(name = 'vs5')
vs5pro.update



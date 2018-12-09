import requests
import time
# url="http://v.juhe.cn/calendar/day?date=2015-1-1&key=3fc2053b46fcafdaacd98165f31706d4"
# r=requests.get(url)
# print(r)

#
#
# url="http://47.92.88.246:8087/x_springboot/sys/login"
# data={"username":"niuyuting","password":"111111"}
# r=requests.post(url=url,data=data)
# r=requests.post(url=url,json=data)
# print(r)

# # 登录
# url="http://47.92.88.246:8087/x_springboot/sys/login"
# data={"username":"niuyuting","password":"111111"}
# r=requests.post(url=url,json=data)
# headers={"content-type":"application/json"}
# print(r.json()["token"])
#
# #退出
# token=r.json()["token"]
# headers={"token":token}
#
# url="http://47.92.88.246:8087/x_springboot/sys/logout"
# r=requests.post(url,headers=headers)
# print(r.json())

# url="http://47.92.88.246:8087/x_springboot/sys/login"
# data={"username":"niuyuting","password":"111111"}
# r=requests.post(url=url,json=data)
# headers={"content-type":"application/json"}
# print(r.json()["token"])
#
# # 增加
# token=r.json()["token"]
# headers={"token":token}
# url="http://47.92.88.246:8087/x_springboot/sys/user/save"
# data={"status":1,"roleIdList":[],"username":"增加+str(time.time())","password":"111111","email":"eee@qq.com","mobile":"12321232123"}
# r=requests.post(url=url,json=data,headers=headers)
# print(r.json())
#
# #查询
# url="http://47.92.88.246:8087/x_springboot/sys/user/list"
# # ?_search=false&nd=1541321402466&limit=10&page=1&sidx=&order=asc&username=&_=1541321327662"
# data={
#     "limit":"10",
#     "page":"1",
#     "order":"asc"
# }
# r=requests.get(url=url,params=data,headers=headers)
# # print(r.text)
# # print("page"+str(r.json()["page"]))
# # print(r.json()["page"]["list"][0]["userId"]
# userID=r.json()["page"]["list"][0]["userId"]
#
# #删除
# url="http://47.92.88.246:8087/x_springboot/sys/user/delete"
# headers={"token":token}
# # list类型
# data=[userID]
# r=requests.post(url=url,json=data,headers=headers)
# print(r.json())
#
# #修改用户
# import time
# url="http://47.92.88.246:8087/x_springboot/sys/user/update"
# data={"userId":userID,"username":"修改"+str(time.time),"password":"111111","salt":None,"email":"1111doudou@qq.com","mobile":"15847584785","status":1,"roleIdList":[],"createUserId":36,"createTime":"2018-11-04 17:20:00"}
# headers={"token":token}
# r=requests.post(url=url,json=data,headers=headers)
# print(r.json())


url="http://47.92.88.246:8087/x_springboot/sys/login"
data={"username":"niuyuting","password":"111111"}
r=requests.post(url=url,json=data)
print(r.json())
token=r.json()["token"]
print(token)
# 角色的增加
url="http://47.92.88.246:8087/x_springboot/sys/role/save"
data={"roleName":"增加"+str(time.time()),"menuIdList":[1, 2, 15]}
headers={"token":token}
r=requests.post(url=url,json=data,headers=headers)
print(r.json())

# 角色的删除
url=""
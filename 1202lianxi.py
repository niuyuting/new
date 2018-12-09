import unittest
import requests
import time
class LoginTest(unittest.TestCase):
    def setUp(self):
        # 测试我们的登录
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "niuyuting", "password": "111111"}
        self.headers={"Content-Type": "application/json"}
        r = requests.post(url=url, json=data)
        self.token=r.json()["token"]
    #测试异常添加用户
        self.addUserUrl="http://47.92.88.246:8087/x_springboot/sys/user/save"
    def testUserAdd1(self):
        # 测试用户添加

        data={"status":1,"roleIdList":[],"username":"用户"+str(time.time()),"password":"111111","email":"test@test.com"}
        self.headers.update({"token":self.token})
        r=requests.post(url=self.addUserUrl,json=data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()["msg"],"success",msg="新增成功")
    # def testUserAdd2(self):
    #     data={"status": 1,"roleIdList": [], "username": "用户" + str(time.time()), "password": "","email": "test@test.com"}
    #     r = requests.post(url=self.addUserUrl, json=data, headers=self.headers)
    #     print(r.json())
    #     self.assertEqual(r.json()["msg"],"", msg="新增失败")
        url="http://47.92.88.246:8087/x_springboot/sys/user/list"
        data={"limit":"10","page":"1","order":"asc"}
        r=requests.get(url=url,params=data,headers=self.headers)
        print(r.text)
        print("page"+str(r.json()["page"]))
        print(r.json()["page"]["list"][0]["userId"])
        userID=r.json()["page"]["list"][0]["userId"]



    def tearDown(self):
        # userID = r.json()["page"]["list"][0]["userId"]
        deleteurl="http://47.92.88.246:8087/x_springboot/sys/user/delete"
        data=[userId]
        r=requests.post(url=deleteurl,json=data,headers=self.headers)
        print(r.json())


if __name__ == '__main__':
    unittest.main()

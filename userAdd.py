# # import unittest
# # class DeamTest(unittest.TestCase):
#
# #     def setUp(self):
# #         print ("setup"+"1")
# #     def test01(self):
# #         print("test01"+"2")
# #     def tearDown(self):
# #         print("tearDown"+"3")
# #
# # if __name__ == '__main__':
# #
# #     unittest.main()
#
#
# import unittest
# import requests
# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         self.url="http://47.92.88.246:8087/x_springboot/sys/login"
#         self.headers={"Content-Type":"application/json"}
#     def testLogin01(self):
#         # url="http://47.92.88.246:8087/x_springboot/sys/login"
#         data={"username":"niuyuting","password":"111111"}
#         # headers={"Content-Type":"application/json"}
#         r=requests.post(url=self.url,json=data,headers=self.headers)
#         print(r.json())
#         self.assertEqual(r.json()["msg"],"success",msg="登录成功")
#     def testLogin02(self):
#         # url="http://47.92.88.246:8087/x_springboot/sys/login"
#         data={"username":"niuyuting","password":""}
#         # headers={"Content-Type":"application/json"}
#         ra=requests.post(url=self.url,json=data,headers=self.headers)
#         print(ra.json())
#         self.assertEqual(ra.json()["msg"],"账号或密码不正确",msg="登录异常")
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
import requests
import time
class LoginTest(unittest.TestCase):
    def setUp(self):
        pass
    def testUserAdd1(self):
        url="http://47.92.88.246:8087/x_springboot/sys/login"
        headers={"Content-Type":"application/json"}
        data={"username":"niuyuting","password":"111111"}
        r=requests.post(url=url,json=data,headers=headers)
        token=r.json(["token"])

        userAddurl="http://47.92.88.246:8087/x_springboot/sys/user/save"
        data={"status":1,"roleIdList":[],"username":"用户"+str(time.time()),"password":"111111","email":"test@test.com"}
        headers.update({"token":token})
        print(str(headers)+"---------------")
        r=requests.post(url=userAddurl,json=data,headers=headers)
        print(r.json())
        # self.assertEqual(r.json()["msg"],"success",msg="新增成功")

        userAddurl2="http://47.92.88.246:8087/x_springboot/sys/user/save"
        data={"status":1,"roleIdList":[],"username":"用户"+ str(time.time()),"password":"111111","email": "test@test.com"}
        headers.update({"token":token})
        print(str(headers)+"---------------")
        r=requests.post(url=userAddurl2,json=data,headers=headers)
        print(r.json())
        # self.assertEqual(r.json()["msg"],"success",msg="新增成功")
if __name__ == '__main__':
    unittest.main()

    # # 创建一个测试套件
    # suite =  = unittest.TestSuite()
    # # ()
    # # 将测试用例加载到测试套件中
    # 件中c
    # suite.addTest(use(st(userTest02.userAderAddTest('testUserAdd1'))
    #                   ))
    # suite.addTest(use(st(userTest02.userAderAddTest('testUserAdd2'))
    # # 定义一个TextTestRunner
    # # runner =  = unittest.TextTestRunneunner()
    # #运行测试用例
    #
    # runner.run(sui(suite)
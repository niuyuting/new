import unittest
from userAdd import LoginTest
#from 脚本 import 类
import HTMLTestRunner

if __name__ == '__main__':
    #实例化一个testsuite测试套件--告诉他运行哪一个用例
    suite=unittest.TestSuite()
    suite.addTest(LoginTest('testUserAdd1'))
    #suite.addTest(类（具体哪一个用例 ）)
    # suite.addTest(userAddTest02('testuserAdd2'))
    print(suite)
    file=open('123.html','wb')
#HTMLTestRunner
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,title="第一个报告")
    runner.run(suite)
    # 我就想看看成功了吗


import  unittest
from src import stu_exam_sys

def createsuite():
    suite = unittest.TestSuite()
    #将测试用例加入到测试容器（套件）中
    suite.addTest(stu_exam_sys.stu_exam_sys("test_login"))
    suite.addTest(stu_exam_sys.stu_exam_sys("test_update"))
    return suite

if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
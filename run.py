# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 12:32:58
# @Author  : lileilei 
from testcase.testbokeyuan import BokeyuanTest
from util import BSTestRunner
import os,unittest,time
if __name__ == '__main__':
    suite = unittest.TestSuite()
    now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'testresult')
    file=os.path.join(file_dir,(now+'.html'))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BokeyuanTest))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='demo by macaca', description='测试结果')
    runner.run(suite)
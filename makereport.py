# 借助模板生成测试报告
import unittest
# 导入时间包
import time
# 导入报告生成模板包
from Tools.HTMLTestRunner import HTMLTestRunner  # 原版模板(英文)
from Tools.HTMLTestReportCN import HTMLTestRunner  # 二改模板(中文)

if __name__ == '__main__':
    # 组装测试用例
    cases_dir = './Cases/'
    discover = unittest.defaultTestLoader.discover(cases_dir, pattern='iWebShop*.py')
    # 报告存放路径
    report_dir = './Reports/'
    # 获取当前时间
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 准备报告名称
    report_name = report_dir + now_time + 'Report.html'
    # 开始报告写入文件流
    with open(report_name, 'wb') as f:
        # 初始化报告生成的执行对象
        '''
        stream=:开启的报告文件写入流
        verbosity=:测试执行后的打印格式(默认值为1,可选2,2显示的信息更详细,推荐使用!)
        title=:生成的报告内的标题(可选)
        description=:测试相关环境描述信息(可选)
        '''
        # 英文模板调用
        # runner = HTMLTestRunner(stream=f, verbosity=1, title='iWebShop登录逻辑测试报告',
        #                         description='测试平台:macOS 测试浏览器:Firefox 版本:v35.0.1 测试人:QA')

        # 中文模板调用
        runner = HTMLTestRunner(stream=f, verbosity=2, title='iWebShop登录逻辑测试报告',
                                description='测试平台:macOS 测试浏览器:Firefox 版本:v35.0.1', tester='test03QA')
        # 调用run()方法执行测试套件discover
        runner.run(discover)

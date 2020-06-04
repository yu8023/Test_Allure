import pytest
import allure

class Test_allure:

    @allure.step(title="第一步")           # 测试步骤: 第一步
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)    # 标注严重级别： 严重的
    def test_all(self):
        allure.attach("描述","我是第一步的描述~~~")   # 描述：描述的内容
        assert 1

    @allure.issue('http://www.163.com')         # 缺陷
    @pytest.allure.testcase('http://www.baidu.com')   # 链接
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)    # 标注严重级别： 不重要的
    def test_al(self):
        allure.attach("描述","我是第一步的描述~~~")   # 描述：描述的内容
        assert 0


if __name__ == '__main__':
    pytest.main(["-s","--alluredir","report","test_001.py"])
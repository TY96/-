import allure
from Common import Assert,Request,read_excel
import pytest
    #在Request的模块里调用request方法
request = Request.Request()

assertions = Assert.Assertions()
    #找到xlsx,在read_excel里面找到含有xlsx的变量名,在本模块下再将变量重命名

excel_list = read_excel.read_excel_list('./document/test.xlsx')
    #设置一个空list
ids_list = []

for i in range(len(excel_list)):
    # i从零开始循环,将xlsx里面每一行的最后一个删除并留在ids_pop里面
    ids_pop = excel_list[i].pop()
    # 将删除的追加在ids_list内
    ids_list.append(ids_pop)

#     加装饰
@allure.feature('登录模块')
class Test_login:
    @allure.story('登录参数化')
    # 将参数化的内容加入括号内
    @pytest.mark.parametrize('name,pwd,msg',excel_list,ids=ids_list)

    def test_login(self,name,pwd,msg):
        # login_resp = request.post_request('url=http://192.168.60.132:8080/admin/login',
        #                                   json={"username": "admin", "password": "123456"})
        login_resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                          json={"username": name, "password": pwd})
        assertions.assert_code(login_resp.status_code,200)

        print(login_resp)
        print(type(login_resp))

        login_resp_json = login_resp.json()

        assertions.assert_in_text(login_resp_json['message'],msg)

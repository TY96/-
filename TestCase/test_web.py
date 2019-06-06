import allure,pytest
from Common import Assert,Request,read_excel,Tools

assertions = Assert.Assertions()
request = Request.Request()
A = []
excel_list = read_excel.read_excel_list('../document/用户注册测试用例.xlsx')
for i in range(len(excel_list)):
    i__pop = excel_list[i].pop()
    A.append(i__pop)

@allure.feature('注册模块测试')
class Test_zc:
    # @pytest.mark.parametrize('phone,pwd,rePwd,userName,resp',excel_list,ids=A)
    @allure.story('注册模块')
    @pytest.mark.zc
    def test_NUMB(self):
        zc_resp = request.post_request(url='http://192.168.60.132:1811/user/signup',
                                            json={"phone": Tools.phone_num(), "pwd": 'ab12345', "rePwd": 'ab12345',
                                                  "userName": Tools.random_str_abc(3)+Tools.random_123(3)})
        assertions.assert_code(zc_resp.status_code,200)
        zc_resp_json = zc_resp.json()

        assertions.assert_in_text(zc_resp_json["respCode"],'0')


    @allure.story('注册失败')
    @pytest.mark.parametrize('phone,pwd,rePwd,userName,resp', excel_list, ids=A)
    @pytest.mark.zc
    def test_fault(self,phone,pwd,rePwd,userName,resp):
        zc_respo=request.post_request(url='http://192.168.60.132:1811/user/signup',
                                            json={"phone": phone, "pwd": pwd, "rePwd": rePwd,
                                                  "userName": userName})
        assertions.assert_code(zc_respo.status_code,200)
        zc_respo_json = zc_respo.json()
        assertions.assert_in_text(zc_respo_json['respCode'],'9')

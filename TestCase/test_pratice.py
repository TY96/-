import allure,pytest
from Common import Assert,Request,read_excel
url = 'http://192.168.60.132:1811/'
assertions = Assert.Assertions()
request = Request.Request()
# excel_list = read_excel.read_excel_list('../document/登录测试用例.xlsx')
# A = []
# for i in range(len(excel_list)):
#     list_pop = excel_list[i].pop()
#     A.append(list_pop)


@allure.feature('注册_修改密码_登录模块')
class   Test_sign_in():

    @allure.story('注册')
    @pytest.mark.ALL
    def test_register(self):
        reginster_spon = request.post_request(url=url + 'user/signup',
                                            json={"phone": "13215452546", "pwd": "a12345", "rePwd": "a12345",
                                                  "userName": "a666666"})
        assertions.assert_code(reginster_spon.status_code, 200)
        reginster_spon_json = reginster_spon.json()
        assertions.assert_in_text(reginster_spon_json['respCode'],'0')

    @allure.story('修改密码')
    @pytest.mark.ALL
    def test_change_password(self):
        change_resp = request.post_request(url=url + 'user/changepwd',
                                           json={"newPwd": "a123456", "oldPwd": "a12345", "reNewPwd": "a123456",
                                                 "userName": "a666666"})
        assertions.assert_code(change_resp.status_code, 200)
        change_resp_json = change_resp.json()
        assertions.assert_in_text(change_resp_json['respCode'], '0')


    @allure.story('登录')
    @pytest.mark.ALL
    # @pytest.mark.parametrize('pwd,userName,code',excel_list,ids=A)
    # def test_sign(self,pwd,userName,code):
    def test_sign(self):
        # sign_resp = request.post_request(url=url + 'user/login', json={"pwd": pwd, "userName": userName})
        sign_resp = request.post_request(url=url + 'user/login', json={"pwd": 'a123456', "userName": 'a666666'})
        assertions.assert_code(sign_resp.status_code,200)
        sign_resp_json = sign_resp.json()
        # assertions.assert_in_text(sign_resp_json['respCode'],code)
        assertions.assert_in_text(sign_resp_json['respCode'], '0')






















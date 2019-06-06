import allure
import pytest

from Common import Assert,Request,Login,read_excel
url = Login.url
head = Login.Login().get_token()
assertions = Assert.Assertions()
request = Request.Request()
A = 0
b = []
goods = read_excel.read_excel_list('./document/退货.xlsx')
for i in range(len(goods)):
    list_i__pop = goods[i].pop()
    b.append(list_i__pop)

@allure.feature('退货窗口')
class Test_return:
    @allure.story('查询退货')
    def test_sel_goods(self):
        sel_resp = request.get_request(url=url + 'returnReason/list', params={'pageNum': 1, 'pageSize': 5},headers=head)
        assertions.assert_code(sel_resp.status_code,200)
        sel_resp_json = sel_resp.json()
        assertions.assert_in_text(sel_resp_json['message'],'成功')
        data_ = sel_resp_json['data']
        list_ = data_['list']
        one = list_[0]
        global A
        A = one['id']
    @allure.story('删除退货')
    def test_del_goods(self):
        del_resp = request.post_request(url=url + 'returnReason/delete', params={'ids': A}, headers=head)
        assertions.assert_code(del_resp.status_code, 200)
        del_resp_json = del_resp.json()
        assertions.assert_in_text(del_resp_json['message'], '成功')

    @allure.story('添加退货')
    @pytest.mark.parametrize('name,sort,status,msg',goods,ids=b)
    def test_add_goods(self,name,sort,status,msg):
        add_return = request.post_request(url=url + 'returnReason/create',
                                            json={"name": name, "sort": sort, "status": status, "createTime": ''},
                                            headers=head)
        assertions.assert_code(add_return.status_code,200)
        add_return_json = add_return.json()
        assertions.assert_in_text(add_return_json['message'],msg)


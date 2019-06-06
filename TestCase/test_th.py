import allure,pytest
from Common import Request, Assert, read_excel,Login

request = Request.Request()
assertions = Assert.Assertions()

url = Login.url
head = Login.Login().get_token()
yhq_id = 0
excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
ids_list = []
for i in range(len(excel_list)):
    # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
    ids_pop = excel_list[i].pop()
    # 将ids_pop添加到 ids_list 里面
    ids_list.append(ids_pop)
@allure.feature('退货窗口')
@pytest.mark.th
class Test_th:
    @allure.story('查询退货')
    def test_sel(self):

        sel_resp = request.get_request(url=url+'returnReason/list', params={'pageNum': 1, 'pageSize': 5},headers=head)
        assertions.assert_code(sel_resp.status_code,200)
        sel_resp_json = sel_resp.json()
        assertions.assert_in_text(sel_resp_json['message'],'成功')
        data_ = sel_resp_json['data']
        list_ = data_['list']
        ASD = list_[0]
        global A
        A=ASD['id']

    # @allure.story('删除退货')
    # def test_del_goods(self):
    #     del_resp = request.post_request(url=url + 'returnReason/delete', params={'ids': A}, headers=head)
    #     assertions.assert_code(del_resp.status_code, 200)
    #     del_resp_json = del_resp.json()
    #     assertions.assert_in_text(del_resp_json['message'], '成功')
    #
    # @allure.story('添加退货')
    # @pytest.mark.parametrize('name,sort,status,msg',goods,ids=b)
    # def test_add_goods(self,name,sort,status,msg):
    #     add_return = request.post_request(url=url + 'returnReason/create',
    #                                         json={"name": name, "sort": sort, "status": status, "createTime": ''},
    #                                         headers=head)
    #     assertions.assert_code(add_return.status_code,200)
    #     add_return_json = add_return.json()
    #     assertions.assert_in_text(add_return_json['message'],msg)

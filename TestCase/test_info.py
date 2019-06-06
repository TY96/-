import allure
from Common import Assert,Request,read_excel
import pytest
F = 0
excel_list = read_excel.read_excel_list('./document/商品分类参数化.xlsx')
a = []
for i in range(len(excel_list)):
    list_i__pop = excel_list[i].pop()
    a.append(list_i__pop)

coupon_list = read_excel.read_excel_list('./document/优惠券.xlsx')
B = []
for i in range(len(coupon_list)):
    data_Coupon = coupon_list[i].pop()
    B.append(data_Coupon)

request = Request.Request()

assertions = Assert.Assertions()
head = {}
ids = 0


@allure.feature('获取用户信息')
class Test_info:

    @allure.story('登录接口')
    def test_login(self):
        login_resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                          json={"username":"admin", "password":"123456"})
        assertions.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()

        assertions.assert_in_text(login_resp_json['message'],'成功')
        # 获取data,为后面提取token做准备
        data_json = login_resp_json['data']

        token = data_json['tokenHead'] + data_json['token']
        global head
        head = {'Authorization':token}



    @allure.story('用户信息接口')
    def test_info(self):
        info_resp = request.get_request(url='http://192.168.60.132:8080/admin/info', headers=head)
        assertions.assert_code(info_resp.status_code,200)
        info_resp_json= info_resp.json()
        assertions.assert_code(info_resp_json['message'],'操作成功')




    @allure.story('获取商品列表')
    def test_sku(self):
        sku_resp = request.get_request(url='http://192.168.60.132:8080/product/list',
                                          params={'pageNum': 1, 'pageSize': 5}, headers=head)
        assertions.assert_code(sku_resp.status_code,200)
        sku_resp_json = sku_resp.json()
        assertions.assert_in_text(sku_resp_json['message'],'成功')

        global ids
        sku_data = sku_resp_json['data']
        sku_list = sku_data['list']
        sku_list_id_ = sku_list[0]
        sku_list_id_ = ids
    @allure.story('添加商品分类')



    def test_add(self):


        add_resp = request.post_request(url='http://192.168.60.132:8080/productCategory/create',
                                        json={"description": "", "icon": "", "keywords": "", "name":'', "navStatus": 0,
                                         "parentId": 0, "productUnit": "", "showStatus": 0, "sort": 0,
                                         "productAttributeIdList": []},headers=head)
        assertions.assert_code(add_resp.status_code,200)
        add_resp_json = add_resp.json()
        assertions.assert_in_text(add_resp_json['message'],'成功')

    @allure.story('删除商品分类')
    def test_del(self):
        del_resp = request.get_request(url='http://192.168.60.132:8080/productCategory/delete/'+str(ids),headers=head)
        assertions.assert_code(del_resp.status_code,405)
        del_resp_json = del_resp.json()
        assertions.assert_in_text(del_resp_json['message'],'失败')





    @allure.story('添加商品分类参数化')
    @pytest.mark.parametrize('describe,keywords,name,msg', excel_list, ids=a)
    def test_add(self,describe,keywords,name,msg):


        add_resp = request.post_request(url='http://192.168.60.132:8080/productCategory/create',
                                        json={"description":describe, "icon": "", "keywords":keywords, "name":name, "navStatus": 0,
                                         "parentId": 0, "productUnit": "", "showStatus": 0, "sort": 0,
                                         "productAttributeIdList": []},headers=head)
        assertions.assert_code(add_resp.status_code,200)
        add_resp_json = add_resp.json()
        assertions.assert_in_text(add_resp_json['message'],msg)



    @allure.story('优惠券参数化')
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',coupon_list,ids=B)
    def test_coupon(self,name,amount,minPoint,publishCount,msg):

        coupon_resp = request.post_request(url='http://192.168.60.132:8080/coupon/create',
                                            json={"type": 0, "name": name, "platform": 0, "amount": amount,
                                                  "perLimit": 1, "minPoint": minPoint, "startTime": "",
                                                  "endTime": "", "useType": "", "note": "",
                                                  "publishCount": publishCount, "productRelationList": [],
                                                  "productCategoryRelationList": []})
        assertions.assert_code(coupon_resp.status_code,200)
        coupon_resp_json = coupon_resp.json()
        assertions.assert_in_text(coupon_resp_json['message'],msg)



    @allure.story('查询优惠券')
    def test_coupon_sel(self):
        coupon_sel = request.get_request(url='http://192.168.60.132:8080/coupon/list',
                                          params={'pageNum': 1, 'pageSize': 10, }, headers=head)
        assertions.assert_code(coupon_sel.status_code,200)
        coupon_sel_json = coupon_sel.json()
        assertions.assert_in_text(coupon_sel_json['code'],'200')
        sel_json_data_ = coupon_sel_json['data']
        json_data__list_ = sel_json_data_['list']
        WE = json_data__list_[0]
        global F
        F = WE['id']


    @allure.story('删除商品')
    def test_del(self):
        del_resp = request.post_request(url='http://192.168.60.132:8080/coupon/delete/' + str(F))

        assertions.assert_code(del_resp.status_code,200)
        del_resp_json = del_resp.json()
        assertions.assert_in_text(del_resp_json['message'],'成功')


























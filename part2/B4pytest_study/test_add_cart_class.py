
from requests_study.mtxshop_apis import login_buyer, add_cart


class TestAddCart:

    def test_add_cart(self):
        login_buyer()
        resp = add_cart()
        # 断言状态码
        assert resp.status_code == 200
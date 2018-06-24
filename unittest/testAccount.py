import unittest,requests,time


class MyTestCase(unittest.TestCase):
    def test_register(self):
        api="http://127.0.0.1:8000/api/account/register"
        postdata={
            "account_id":"3150102098",
            "account_pw":"123456789",
            ""
            "accout_type":0
        }
        response=requests.post(url=api,data=postdata)
        print(response.text)
        self.assertEqual(response.text,'''{"success": 1, "reason": null}''')

    # def test_login(self):
    #
    #     api="http://127.0.0.1:8000/api/account/login/"
    #     postdata={
    #         "account_id":"3150102098",
    #         "account_pw":"123456789",
    #
    #     }
    #     res=requests.post(url=api,data=postdata)
    #     print(res.text)
    #     self.assertEqual(res.text,'''{"success": 1, "type": 0, "reason": null}''')
    # def test_account_repassword(self):
    #     api="http://127.0.0.1:8000/api/account/repassword/"
    #     postdata={
    #         "account_id":"3150102098",
    #         "account_pw":"12345678",
    #
    #     }
    #     res=requests.post(url=api,data=postdata)
    #
    #     self.assertEqual(res.text,'''{"success": 1, "reason": null}''')




if __name__ == '__main__':
    unittest.main()

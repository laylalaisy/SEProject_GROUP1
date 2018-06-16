import unittest,requests


class MyTestCase(unittest.TestCase):
    def test_something(self):
        url="http://127.0.0.1:8000/api/account/login/"
        response=requests.post(url,data={"account_id":"111","account_pw":"222"})
        print(response)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

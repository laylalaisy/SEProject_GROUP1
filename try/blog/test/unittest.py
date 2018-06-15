import requests
import unittest

dir(unittest)


class TestBasic(unittest.TestCase):
    def testHome(self):
        api = 'http://127.0.0.1:8000/'
        requests.post(url=api, data={})
        response = requests.post(url=api, data={})
        self.assertEqual(response.text, '{}')

    def testLogin(self):
        api = 'http://127.0.0.1:8000/login.html'
        requests.post(url=api, data={'account_id': '3150105000', 'password': '3150105000'})
        response = requests.post(url=api, data={'account_id': '3150105000', 'password': '3150105000'})
        self.assertEqual(response.text, '{"account_id": "3150105000"}')

    def testPerson(self):
        api = 'http://127.0.0.1:8000/personinfo.html'
        requests.post(url=api, data={'st_id': '3150105000', 'st_nick': 'gtx', 'st_email': '123'})
        response = requests.post(url=api, data={'st_id': '3150105000', 'st_nick': 'gtx', 'st_email': '123'})
        self.assertEqual(response.text, '{"st_id": "3150105000", "st_nick": "gtx", "st_email": "123"}')

    def testExam(self):
        api = 'http://127.0.0.1:8000/exam.html'
        requests.get(url=api, data={'account_id': '3150105000'})
        response = requests.get(url=api, data={'account_id': '3150105000'})
        self.assertEqual(response.text, '{"account_id": "3150105000", "courses": [{'
                                        '"student_id": "3150105000", '
                                        '"takeup_id": 9, '
                                        '"position": 100'
                                        '"date": "2018/7/8"'
                                        '}]}')

    def testGrade(self):
        api = 'http://127.0.0.1:8000/grade.html'
        requests.get(url=api, data={'account_id': '3150105000'})
        response = requests.get(url=api, data={'account_id': '3150105000'})
        self.assertEqual(response.text, '{"account_id": "3150105000", "courses": [{'
                                        '"course_id": 3, '
                                        '"student_id": "3150105000", '
                                        '"grade": null'
                                        '"status": 0'
                                        '},{'
                                        '"course_id": 2, '
                                        '"student_id": "3150105000", '
                                        '"grade": 60'
                                        '"status": 1'
                                        '}]}')

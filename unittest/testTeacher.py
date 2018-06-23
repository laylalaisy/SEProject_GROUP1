import requests


def testTeacherInfoget():
    api="http://127.0.0.1:8000/api/teacher/info"
    post={
        "account_id":"000123"
    }
    response=requests.get(url=api,params=post)
    print(response.text)


    pass

def testTeacherInfoPost():
    api="http://127.0.0.1:8000/api/teacher/info"
    post={
        "account_id": "000123",
        "account_email":"fuckyou@163.com",
        "teacher_office":"启真湖底1"
    }
    response=requests.post(url=api,data=post)
    print(response.text)

    pass

def testTeacherCourseGet():
    api = "http://127.0.0.1:8000/api/teacher/course"
    post = {
        "account_id": "000123",
    }
    response = requests.get(url=api, params=post)
    print(response.text)


if __name__=="__main__":
    testTeacherCourseGet()
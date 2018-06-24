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



def testTeacherAddCourse():
    api = "http://127.0.0.1:8000/api/teacher/addcourse"
    post = {
        "id":"00010003",
        "name":"c程序设计",
        "credit":"2.5",
        "hour":"2",
        "intro":"很难得课程"
    }
    response = requests.post(url=api, data=post)
    print(response.text)

def testTeacherChange():
    api = "http://127.0.0.1:8000/api/teacher/chgcourse"
    post = {
        "account_id":"000123",
        "id":"1",
        "intro":"info changed"
    }
    response = requests.post(url=api, data=post)
    print(response.text)


def testImg():
    api = "http://127.0.0.1:8000/api/account/img"
    post = {
        "account_id": "000123",
    }
    files={
        "file":open("favicon.jpg","rb")
    }

    response = requests.post(url=api, data=post,files=files)
    print(response.text)

if __name__=="__main__":
    testTeacherChange()
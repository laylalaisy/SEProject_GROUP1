import requests

def testWaitCourseList():
    api="http://127.0.0.1:8000/api/admin/coursewaitlist"
    response=requests.get(url=api)
    print(response.text)

def testAgreeCourse():
    api="http://127.0.0.1:8000/api/admin/agreecourse"
    postdata={
        "teacherid":"000456",
        "courseid":"00010000"
    }
    response=requests.post(url=api,data=postdata)
    print(response.text)


def testStudentInfoUpdate():
    api="http://127.0.0.1:8000/api/admin/student/info"
    postdata={
        "account_id":"3150105000",
        "name":"胖次",
        "dorm":"启真湖底111"
    }
    response=requests.post(url=api,data=postdata)
    print(response.text)

def testTeacherInfoUpdate():
    api = "http://127.0.0.1:8000/api/admin/teacher/info"
    postdata = {
        "account_id": "000123",
        "name": "胖次1",
        "title": "教授",
        "office":"410",
        "management":"软件工程"
    }
    response = requests.post(url=api, data=postdata)
    print(response.text)

if __name__=="__main__":
    testTeacherInfoUpdate()
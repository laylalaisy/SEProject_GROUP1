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


if __name__=="__main__":
    testWaitCourseList()
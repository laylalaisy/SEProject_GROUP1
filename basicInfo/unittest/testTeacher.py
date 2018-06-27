import requests


def testOpenCourse():
    api="http://127.0.0.1:8000/api/teacher/opencourse"
    postdata={
        "account_id":"000456",
        "id":"00010001",
        "capacity":50

    }
    response=requests.post(url=api,data=postdata)
    print(response.text)

if __name__=="__main__":
    testOpenCourse()
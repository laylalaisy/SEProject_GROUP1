import requests


def testTeacherInfoPost():
    api="http://127.0.0.1:8000/api/teacher/info"
    post={
        "account_id":"000123"
    }
    response=requests.get(url=api,params=post)
    print(response.text)


    pass


if __name__=="__main__":
    testTeacherInfoPost()
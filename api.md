### API文档

#### Account API

##### POST /api/account/login

账户登录

```doc
@param
	account_id(string):要查询的用户名
	account_pw(string):要查询的密码
@return
	json object{
		success(bool):登录成功与否
		type(int):该账户的类型（学生、老师、管理员）
		reason(string):不成功的原因
	}
```



##### POST /api/account/register

账户注册

```doc
@param
	account_id(string):新建的用户名
	account_pw(string):新建的密码
	accout_type(int):注册账户的类型（学生、老师、管理员）
@return
	json object{
		success(bool):注册成功与否
		reason(string):不成功的原因
	}
```



##### POST /api/account/repassword

账户密码修改

```doc
@param
	account_id(string):当前的用户名
	account_pw(string):新建的密码
@return
	json object{
		success(bool):修改成功与否
		reason(string):不成功的原因
	}
```

##### POST /api/account/person
账户信息修改
```doc
@param
	account_id(string):当前的用户名
	name(string):真实姓名
    nick(string):昵称
    email(string):电子邮箱
    exp(int):个人经验
    coin(int):金币数
    //...(还有什么别的个人信息随便加)
@return
	json object{
		success(bool):是否修改成功，
		reason(string):原因
	}
```


##### GET /api/account/person

账户信息查询

```doc
@param
	account_id(string):当前的用户名
@return
	json object{
		name(string):真实姓名
		nick(string):昵称
		email(string):电子邮箱
		exp(int):个人经验
		coin(int):金币数
		//...(还有什么别的个人信息随便加)
	}
```



#### Student API

##### GET /api/student/classes

学生当前课程查询

```doc
@param
	account_id(string):当前的用户名
	semister(string):查询学期
@return
	(array) json object{
		name(string):课程名称
		credit(real):课程学分
		teacher(string):教师姓名
		time(time):上课时间
		room(string):上课教室
	}
```



##### GET /api/student/exam

学生当前考试查询

```doc
@param
	account_id(string):当前的用户名
@return
	(array) json object{
		name(string):课程名称
		time(time):考试时间
		room(string):考试教室
		seat(int):考试座位
	}
```



##### GET /api/student/grade

学生当前成绩查询

```doc
@param
	account_id(string):当前的用户名
@return
	(array) json object{
		name(string):课程名称
		credit(real):课程学分
		grade(int):课程成绩
	}
```



##### GET /api/student/course

课程详细信息查询

```doc
@param
	course_id(string):查询课程号
@return
	json object{
		name(string):课程名称
		credit(real):课程学分
		intro(int):课程介绍
		//...(还有什么别的课程信息随便加)
	}
```



#### Teacher API

##### GET /api/teacher/course

讲授课程查询

```doc
@param
	account_id(string):当前的用户名
@return
	(array) json object{
		name(string):课程名称
		credit(real):课程学分
		time(time):上课时间
		room(string):上课教室
	}
```



##### POST /api/teacher/addcourse

申请新增课程

```doc
@param
	name(string):课程名称
	credit(real):课程学分
	intro(string):课程介绍
	type(int):课程类型
@return
	json object{
		success(bool):申请成功与否
		reason(string):不成功的原因
	}
```



##### POST /api/teacher/chgcourse

申请修改课程

```doc
@param
	id(string):课程代号
	name(string):课程名称
	credit(real):课程学分
	intro(string):课程介绍
	type(int):课程类型
@return
	json object{
		success(bool):申请成功与否
		reason(string):不成功的原因
	}
```



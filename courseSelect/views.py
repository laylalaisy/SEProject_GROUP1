from django.shortcuts import render, redirect
from basicInfo.models import course, student, major, discipline, takeup, teacher, college, belong
from .models import selection, teach, creditNeed, curriculum, selectControl, requiredCourse
from .utils import search, getDisciplineByStudent, timestampToDatetime
from django.http import JsonResponse, HttpResponse
import django.utils.timezone as timezone
import xlsxwriter
import io
# Create your views here.

def courses(request):
    courses = course.objects.all()
    if request.POST:
        courses = search(request.POST, courses)
    return render(request, 'courseSelect/courses.html', {'courses':courses})

def course_select(request):
    student = student.objects.get(student_id = 1)
    major = major.objects.get(student_id = student.student_id)
    discipline = discipline.objects.get(discipline_id = major.discipline_id)
    credit_need = creditNeed.objects.get(discipline = discipline)
    curriculum = None
    try:
        curriculum = curriculum.objects.get(student = student)
    except:
        return redirect('curriculum')
    courses = curriculum.courses.all()
    # section = Section.objects.filter(takeup__course_id__course_curriculum = curriculum)
    if request.POST:
        courses = search(request.POST, courses)
                
    return render(request,'courseSelect/course_select.html',{
        'student': student, 
        'major':discipline, 
        'credit_need': credit_need,
        'curriculum':curriculum,
        'courses': courses,
        # 'section': section
    })

def select(request):
    if request.POST:
        msg = ''
        student = student.objects.get(student_id = int(request.POST['student_id']))
        try:
            section_id = int(request.POST['section_id'])
        except: 
            section_id = 0
        section = teach.objects.get(teach_id = section_id)
        
        # course_name = request.POST['course_name']
        #print(request.POST)
        if (request.POST['oper'] == 'select'):
            try:
                selection.objects.get(student = student, teach = section)
                msg = '该课程已经在您的已选列表当中！' 
                code = 500
            except:
                selection.objects.create(student = student, select_time = timezone.now(), state = False, priority = 1,teach = section)
                msg = '选课成功！'
                code = 0
        if (request.POST['oper'] == 'quit'):
            try:
                selection.objects.get(student = student, teach = section).delete()
                msg = '退课成功！'
                code = 0
            except:
                msg = '似乎还未选择这门课哦'
                code = 500
        # todo:
        return JsonResponse({'msg':msg, 'code':code})

def table(request):
    student = student.objects.get(student_id = 1)
    sections = teach.objects.filter(selection__student = student)
    return render(request, 'courseSelect/table.html',{'student':student,'sections':sections})

def teacher(request):
    teacher = teacher.objects.get(teacher_id = 2)
    sections = teach.objects.filter(takeup__teacher_id = teacher)
    return render(request, 'courseSelect/teacher.html',{'teacher':teacher,'sections':sections})

def curriculum(request):
    student = student.objects.get(student_id = 1)
    major = major.objects.get(student_id = student.student_id)
    discipline = discipline.objects.get(discipline_id = major.discipline_id)
    try:
        credit_need = creditNeed.objects.get(discipline = discipline)
    except:
        credit_need = creditNeed.objects.create(discipline = discipline,elective = 37.5,public = 12)
    try:
        curriculum = curriculum.objects.get(student = student)
    except:
        curriculum = curriculum.objects.create(student = student)
    selected_elective_credit = 0
    selected_public_credit = 0
    for course in curriculum.courses.all():
        if course.type == '2':
            selected_elective_credit +=  course.credit
        elif course.type == '3':
            selected_public_credit +=  course.credit
    courses = course.objects.all()
    # todo: 一张专业与课程对应表
    if request.POST:
        if 'oper' in request.POST:
            msg = ''
            try:
                course_id = int(request.POST['course_id'])
            except: 
                course_id = 0
            course = course.objects.get(course_id = course_id)
            if (request.POST['oper'] == 'add'):
                if course in curriculum.courses.all():
                    msg = course.name + '已在您的培养方案中！'
                    code = 500
                else:
                    curriculum.courses.add(course)
                    curriculum.save()
                    msg = course.name + '成功添加至您的培养方案中！'
                    code = 0
            elif request.POST['oper'] == 'drop':
                if course in curriculum.courses.all():
                    curriculum.courses.remove(course)
                    curriculum.save()
                    msg = course.name + '成功从您的培养方案中移除！'
                    code = 0
                else:
                    msg = course.name + '不在您的培养方案中！'
                    code = 500
            return JsonResponse({'msg':msg, 'code':code})
        else:
            courses = search(request.POST, courses)


    return render(request, 'courseSelect/curriculum.html', {
        'student': student, 
        'major':discipline, 
        'credit_need': credit_need,
        'curriculum':curriculum,
        'courses': courses,
        'selected_public_credit': selected_public_credit,
        'selected_elective_credit': selected_elective_credit,
    })

def export_excel(request):
    section_id = int(request.GET.get('section_id'))
    teacher_id = int(request.GET.get('teacher_id'))
    course_id = int(request.GET.get('course_id'))
    section = Teacj.objects.get(teach_id = section_id)
    teacher = teacher.objects.get(teacher_id = teacher_id)
    course = course.objects.get(course_id = course_id)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('学生名单')
    worksheet.set_column(0, 4, 20) 
    head1 = workbook.add_format({'font_name':'Arial', 'border':True, 'align':'center','font_size':20, 'bold': True})
    worksheet.merge_range('A1:E1', '学生名单  '+course.name , head1)
    head2 = workbook.add_format({'font_name':'Arial', 'border':True, 'align':'center','font_size':14, 'bold': True})
    worksheet.merge_range('A2:B2', '授课教师', head2)
    worksheet.merge_range('C2:E2', teacher.name, head2)
    # worksheet.write('C2', '上课时间', head2)
    # worksheet.write('D2', teacher.name, head2)
    head = workbook.add_format({'bold': True, 'font_name': 'Arial', 'border': True, 'align':'center','font_size':14, 'fg_color': '#aabb00'})
    body = workbook.add_format({'font_name': 'Arial','border': True, 'align':'center','font_size':14})
    worksheet.write('A3', '序号', head)
    worksheet.write('B3', '学号', head)
    worksheet.write('C3', '姓名', head)
    worksheet.write('D3', '专业', head)
    worksheet.write('E3', '备注', head)

    students = student.objects.filter(selection__teach = section, selection__state = True)
    row = 3
    col = 0
    for student in students:
        worksheet.write(row, col, row - 2, body)
        worksheet.write(row, col + 1, student.student_id, body)
        worksheet.write(row, col + 2, student.name, body)
        worksheet.write(row, col + 3, getDisciplineByStudent(student.student_id).name, body)
        worksheet.write(row, col + 4, '', body)

    workbook.close()
    response = HttpResponse(output.getvalue(), content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = '学生名单_{0}_{1}_{2}.xlsx'.format(course.name,teacher.name,section_id)
    response['Content-Disposition'] = 'attachment;filename=' + filename.encode('utf-8').decode('ISO-8859-1')

    return response

def control(request):
    select_control = selectControl.objects.all().order_by('-pk')[:1][0]    
    if request.POST:
        max_connections = int(request.POST['max_connections'])
        first_time_start = int(request.POST['first_time_start'])
        first_time_end = int(request.POST['first_time_end'])
        apply_time_start = int(request.POST['apply_time_start'])
        apply_time_end = int(request.POST['apply_time_end'])
        withdraw_time_start = int(request.POST['withdraw_time_start'])
        withdraw_time_end = int(request.POST['withdraw_time_end'])
        select_control.first_time.start = timestampToDatetime(first_time_start)
        select_control.first_time.end = timestampToDatetime(first_time_end)
        select_control.first_time.save()
        select_control.apply_time.start = timestampToDatetime(apply_time_start)
        select_control.apply_time.end = timestampToDatetime(apply_time_end)
        select_control.apply_time.save()
        select_control.withdraw_time.start = timestampToDatetime(withdraw_time_start)
        select_control.withdraw_time.end = timestampToDatetime(withdraw_time_end)
        select_control.withdraw_time.save()
        select_control.max_connections = max_connections
        select_control.save()
        return JsonResponse({'code':0,'msg':'修改成功'})
    return render(request, 'courseSelect/control_panel.html', {'select_control':select_control})

def get_discipline_options(request):
    colleges = college.objects.all()
    discipline_options = []
    for college in colleges:
        child = {'value':college.college_id,'label':college.name, 'children':[]}
        disciplines = discipline.objects.filter(belong__college_id = college).distinct()
        for discipline in disciplines:
            child['children'].append({'value':discipline.discipline_id, 'label':discipline.name})
        discipline_options.append(child)
    return JsonResponse(discipline_options, safe=False)

def get_discipline_details(request):
    discipline_id = int(request.GET.get('discipline_id'))
    discipline = discipline.objects.get(discipline_id=discipline_id)
    credit_need = creditNeed.objects.get(discipline=discipline)

    return JsonResponse({'min_elective':credit_need.elective,'min_public':credit_need.public})

def post_discipline_details(request):
    data = {'code': 500, 'msg': ''}
    if request.POST:
        discipline = discipline.objects.get(discipline_id = request.POST['discipline_id'])
        try:
            credit_need = creditNeed.objects.get(discipline=discipline)
        except:
            credit_need = creditNeed.objects.create(discipline=discipline,public=0,elective=0)
        credit_need.public = request.POST['min_public']
        credit_need.elective = request.POST['min_elective']
        credit_need.save()
        try:
            required_course = requiredCourse.objects.get(discipline=discipline)
        except:

            required_course = requiredCourse.objects.create(discipline=discipline)

        courses_id = request.POST['required_courses'].split(',')
        for course_id in courses_id:
            if not (int(course_id) in required_course.required_courses.all()):
                course = course.objects.get(course_id=int(course_id))
                required_course.required_courses.add(course)
        required_course.save()
        data['code']=0
        data['msg']='修改成功'
    return JsonResponse(data)

def get_all_courses(request):
    courses = course.objects.all().order_by('course_id')
    courses_options = []
    for course in courses:
        courses_options.append({
            'value':course.course_id,
            'label':'['+str(course.course_id)+'] '+course.name
        })
    return JsonResponse(courses_options, safe=False)

def get_required_courses(request):
    discipline_id = int(request.GET.get('discipline_id'))
    discipline = discipline.objects.get(discipline_id=discipline_id)
    data = []
    required_course = requiredCourse.objects.get(discipline=discipline)
    for course in required_course.required_courses.all():
        data.append({'course_id':course.course_id,'course_name':course.name})
    return JsonResponse(data, safe=False)

def remove_required_course(request):
    data = {'code': 500, 'msg': ''}
    if request.POST:
        discipline = discipline.objects.get(discipline_id=request.POST['discipline_id'])
        course = course.objects.get(course_id=request.POST['course_id'])
        required_course = requiredCourse.objects.get(discipline=discipline)
        if course in required_course.required_courses.all():
            required_course.required_courses.remove(course)
            data['code'] = 0
            data['msg'] = "已将 " + course.name + " 从 " + discipline.name + " 的必修课中移除！"
        else:
            data['code'] = 500
            data['msg'] = course.name + " 不在 " + discipline.name + " 的必修课列表中！"
        return JsonResponse(data)

def import_student(request):
    courses = course.objects.all()
    if request.POST:
        if 'oper' in request.POST:
            if request.POST['oper'] == 'import_student':
                student_id = request.POST['student_id']
                section_id = request.POST['section_id']
                course_id = request.POST['course_id']
                section = teach.objects.get(teach_id = section_id)
                course = course.objects.get(course_id = course_id)
                try:
                    student = student.objects.get(student_id = student_id)
                    try:
                        selections = selection.objects.filter(student = student,teach__course_id = course,state = True).exclude(teach = section)
                        if len(selections) > 0:
                            code = 500
                            msg = student_id+": "+student.name+" 已存在同一课程的其他班级中！"
                        else:
                            raise
                    except:
                        try:
                            selection = selection.objects.get(student = student,teach = section)
                            if selection.state:
                                code = 500
                                msg = student_id+": "+student.name+" 已存在课程名单中！"
                            else:
                                selection.state = True
                                selection.save()
                                msg = "成功将 "+student_id+": "+student.name+" 导入 "+course.name+"！"
                                code = 0
                        except:
                            selection = selection.objects.create(student = student,teach = section,select_time = timezone.now(),priority = 5,state = True)
                            msg = "成功将 "+student_id+": "+student.name+" 导入 "+course.name+"！"
                            code = 0
                except:
                    msg = "未搜索到学号为 "+student_id+" 的学生！请检查学号是否输入正确！"
                    code = 500
                return JsonResponse({"msg":msg, "code":code})
        else:
            courses = search(request.POST, courses)
    return render(request, "courseSelect/import_student.html", {"courses":courses})
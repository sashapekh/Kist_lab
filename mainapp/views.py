from django.shortcuts import render
from .models import *
from .forms import Query2Form
from mainapp.TableView import *
import sql_test
import django_tables2 as tables
import psycopg2

# Create your views here.
def main_page(request):
    # query1 - выполняет первый запрос по
    person_table = PersonTable(Person.objects.all())
    student_table = StudentTable(Student.objects.all())
    studentmarks_table = StudentMarksTable(Student_marks.objects.all())
    query1 = Student.objects.filter(finance_id='2', student_marks__mark_id__in=[1, 2, 3])
    return render(request, 'index.html', {'person': person_table,
                                          'student': student_table,
                                          'student_mark': studentmarks_table,
                                          'query1': query1,

                                          }, )


def search_form(request):
    form = Query2Form
    return render(request, 'search_form.html', {'form': form})


# result function for first query
def result(request):
    # connect to psql
    conn = psycopg2.connect(database='kist_db_2',
                            user='sashapekh',
                            password='',
                            host='localhost',
                            port='5432')
    cur = conn.cursor()
    data = [
        {'cafedra_name': '', 'speciality_name': '', 'group_code': ''}
    ]
    message = request.GET
    # query = PersonTable(Person.objects.filter(name=message['name'], surname=message['surname']).values())
    cur.execute("""select c.cafedra_name, sp.speciality_name,g.group_code from mainapp_cafedra as c
        join mainapp_speciality as sp on c.cafedra_id = sp.caferda_id_id
        join mainapp_groups as g on sp.speciality_id = g.speciality_id_id
        join mainapp_student_group as st on g.group_id = st.group_id_id
        join mainapp_student as s on st.student_id_id=s.student_id
        join mainapp_person as p on s.person_student_fk_id = p.person_id
        where p.surname = %s and p.name = %s ;""", (message['surname'], message['name']))
    query_result = cur.fetchall()
    print('result is  ' + str(query_result))
    print('message is = ',message)
    try:
        data[0]['cafedra_name'] = query_result[0][0]
        data[0]['speciality_name'] = query_result[0][1]
        data[0]['group_code'] = query_result[0][2]
    except IndexError:
        pass
    result_table = Query2Table(data)
    return render(request, 'result_2_query.html',
                  {'query_result': result_table,

                   })

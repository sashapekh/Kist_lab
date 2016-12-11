from django.shortcuts import render
from .models import *
from .forms import Query2Form
from mainapp.TableView import *
import sql_test
import django_tables2 as tables
import psycopg2
from django.db import connections


# Create your views here.
def main_page(request):
    # create query for 3-d result
    cursor = connections['default'].cursor()

    # create query for 4-th result
    cursor.execute('''select p.* from mainapp_person as p
  JOIN mainapp_student as st on p.person_id = st.person_student_fk_id
  JOIN mainapp_sfinance as sfinance on st.finance_id_id = sfinance.finance_id
  JOIN mainapp_student_marks as stmark on st.student_id = stmark.student_id_id
  JOIN mainapp_smark as smark on stmark.mark_id_id = smark.mark_id
  WHERE smark.mark_name IN ('C','B','A') and p.sex = 2 and sfinance.finance_name='Бюджет(+)';''')
    query4_result = sql_test.dictfetchall(cursor)

    # query1 - выполняет первый запрос по
    mark_name = Smark.objects.all().values('mark_name')
    student_name = Person.objects.all().values()
    cafedra_name = Cafedra.objects.all().values()

    return render(request, 'index.html', {
        'mark_name': mark_name,
        'student_name': student_name,
        'cafedra_name': cafedra_name,
    }, )


def search_form(request):
    form = Query2Form
    return render(request, 'search_form.html', {'form': form})


# result function for second query
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

    try:
        data[0]['cafedra_name'] = query_result[0][0]
        data[0]['speciality_name'] = query_result[0][1]
        data[0]['group_code'] = query_result[0][2]
    except IndexError:
        pass
    result_table = Query2Table(data)
    print(message)
    return render(request, 'result_2_query.html',
                  {'query_result': result_table,

                   })


def result_qur_2(request):
    message = request.GET
    name = str(message['name_surname']).split(' ', 1)[0]
    surname = str(message['name_surname']).split(' ', )[2]

    cursor = connections['default'].cursor()
    cursor.execute('''select p.name ,p.surname, caf.cafedra_name,smk.mark_name, contract.contract_sum from mainapp_person as p
  JOIN mainapp_student as st on p.person_id = st.person_student_fk_id
  JOIN mainapp_student_marks on st.student_id = mainapp_student_marks.student_id_id
  JOIN mainapp_smark as smk on mainapp_student_marks.mark_id_id = smk.mark_id
  JOIN mainapp_speciality on st.specialize_id_id = mainapp_speciality.speciality_id
  JOIN mainapp_cafedra as caf on mainapp_speciality.caferda_id_id = caf.cafedra_id
  JOIN mainapp_contract as contract on st.student_id = contract.student_id_id
  WHERE p.name = %s and p.surname = %s and caf.cafedra_name = %s and smk.mark_name = %s ;''',
                   (name, surname,
                    message['cafedra_name'], message['mark_name']))

    query_1_result = sql_test.dictfetchall(cursor)
    query_1_table = Query1Table(query_1_result)
    print(query_1_result)

    return render(request, 'result_qur_1.html', {'query_1_table': query_1_table})


def result_3_query(request):
    message = request.GET
    cursor = connections['default'].cursor()
    cursor.execute('''select DISTINCT p.name,p.surname,skind.contract_kind_name,contract.contract_sum,payment.payment_sum, contract.contract_date from mainapp_contract as contract
  JOIN mainapp_student as student on contract.student_id_id = student.student_id
  JOIN mainapp_person as p on student.person_student_fk_id = p.person_id
  JOIN mainapp_scontract_kind as skind on contract.contract_kind_id_id = skind.contract_kind_id
  JOIN mainapp_payment as payment ON contract.contract_id = payment.contract_id_id
  WHERE EXTRACT(year FROM contract.contract_date) = %s and EXTRACT(MONTH FROM contract.contract_date) = %s ;''',
                   (message['year'], message['month']))
    query_3_result = sql_test.dictfetchall(cursor)
    table_query3 = Query3Table(query_3_result)
    print(message)
    return render(request, 'result_3_query.html', {'table_query3': table_query3})


def result_4_query(request):
    message = request.GET
    cursor = connections['default'].cursor()
    cursor.execute('''select p.name, p.surname, p.sex , sfinance.finance_name from mainapp_person as p
  JOIN mainapp_student as st on p.person_id = st.person_student_fk_id
  JOIN mainapp_sfinance as sfinance on st.finance_id_id = sfinance.finance_id
  JOIN mainapp_student_marks as stmark on st.student_id = stmark.student_id_id
  JOIN mainapp_smark as smark on stmark.mark_id_id = smark.mark_id
  WHERE p.sex = 2 and sfinance.finance_name = %s  and smark.mark_name = %s ;''', (
            str(message['budget']),
            str(message['mark_name'])
    ))

    result_query_4 = sql_test.dictfetchall(cursor)
    query_table_4 = Query4Table(result_query_4)
    return render(request, 'result_4_query.html', {'query_table_4': query_table_4})

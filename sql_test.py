import psycopg2

conn = psycopg2.connect(database='kist_db_2',
                        user='sashapekh',
                        password='',
                        host='localhost',
                        port='5432')
cur = conn.cursor()
cur.execute("""select c.cafedra_name, sp.speciality_name,g.group_code from mainapp_cafedra as c
        join mainapp_speciality as sp on c.cafedra_id = sp.caferda_id_id
        join mainapp_groups as g on sp.speciality_id = g.speciality_id_id
        join mainapp_student_group as st on g.group_id = st.group_id_id
        join mainapp_student as s on st.student_id_id=s.student_id
        join mainapp_person as p on s.person_student_fk_id = p.person_id
        where p.surname = %s and p.name = %s ;""", ('Пех', 'Александр'))

result = cur.fetchall()
#
# print(len(result))

data = [
    {'cafedra_name': '', 'speciality_name': '', 'group_code': ''}
]
try:
    data[0]['cafedra_name'] = result[0][0]
    data[0]['speciality_name'] = result[0][1]
    data[0]['group_code'] = result[0][2]
except IndexError:
    pass
print(result)

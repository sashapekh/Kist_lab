import django_tables2 as tables
from mainapp.models import *


class PersonTable(tables.Table):
    class Meta:
        model = Person
        attrs = {'class': 'paleblue'}
        exclude = {'person_id'}


class StudentTable(tables.Table):
    class Meta:
        model = Student
        attrs = {'class': 'paleblue'}
        exclude = {'student_id'}


class StudentMarksTable(tables.Table):
    class Meta:
        model = Student_marks
        attrs = {'class': 'paleblue'}
        exclude = {'id'}


class Query2Table(tables.Table):
    cafedra_name = tables.Column()
    group_code = tables.Column()
    speciality_name = tables.Column()

    class Meta:
        attrs = {'class': 'paleblue'}


class Query3Table(tables.Table):
    surname = tables.Column()
    name = tables.Column()
    Patronymic = tables.Column()
    birth_day = tables.Column()
    address = tables.Column()
    telephone = tables.Column()
    contract_sum = tables.Column()

    class Meta:
        attrs = {'class': 'paleblue'}


class Query4Table(Query3Table):

    class Meta:
        exclude = {'contract_sum'}
        attrs = {'class': 'paleblue'}

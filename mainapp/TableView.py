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


class Query1Table(tables.Table):
    name = tables.Column('Имя')
    surname = tables.Column("Фалимия")
    cafedra_name = tables.Column("Кафедра")
    mark_name = tables.Column("Оценка")
    contract_sum = tables.Column("Цена за контракт")
    score = tables.Column()

    class Meta:
        attrs = {'class': 'paleblue'}


class Query2Table(tables.Table):
    cafedra_name = tables.Column("Имя кафедры")
    group_code = tables.Column("Название группы(код группы)")
    speciality_name = tables.Column("Название специальности")

    class Meta:
        attrs = {'class': 'paleblue'}


class Query3Table(tables.Table):
    name = tables.Column('Имя')
    surname = tables.Column("Фалимия")
    contract_kind_name = tables.Column('Тип контракта')
    contract_date = tables.Column('Дата оформления контракта')
    contract_sum = tables.Column('Сумма контракта')
    payment_sum = tables.Column('Сумма оплаты')

    class Meta:
        attrs = {'class': 'paleblue'}


class Query4Table(tables.Table):
    name = tables.Column("Имя")
    surname = tables.Column("Фамилия")
    sex = tables.Column("Стать")
    finance_name = tables.Column("Контракт или бюджет")

    class Meta:
        exclude = {'contract_sum'}
        attrs = {'class': 'paleblue'}

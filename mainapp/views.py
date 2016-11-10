from django.shortcuts import render
from .models import *
from .forms import Query2Form


# Create your views here.

def main_page(request):
    # quer1 - выполняет первый запрос по
    quer1 = Student.objects.filter(finance_id='2', student_marks__mark_id__in=[1, 2, 3])
    return render(request, 'index.html', {'person': Person.objects.all(),
                                          'student': Student.objects.all(),
                                          'student_mark': Student_marks.objects.all(),
                                          'quer1': quer1,
                                          }, )


def search_form(request):
    form = Query2Form
    return render(request, 'search_form.html', {'form': form})


def result(request):

    message = request.GET
    query = Person.objects.filter(name=message['name'], surname=message['surname']).values()
    test_var = query[0]['person_id']
    query_group_name = Groups.objects.filter(student_group__student_id_id=test_var)



    return render(request, 'result.html', {'query_result': query,'test_var':test_var,'query_group_name':query_group_name})

from django.db import models


# Create your models here.

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=False)
    Patronymic = models.CharField(max_length=30, null=True)
    # sex models -> if 1 - male , 2 - female
    sex = models.SmallIntegerField(null=False)
    # DateField - YYYY.MM.DD
    birth_day = models.DateField(null=False)
    address = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.surname + ' ' + self.name


class Sdiploma(models.Model):
    diploma_id = models.AutoField(primary_key=True)
    diploma_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.diploma_name


class Smark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    mark_name = models.CharField(max_length=1, null=False)
    old_type_mark = models.FloatField(max_length=3, null=False, default=1)

    def __str__(self):
        return self.mark_name


class Cafedra(models.Model):
    cafedra_id = models.AutoField(primary_key=True)
    cafedra_name = models.CharField(max_length=50, null=False)
    cafedra_shifr = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.cafedra_name


class Speciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    speciality_name = models.CharField(max_length=50, null=False)
    speciality_shifr = models.CharField(max_length=10, null=False)
    caferda_id = models.ForeignKey(Cafedra, on_delete=models.CASCADE)

    def __str__(self):
        return self.speciality_name


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_code = models.CharField(max_length=10, null=False)
    group_create_date = models.DateField(null=False)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_code + " " + str(self.group_create_date)


class Sfinance(models.Model):
    finance_id = models.AutoField(primary_key=True)
    finance_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.finance_name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    finance_id = models.ForeignKey(Sfinance, on_delete=models.CASCADE)
    diploma_id = models.ForeignKey(Sdiploma, on_delete=models.CASCADE)
    specialize_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    book_no = models.CharField(max_length=15, null=False)
    note = models.TextField(max_length=255, null=True)
    person_student_fk = models.OneToOneField(Person, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(Person.objects.filter(student__student_id=self.student_id).values('surname', 'name')) + str(self.finance_id)


class Scontract_kind(models.Model):
    contract_kind_id = models.AutoField(primary_key=True)
    contract_kind_name = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.contract_kind_name


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    contract_kind_id = models.OneToOneField(Scontract_kind, on_delete=models.CASCADE)
    contract_date = models.DateField(null=False)
    contract_sum = models.CharField(max_length=15, null=False)
    payer_kind = models.CharField(max_length=15, null=False)

    def __str__(self):
        return str(self.student_id) + ' ' + str(self.contract_date)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    payment_date = models.DateField(null=False)
    payment_sum = models.CharField(max_length=15, null=False)
    document_no = models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.contract_id)


class Student_group(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    putting_date = models.DateField(null=False)

    def __str__(self):
        return " student " + str(self.student_id) + ' was added to group  ' + str(self.group_id)


class Student_marks(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark_id = models.ForeignKey(Smark, on_delete=models.CASCADE)

    def __str__(self):
        return 'mark is ' + str(self.mark_id) + ' for student - ' + str(self.student_id)

from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=50)
    address=models.TextField()
    
    def __str__(self):
        return f"name : {self.name}"
    
    
# Inheritance Module
# 1. abstract base class
# 2. multitable inheritance
# 3. proxy model

# 1. abstract base class

class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    
# 2. Multitable inheritance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# 3. proxy model

class Friend(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    class_teacher= models.CharField(max_length=20)
    attendance = models.BooleanField()
    hw=models.CharField(max_length=50)
    
class Me(Friend):
    class Meta:
        proxy=True
        ordering = ['id']
  
# 1. one to one relation:      
class Persion(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.name
    
class Password(models.Model):#Password = Passport
    user= models.OneToOneField(to=Persion ,on_delete = models.CASCADE)
    pass_number= models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# 2. one to many relation:
class Post(models.Model):
    user = models.ForeignKey(Persion, on_delete=models.SET_NULL,null=True)
    post_cap = models.CharField(max_length=30)
    post_details= models.CharField(max_length=1000)
    create_at=models.DateTimeField()

#3. many to many relationship

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(max_length=10)
    class_name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student,related_name='teachers') # related_name case reverse relationship
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade

fake = Faker()

engine = create_engine('postgresql://user:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()

# Наповнення таблиці Group
groups = []
for _ in range(5):
    group = Group(name=fake.word())
    groups.append(group)

session.bulk_save_objects(groups)
session.commit()

# Наповнення таблиці Student
students = []
for _ in range(20):
    student = Student(fullname=fake.name(), group_id=fake.random_element(elements=groups).id)
    students.append(student)

session.bulk_save_objects(students)
session.commit()

# Наповнення таблиці Subject
subjects = []
for _ in range(3):
    subject = Subject(name=fake.word())
    subjects.append(subject)

session.bulk_save_objects(subjects)
session.commit()

# Наповнення таблиці Teacher
teachers = []
for _ in range(10):
    teacher = Teacher(fullname=fake.name(), subject_id=fake.random_element(elements=subjects).id)
    teachers.append(teacher)

session.bulk_save_objects(teachers)
session.commit()

# Наповнення таблиці Grade
grades = []
for student in students:
    for subject in subjects:
        grade = Grade(value=fake.random_int(min=1, max=10), student_id=student.id, subject_id=subject.id)
        grades.append(grade)

session.bulk_save_objects(grades)
session.commit()

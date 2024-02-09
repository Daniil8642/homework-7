# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_name):
    result = session.query(Student.fullname, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Student.id).order_by(desc('avg_grade')).limit(1).first()
    return result

# Знайти середній бал у групах з певного предмета.
def select_3(subject_name):
    result = session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).join(Group) \
        .filter(Subject.name == subject_name).group_by(Group.id).all()
    return result

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    result = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')).first()
    return result[0] if result else None

# Знайти які курси читає певний викладач.
def select_5(teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return [subject[0] for subject in result]

# Знайти список студентів у певній групі.
def select_6(group_name):
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return [student[0] for student in result]

# Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group_name, subject_name):
    result = session.query(Student.fullname, Grade.value) \
        .join(Group).join(Subject).join(Grade) \
        .filter(Group.name == group_name, Subject.name == subject_name).all()
    return result

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_name):
    result = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Subject).join(Teacher) \
        .filter(Teacher.name == teacher_name).first()
    return result[0] if result else None

# Знайти список курсів, які відвідує певний студент.
def select_9(student_name):
    result = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).all()
    return [subject[0] for subject in result]

# Список курсів, які певному студенту читає певний викладач.
def select_10(student_name, teacher_name):
    result = session.query(Subject.name).join(Grade).join(Student).join(Teacher) \
        .filter(Student.fullname == student_name, Teacher.name == teacher_name).all()
    return [subject[0] for subject in result]

if __name__ == "__main__":
    # Викликайте функції для перевірки результатів
    result_2 = select_2('Mathematics')
    print(result_2)

    result_3 = select_3('Physics')
    print(result_3)

    result_4 = select_4()
    print(result_4)

    result_5 = select_5('John Doe')
    print(result_5)

    result_6 = select_6('Group A')
    print(result_6)

    result_7 = select_7('Group A', 'Chemistry')
    print(result_7)

    result_8 = select_8('John Doe')
    print(result_8)

    result_9 = select_9('Alice Smith')
    print(result_9)

    result_10 = select_10('Alice Smith', 'Jane Johnson')
    print(result_10)


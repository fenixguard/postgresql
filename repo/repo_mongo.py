from typing import List


def add_course(conn, course: str):  # добавить курс
    cur = conn.cursor()
    cur.execute('''INSERT INTO course(name) VALUES (%s);''',
                (course,))
    conn.commit()


def add_student(conn, student: List):  # добавить студента в базу данных
    cur = conn.cursor()
    cur.execute('''INSERT INTO student(name, gpa, birth) VALUES (%s, %s, %s);''',
                (student[0], student[1], student[2],))
    conn.commit()


def add_student_to_course(conn, course_id, student_id):  # добавить студента на курс
    cur = conn.cursor()
    cur.execute('''INSERT INTO student_course(student_id, course_id) VALUES (%s, %s);''',
                (student_id, course_id, ))
    conn.commit()


def get_student(conn, student_id):  # получить студента
    cur = conn.cursor()
    cur.execute('''SELECT * FROM student WHERE id = (%s);''', (student_id,))
    return cur.fetchall()[0][1]


def get_students(conn, course_id):  # возвращает студентов определенного курса
    cur = conn.cursor()
    cur.execute('''SELECT s.name, c.name FROM student_course AS sc
        JOIN student s on s.id = sc.student_id
        JOIN course c on c.id = sc.course_id WHERE c.id = %s
    ;''', (course_id,))
    return cur.fetchall()

import psycopg2 as pg
from pprint import pprint
from repo.repo_mongo import get_student, add_student, get_students, add_student_to_course, add_course


COURSES = [
    'Продвинутый Python',
    'Основы HTML и CSS',
    'Фриланс - с чего начать?'
]

STUDENTS = [
    ['Иванов Иван Иванович', 4.75, '1999-01-01 00:00:00'],
    ['Сидоров Петр Ильич', 0, '2000-05-01 00:00:00'],
    ['Петров Игорь Олегович', 3.00, '2005-06-07 00:00:00'],
    ['Пропусков Геннадий Сергеевич', 4.5, '1994-07-07 00:00:00'],
    ['Сергеев Михаил Сидорович', 5.00, '2003-02-10 00:00:00']
]


def init_database(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student (
          id SERIAL PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          gpa NUMERIC (10, 2) null,
          birth TIMESTAMP
        );''')

    cur.execute('''CREATE TABLE course (
          id SERIAL PRIMARY KEY,
          name VARCHAR(100) NOT NULL
        );''')

    cur.execute('''CREATE TABLE IF NOT EXISTS student_course (
          student_id INTEGER REFERENCES student(id),
          course_id INTEGER REFERENCES course(id),
          CONSTRAINT student_course_pk PRIMARY KEY(student_id, course_id)
        );''')


def main():
    with pg.connect(database='netology', user='netology', password='netology') as conn:
        init_database(conn)
        for course in COURSES:
            add_course(conn, course)
        for student in STUDENTS:
            add_student(conn, student)

        pprint(get_student(conn, student_id=3))
        pprint(get_student(conn, student_id=1))
        add_student_to_course(conn, course_id=1, student_id=3)
        add_student_to_course(conn, course_id=2, student_id=1)
        add_student_to_course(conn, course_id=1, student_id=4)
        add_student_to_course(conn, course_id=3, student_id=2)
        add_student_to_course(conn, course_id=3, student_id=5)
        pprint(get_students(conn, course_id=1))
        print('=' * 50)
        pprint(get_students(conn, course_id=2))
        print('=' * 50)
        pprint(get_students(conn, course_id=3))
        print('=' * 50)


if __name__ == '__main__':

    main()


from manim import *
from props.academia import *

lecture_number = 3
lecture_title = "Introduction to Recursion"
course_code = "CSE 4202"
course_title = "Structured Programming II Lab"
course_teachers = [
    CourseTeacher(
        name="Irfanur Rahman Rafio",
        designation="Part-time Lecturer",
        email="irfanurrahman5@iut-dhaka.edu",
        department="CSE",
        institution="Islamic University of Technology"
    ),
    CourseTeacher(
        name="Reaz Hassan Joarder",
        designation="Junior Lecturer",
        email="reazhassan@iut-dhaka.edu",
        department="CSE",
        institution="Islamic University of Technology"
    ),
    CourseTeacher(
        name="Syed Rifat Raiyan",
        designation="Lecturer",
        email="rifatraiyan@iut-dhaka.edu",
        department="CSE",
        institution="Islamic University of Technology"
    ),

    CourseTeacher(
        name="Asaduzzaman Herok",
        designation="Lecturer",
        email="asaduzzaman34@iut-dhaka.edu",
        department="CSE",
        institution="Islamic University of Technology"
    ),

    CourseTeacher(
        name="Shahriar Ivan",
        designation="Assistant Professor",
        email="shahriarivan@iut-dhaka.edu",
        department="CSE",
        institution="Islamic University of Technology"
    )
]

def add_footer(scene):
    add_lecture_footer(
        scene,
        text1=f"{course_code}: {course_title}",
        text2=f"Lecture {lecture_number}",
        text3="IUT CSE"
    )
from manim import *
from manim_slides import Slide

class CourseTeacher:
    def __init__(
        self,
        name,
        designation,
        email,
        department,
        institution
    ):
        self.name = name
        self.designation = designation
        self.email = email
        self.department = department
        self.institution = institution

class TitleSlide(Slide):
    def __init__(
        self,
        lecture_number="",
        lecture_title="",
        course_code="",
        course_title="",
        course_teachers=None,
        text_color1=WHITE,
        text_color2=GRAY,
        font_size1=30,
        font_size2=28,
        font_size3=20,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        self.lecture_number = lecture_number
        self.lecture_title = lecture_title
        self.course_code = course_code
        self.course_title = course_title
        self.course_teachers = course_teachers or []

        self.text_color1 = text_color1
        self.text_color2 = text_color2

        self.font_size1 = font_size1
        self.font_size2 = font_size2
        self.font_size3 = font_size3

        self.build_title()
        self.build_course_info()
        self.build_teachers()
        self.position_elements()

    def construct(self):
        self.present()
        self.next_slide()
        self.cleanup()
        self.next_slide()

    def build_title(self):
        self.title_main = Tex(
            rf"\textbf{{Lecture {self.lecture_number}: {self.lecture_title}}}",
            color=self.text_color1,
            font_size=self.font_size1
        )

    def build_course_info(self):
        self.title_course = Tex(
            rf"{self.course_code}: {self.course_title}",
            color=self.text_color2,
            font_size=self.font_size2
        )

    def build_teachers(self):
        teacher_groups = [
            self._build_teacher_group(t)
            for t in self.course_teachers
        ]

        if not teacher_groups:
            self.teachers_group = VGroup()
            return

        cols = 3
        n = len(teacher_groups)

        first_row_size = n % cols
        if first_row_size == 0: first_row_size = cols

        rows = []
        start = 0

        first_row = VGroup(*teacher_groups[start:start + first_row_size]).arrange(RIGHT, buff=1)
        rows.append(first_row)
        start += first_row_size

        while start < n:
            row = VGroup(*teacher_groups[start:start + cols]).arrange(RIGHT, buff=1)
            rows.append(row)
            start += cols

        self.teachers_group = VGroup(*rows).arrange(DOWN, buff=0.6)

    def _build_teacher_group(self, teacher):
        name = Tex(rf"\textbf{{{teacher.name}}}", color=self.text_color1, font_size=self.font_size3)
        designation = Tex(teacher.designation, color=self.text_color1, font_size=self.font_size3)
        email = Tex(teacher.email, color=self.text_color1, font_size=self.font_size3)

        department = Tex(f"Department of {teacher.department}", color=self.text_color2, font_size=self.font_size3)
        institution = Tex(teacher.institution, color=self.text_color2, font_size=self.font_size3)

        return VGroup(
            name,
            designation,
            email,
            department,
            institution
        ).arrange(DOWN, buff=0.1)

    def position_elements(self):
        title_group = VGroup(
            self.title_main,
            self.title_course
        ).arrange(DOWN, buff=0.2)

        self.group = VGroup(
            title_group,
            self.teachers_group
        ).arrange(DOWN, buff=1)

        self.group.move_to(ORIGIN)

    def present(self, run_time=1):
        self.play(Create(self.group), run_time=run_time)

    def cleanup(self, run_time=1):
        self.play(Uncreate(self.group), run_time=run_time)

def add_lecture_footer(
    scene,
    text1,
    text2,
    text3,
    bg1=GREEN_E,
    bg2=GREEN_D,
    bg3=GREEN_C,
    text_color=WHITE,
    font_size=16
):
    total_w = config.frame_width
    h = 0.4

    w1 = total_w * 0.4
    w2 = total_w * 0.4
    w3 = total_w * 0.2

    rect1 = Rectangle(width=w1, height=h)
    rect2 = Rectangle(width=w2, height=h)
    rect3 = Rectangle(width=w3, height=h)

    rect1.set_fill(bg1, opacity=1).set_stroke(text_color, width=1)
    rect2.set_fill(bg2, opacity=1).set_stroke(text_color, width=1)
    rect3.set_fill(bg3, opacity=1).set_stroke(text_color, width=1)

    t1 = Tex(text1, color=text_color, font_size=font_size).move_to(rect1.get_center())
    t2 = Tex(text2, color=text_color, font_size=font_size).move_to(rect2.get_center())
    t3 = Tex(text3, color=text_color, font_size=font_size).move_to(rect3.get_center())

    footer = VGroup(
        VGroup(rect1, t1),
        VGroup(rect2, t2),
        VGroup(rect3, t3),
    ).arrange(RIGHT, buff=0)

    separators = VGroup(
        Line(UP * h / 2, DOWN * h / 2)
        .set_stroke(text_color, width=1)
        .move_to(rect1.get_right()),

        Line(UP * h / 2, DOWN * h / 2)
        .set_stroke(text_color, width=1)
        .move_to(rect2.get_right()),
    )

    footer_group = VGroup(footer, separators)
    footer_group.to_corner(DOWN, buff=0)

    scene.footer_mob = footer_group
    scene.add(scene.footer_mob)
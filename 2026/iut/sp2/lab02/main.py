from manim import *
from manim_slides import Slide
from props.presentation import *
from props.code_style import *
from lab_info import *

sans_template = TexTemplate()
sans_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
Tex.set_default(tex_template=sans_template)

class Title_Recursion(TitleSlide):
    def __init__(self, **kwargs):
        super().__init__(
            lecture_number=lecture_number,
            lecture_title=lecture_title,
            course_code=course_code,
            course_title=course_title,
            course_teachers=course_teachers,
            text_color1=BLACK,
            text_color2=DARK_GREY,
            **kwargs
        )
        add_footer(self)

class Introduction(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Introduction",
            text_color=BLACK,
            points=[
                r"Can a function solve a problem by calling itself?",
                r"At first, this might sound strange or even impossible.",
                r"However, many problems become much easier when they are broken into smaller versions of the same problem.",
                r"This idea leads to recursion, where a function uses smaller instances of itself to build a solution.",
                r"Although recursion may seem confusing at first, it is a natural and powerful way to think about problems.",
                r"To use recursion effectively, programmers need to understand its rules and develop the right way of thinking."
            ],
            **kwargs
        )
        add_footer(self)

class TableOfContents(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Table of Contents",
            text_color=BLACK,
            points = [
                r"Functions and Modular Programming",
                r"The Main Idea of Recursion",
                r"Memory In Recursion",
                r"Branching In Recursion",
                r"Recursive Leap of Faith",
                r"The Idea of Generalization"
            ],
            **kwargs
        )
        add_footer(self)

class Section_Functions(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Functions\\and\\Modular\\Programming",
            **kwargs
        )
        add_footer(self)

class Functions(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Functions and Modular Programming",
            text_color=BLACK,
            points=[
                r"A function is a reusable block of code usually designed to perform a single, specific task.",
                r"It acts as a modular unit that organizes logic, improves readability, and prevents code duplication by allowing a set of instructions to be written once and called multiple times.",
                r"A function is like a program inside a program.",
                r"Programmers often think of programs as machines. In that sense, functions can be seen as machines used by the main program, and a recursive functions can be seen as a machine that uses copies of itself to complete its task.",
                r"Functions are also called modules, procedures, methods, subroutines, or subprograms depending on the programming context."
            ],
            **kwargs
        )
        add_footer(self)

class ModularProgramming1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Functions and Modular Programming",
            text_color=BLACK,
            points=[
                r"Modular programming is the process of organizing a program into independent and well-defined components.",
                r"In simple language, when you're outside a function, don't worry about what's inside (how it is implemented) and when you're inside a function, don't worry about what's outside (where it is used).",
                r"The interaction between different functions of a program is defined only by inputs, outputs, side effects, time complexity, and space requirements.",
            ],
            **kwargs
        )
        add_footer(self)

class ModularProgramming2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Functions and Modular Programming",
            text_color=BLACK,
            points=[
                r"Modular Programming reduces cognitive load by letting programmers focus on one piece at a time.",
                r"It improves reusability because the same function can be used in different places.",
                r"It improves readability because complex problems are split into simpler parts.",
                r"It makes testing easier because each part can be checked independently."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Recursion(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"The Main\\Idea of\\Recursion",
            **kwargs
        )
        add_footer(self)

class RecursionIdea(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="The Main Idea of Recursion",
            text_color=BLACK,
            points=[
                r"Recursion is a technique where a function solves a problem by calling itself on smaller inputs.",
                r"Recursion is used to solve problems where knowing the result of subproblems (same problem with different inputs) can be helpful.",
                r"Although recursion seems unintuitive initially, it is a very natural way of thinking that is widely used.",
                r"Every recursive algorithm can be converted into an iterative one, but using recursion sometimes makes the idea clearer and the code easier to read."
            ],
            **kwargs
        )
        add_footer(self)

class Rules(BulletSlide):
    def __init__(self, **kwargs):
        text_color=BLACK

        code_file = f"./assets/code/powr.c"
        code = StylelessCode(
            code_file=code_file,
            text_color=text_color
        ).scale(0.5)

        super().__init__(
            header_text="The Main Idea of Recursion",
            text_color=BLACK,
            points=[
                r"Every recursive function must have at least one base case and one recursive step.",
                r"The base case is the simplest case that can be answered directly without any further recursion.",
                r"The recursive step reduces the problem by calling the same function on a smaller input.",
                r"Critical requirement: Each recursive call must move the problem closer to the base case to ensure termination.",
                r"Any assumptions about the domain of valid inputs must be clearly defined so that the base case is guaranteed to be reached."
            ],
            side_mobject=code,
            **kwargs
        )
        add_footer(self)

        self.poster = ImageMobject("./assets/img/first-rule.png")
        self.poster.scale_to_fit_height(6)

    def present_points(self, run_time=1):
        self.play(FadeIn(self.poster))
        self.next_slide()

        self.play(FadeOut(self.poster))
        self.next_slide()

        self.play(Create(self.side))
        self.next_slide()

        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

class Section_Memory(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Memory\\In\\Recursion",
            **kwargs
        )
        add_footer(self)

class Memory(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Memory In Recursion",
            text_color=BLACK,
            points=[
                r"Every function call gets its own set of parameters and local variables.",
                r"When a function calls another function, its current state is stored so that execution can resume correctly after that function returns.",
                r"These calls are managed using the call stack, which follows a Last-In, First-Out (LIFO) order.",
                r"In recursion, multiple function calls are stacked on top of each other before earlier calls complete. Each recursive call must wait for the result of deeper calls before continuing execution.",
                r"Recursion requires additional memory due to the storage of multiple active function calls.",
                r"Too many recursive calls can cause a stack overflow if memory runs out."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Branching(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Branching\\In\\Recursion",
            **kwargs
        )
        add_footer(self)

class Branching(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Branching In Recursion",
            text_color=BLACK,
            points=[
                r"Some recursive functions make more than one recursive call.",
                r"These recursive calls are executed sequentially, even though they conceptually form branches.",
                r"Branching recursion leads to a recursion tree structure that represents all function calls.",
                r"The number of function calls can grow very quickly, often exponentially, in branching recursion."
            ],
            **kwargs
        )
        add_footer(self)

class Section_LeapOfFaith(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Recursive\\Leap of\\Faith",
            **kwargs
        )
        add_footer(self)

class LeapOfFaith1(BulletSlide):
    def __init__(self, **kwargs):
        text_color=BLACK

        code_file = f"./assets/code/fib.c"
        code = StylelessCode(
            code_file=code_file,
            text_color=text_color
        ).scale(0.5)

        super().__init__(
            header_text="Recursive Leap of Faith",
            text_color=text_color,
            points=[
                r"Drawing full recursion trees or tables is for beginners to understand the behavior of recursion so that they can convince themselves or get an intuition that recursion works.",
                r"Once a programmer is comfortable with the idea of recursion, he doesn't need to draw the full tree anymore (sometimes a few levels can be drawn for debugging purposes).",
                r"Recursive leap of faith extends the idea of modular programming to recursion.",
                r"It is not necessary to check how the subproblems get their results.",
                r"The focus is only on verifying that the \textbf{base case} is correct (and always reachable) and that the current step \textbf{correctly uses} results from smaller inputs \textit{assuming they are correct}."
            ],
            side_mobject=code,
            **kwargs
        )
        add_footer(self)

    def present_points(self, run_time=1):
        for bullet in self.bullets[:2]:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Write(self.side))
        self.next_slide()

        for bullet in self.bullets[2:]:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

class LeapOfFaith2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Recursive Leap of Faith",
            text_color=BLACK,
            points=[
                r"If the base case is correct, then the smallest case of the problem is solved correctly.",
                r"If each case is correct assuming the previous (smaller) cases are correct, then the method works step by step.",
                r"Since the first case is correct, the second case must also be correct.",
                r"Since the second case is correct, the third case must also be correct, and this continues for all cases.",
                r"Therefore, the correctness of the entire algorithm is proved by mathematical induction."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Generalization(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"The Idea\\of\\Generalization",
            **kwargs
        )
        add_footer(self)

class Generalization(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="The Idea of Generalization",
            text_color=BLACK,
            points=[
                r"Generalization is the process of moving from specific instances to a broader concept",
                r"Generalization can expand domain by removing assumptions, such as extending natural numbers to integers, rational numbers, real numbers, and eventually complex numbers.",
                r"Functions can be generalized by introducing additional parameters, making them more flexible and capable of solving a broader range of problems.",
                r"For example, the function \texttt{getSquareArea(length)} can be generalized to \texttt{getRectangleArea(length, width)}.",
                r"Sometimes a problem or algorithm may not appear recursive in its original form, but after generalizing the problem, recursion becomes possible."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Debug(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Debugging\\Practice",
            **kwargs
        )
        add_footer(self)

class DebugCode(Slide):
    def __init__(self, idx, mistake, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        code_file = f"./assets/code/dbg{idx}.c"
        header_text = rf"Debugging Practice --- Example ${idx}$"

        self.text_color = BLACK
        add_header(self, header_text, text_color=self.text_color)
        add_footer(self)

        self.build_group(code_file, mistake)
        self.fit_group_in_frame()
        self.position_group()

    def construct(self):
        self.present()
        self.next_slide()
        self.cleanup()
        self.next_slide()
    
    def build_group(self, code_file, mistake):
        self.code = StylelessCode(
            code_file=code_file,
            text_color=self.text_color
        )
        self.mistake = Tex(mistake, color=self.text_color)
    
    def fit_group_in_frame(self):
        max_width = config.frame_width - 1
        max_height = config.frame_height - 2 - self.header_mob.height

        if self.code.width > max_width:
            self.code.scale_to_fit_width(max_width)

        if self.mistake.width > max_width:
            self.mistake.scale_to_fit_width(max_width)

        self.group = VGroup(self.code, self.mistake)
        self.group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        if self.group.height > max_height:
            self.group.scale_to_fit_height(max_height)
    
    def position_group(self):
        self.group.next_to(
            self.header_mob,
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        )

    def present(self, run_time=1):
        self.play(Write(self.code), run_time=run_time)
        self.next_slide()
        self.play(Write(self.mistake), run_time=run_time)
        self.next_slide()
    
    def cleanup(self, run_time=1):
      self.play(
          Unwrite(self.group),
          run_time=run_time
      )

class Debug1(DebugCode):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 1,
            mistake = r"\textbf{Mistake}: No base case!",
            **kwargs
        )

class Debug2(DebugCode):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 2,
            mistake = r"\textbf{Mistake}: Wrong recursion step!",
            **kwargs
        )

class Debug3(DebugCode):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 3,
            mistake = r"\textbf{Mistake}: Does not reach base case!",
            **kwargs
        )

class Debug4(DebugCode):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 4,
            mistake = r"\textbf{Mistake}: Wrong recursion step and logic!",
            **kwargs
        )

class Debug5(DebugCode):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 5,
            mistake = r"\textbf{No mistake}! This is a working function for printing the octal value of an integer.",
            **kwargs
        )

class Section_Summary(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Summary",
            **kwargs
        )
        add_footer(self)

class Summary(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Summary",
            text_color=BLACK,
            points=[
                r"Recursion solves problems by reducing them to smaller instances of the same problem.",
                r"A correct recursive solution depends on a clear base case and a correct recursive step.",
                r"The recursive leap of faith allows focusing only on the current step instead of the entire process.",
                r"The total running time of a recursive function depends on the work done across all recursive calls.",
                r"The space requirement depends on how many function calls are active at the same time (at the call stack).",
                r"Sometimes a problem needs to be generalized to solve with recursion."
            ],
            **kwargs
        )
        add_footer(self)

class Ending(Slide):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1
        add_footer(self)
    
    def construct(self):
        txt = Tex("To Be Continued", color=BLACK, font_size=DEFAULT_FONT_SIZE * 3)
        self.play(Write(txt))
        self.next_slide()
        self.play(Unwrite(txt))
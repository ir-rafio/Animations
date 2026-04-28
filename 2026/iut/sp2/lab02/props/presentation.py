from manim import *
from manim_slides import Slide
import math

def add_header(scene, header_text, text_color=WHITE):
    scene.header_mob = Tex(header_text, color=text_color).to_corner(UL)
    scene.add(scene.header_mob)

    add_header_underline(scene, text_color=text_color)


def add_header_underline(scene, margin=0.5, text_color=WHITE):
    half_width = config.frame_width / 2

    scene.header_underline = Line(
        LEFT * (half_width - margin),
        RIGHT * (half_width - margin),
    )

    scene.header_underline.next_to(scene.header_mob, DOWN, buff=0.15)
    scene.header_underline.align_to(scene.header_mob, LEFT)
    scene.header_underline.set_stroke(width=2, color=text_color)

    scene.add(scene.header_underline)

class SectionSlide(Slide):
    def __init__(
        self,
        section_title="",
        circle_color=GREEN_E,
        text_color=WHITE,
        radius=3,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        self.section_title = rf"\textbf{{{section_title}}}"
        self.circle_color = circle_color
        self.text_color = text_color
        self.radius = radius

        self.build_circle()
        self.build_title()
        self.fit_text_in_circle()
        self.position_elements()

    def construct(self):
        self.present_section()
        self.next_slide()
        self.cleanup()

    def build_circle(self):
        self.circle = Circle(radius=self.radius)
        self.circle.set_fill(self.circle_color, opacity=1)
        self.circle.set_stroke(width=0)

    def build_title(self):
        self.title = Tex(self.section_title, color=self.text_color)

    def fit_text_in_circle(self):
        scale_factor = math.sqrt(2) * 0.9
        max_width = self.radius * scale_factor
        max_height = self.radius * scale_factor

        self.title.scale_to_fit_width(max_width)

        if self.title.height > max_height:
            self.title.scale_to_fit_height(max_height)

    def position_elements(self):
        self.group = VGroup(self.circle, self.title)
        self.title.move_to(self.circle.get_center())

        self.group.move_to(ORIGIN)

    def present_section(self, run_time=2):
        self.play(FadeIn(self.circle), run_time=run_time / 2)
        self.play(Write(self.title), run_time=run_time / 2)
    
    def cleanup(self, run_time=1):
      self.play(FadeOut(self.group), run_time=run_time)

class BulletSlide(Slide):
    def __init__(
        self,
        header_text="",
        points=None,
        side_mobject=None,
        text_color=WHITE,
        bullet_symbol=r"$\square$",
        **kwargs
    ):
        super().__init__(**kwargs)

        self.wait_time_between_slides = 0.1

        self.header_text = header_text
        self.points = points or []
        self.text_color = text_color

        self.side = VGroup(side_mobject) if side_mobject is not None else VGroup()

        add_header(self, header_text, text_color=self.text_color)

        self.build_points(bullet_symbol)
        self.layout()

    def construct(self):
        self.present_points()
        self.next_slide()
        self.cleanup()
        self.next_slide()

    def build_points(self, bullet_symbol):
        self.bullets = VGroup(*[
            VGroup(
                Tex(bullet_symbol, color=self.text_color),
                Tex(p, color=self.text_color)
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            for p in self.points
        ])

    def layout(self):
        self.bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        self.fit_in_frame(self.bullets)
        self.position_group(self.bullets)

        if len(self.side) == 0: return

        overlap, non_overlap = self.split_by_overlap()
        self.fit_in_frame(overlap, max_width=config.frame_width - 1 - self.side.width)

        cluster = VGroup(overlap, self.side).arrange(
            RIGHT,
            buff=0.4,
            aligned_edge=UP
        )

        self.position_group(cluster)
        non_overlap.next_to(cluster, DOWN, buff=0.4, aligned_edge=LEFT)

        self.fit_in_frame(VGroup(self.bullets, self.side))

    def split_by_overlap(self):
        overlap = VGroup()
        non_overlap = VGroup()

        side_bottom = self.side.get_bottom()[1]

        for b in self.bullets:
            if b.get_top()[1] > side_bottom:
                overlap.add(b)
            else:
                non_overlap.add(b)

        return overlap, non_overlap

    def fit_in_frame(
            self,
            mob,
            max_width=None,
            max_height=None
        ):
        if(max_width is None): max_width = config.frame_width - 1
        if(max_height is None): max_height = config.frame_height - 2 - self.header_mob.height

        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)

        if mob.height > max_height:
            mob.scale_to_fit_height(max_height)

    def position_group(self, mob):
        mob.next_to(
            self.header_mob,
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        )

    def present_points(self, run_time=1):
        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        if len(self.side) > 0:
            self.play(Create(self.side))
            self.next_slide()

    def cleanup(self, run_time=1):
        self.play(
            *[Unwrite(b) for b in self.bullets],
            Uncreate(self.side),
            run_time=run_time
        )

class MathExpansionSlide(Slide):
    def __init__(
        self,
        header_text="",
        lhs_builder="",
        rhs_builders=None,
        comparison_symbols=None,
        text_color=WHITE,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.wait_time_between_slides = 0.1
        self.text_color = text_color

        lhs_builder = lhs_builder
        rhs_builders = rhs_builders or []
        comparison_symbols = comparison_symbols or []

        if len(rhs_builders) == 0:
            raise ValueError("rhs_builders must not be empty")

        if len(comparison_symbols) != len(rhs_builders):
            raise ValueError("comparison_symbols must match rhs_builders length")

        add_header(self, header_text, text_color=self.text_color)

        self.build_expressions(lhs_builder, rhs_builders, comparison_symbols)
        self.fit_expressions()
        self.position_expressions()

    def build_expressions(self, lhs_builder, rhs_builders, comparison_symbols):
        self.lhs = MathTex(*lhs_builder, color=self.text_color)

        self.rhs = VGroup(*[
            MathTex(*step, color=self.text_color)
            for step in rhs_builders
        ])

        self.rhs_prev = VGroup(
            MathTex(*lhs_builder, color=self.text_color),
            *[
                MathTex(*step, color=self.text_color)
                for step in rhs_builders[:-1]
            ]
        )

        self.symbols = VGroup(*[
            MathTex(sym, color=self.text_color)
            for sym in comparison_symbols
        ])

        for i in range(len(self.rhs)):
            if i == 0:
                self.symbols[i].next_to(self.lhs, RIGHT, buff=0.4)

                self.rhs[i].next_to(self.symbols[i], RIGHT, buff=0.4)
                self.rhs[i].align_to(self.lhs, UP)

                self.rhs_prev[i].align_to(self.rhs[i], LEFT)
                self.rhs_prev[i].align_to(self.rhs[i], UP)

            else:
                self.rhs[i].next_to(self.rhs[i - 1], DOWN, aligned_edge=LEFT, buff=0.6)

                self.symbols[i].next_to(self.rhs[i], LEFT, buff=0.4)

                self.rhs_prev[i].align_to(self.rhs[i], LEFT)
                self.rhs_prev[i].align_to(self.rhs[i], UP)

        self.expressions = VGroup(self.lhs, self.symbols, self.rhs, self.rhs_prev)

    def fit_expressions(self):
        max_width = config.frame_width - 1
        max_height = config.frame_height - 2 - self.header_mob.height

        self.expressions.scale_to_fit_height(max_height)

        if self.expressions.width > max_width:
            self.expressions.scale_to_fit_width(max_width)

    def position_expressions(self):
        self.expressions.next_to(
            self.header_mob,
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        )

    def construct(self):
        self.present_expressions()
        self.next_slide()
        self.cleanup()

    def present_expressions(self, run_time=1):
        self.play(Write(self.lhs), run_time=run_time)
        self.next_slide()

        for sym, old_expr, new_expr in zip(self.symbols, self.rhs_prev, self.rhs):
            self.play(Write(sym), run_time=run_time / 2)
            self.play(Write(old_expr), run_time=run_time / 2)
            self.next_slide()

            self.play(
                TransformMatchingTex(old_expr, new_expr),
                run_time=run_time
            )
            self.next_slide()

    def cleanup(self, run_time=1):
        self.play(Unwrite(self.expressions), run_time=run_time)
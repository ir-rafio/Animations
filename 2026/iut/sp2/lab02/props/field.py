from manim import *
import numpy as np

class Field(VGroup):
    def __init__(self, text_color=WHITE, l=12, w=8, a=4.5, b=6, **kwargs):
        super().__init__(**kwargs)

        rect = Polygon(
            [0, 0, 0],
            [l, 0, 0],
            [l, w, 0],
            [0, w, 0],
        ).set_style(
            fill_color=BLUE_B,
            fill_opacity=1,
            stroke_width=0
        )

        tri_points = [
            [0, 0, 0],
            [0, b, 0],
            [a, 0, 0],
        ]

        tri = Polygon(*tri_points).set_style(
            fill_color=GREEN_B,
            fill_opacity=1,
            stroke_width=0
        )

        start = tri_points[2]
        end = tri_points[1]

        semicircle = ArcBetweenPoints(
            start,
            end,
            angle=PI,
        ).set_style(
            fill_color=YELLOW_B,
            fill_opacity=1,
            stroke_width=0
        )

        l_label = MathTex("l", color=text_color).next_to(Line([0, w, 0], [l, w, 0]), UP)
        w_label = MathTex("w", color=text_color).next_to(Line([l, 0, 0], [l, w, 0]), RIGHT)
        a_label = MathTex("a", color=text_color).next_to(Line([0, 0, 0], tri_points[2]), DOWN)
        b_label = MathTex("b", color=text_color).next_to(Line([0, 0, 0], tri_points[1]), LEFT)

        field = VGroup(rect, tri, semicircle, l_label, w_label, a_label, b_label)

        self.add(*field)
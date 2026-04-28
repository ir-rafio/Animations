from manim import *

class StylelessCode(VGroup):
    def __init__(
        self,
        code_file,
        text_color=WHITE,
        line_number_color=GREY,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.code_file = code_file
        self.text_color = text_color
        self.line_number_color = line_number_color

        self.code = Code(
            code_file=code_file,
            background_config={
                "fill_opacity": 0,
                "stroke_color": self.text_color,
            },
            **kwargs
        )

        self.code.set_color(self.text_color)
        self.code.line_numbers.set_color(self.line_number_color)
        self.code.line_numbers.set_color
        self.add(self.code)
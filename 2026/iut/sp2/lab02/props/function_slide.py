from .code_style import *
from .presentation import *

class FunctionSlide(BulletSlide):
    def __init__(self, header_text, points, code_file, intervals, text_color=BLACK, **kwargs):
        super().__init__(
            header_text=header_text,
            text_color=text_color,
            points=points,
            bullet_symbol="",
            **kwargs
        )

        self.intervals = intervals

        self.code = StylelessCode(
            code_file=code_file,
            text_color=text_color
        ).next_to(self.bullets, DOWN, buff=0.4)

    def present_points(self, run_time=1):
        super().present_points(run_time=run_time)

        frame = self.code.code.background
        line_numbers = self.code.code.line_numbers
        code_lines = self.code.code.code_lines

        self.play(Create(frame), FadeIn(line_numbers), run_time=run_time)
        self.next_slide()

        for interval in self.intervals:
            lines_group = VGroup(*[code_lines[i - 1] for i in interval]) # IndexError: list index out of range, interval contains a list of line numbers
            self.play(Write(lines_group), run_time=run_time)
            self.next_slide()

    def cleanup(self, run_time=1):
        self.play(
            *[Unwrite(b) for b in self.bullets],
            Uncreate(self.side),
            Uncreate(self.code),
            run_time=run_time
        )
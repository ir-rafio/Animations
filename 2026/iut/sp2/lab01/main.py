from manim import *
from manim_slides import Slide
from props.presentation import *

class TitleSlide(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title = r"Title\\Slide",
            **kwargs
        )

class Introduction(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Introduction",
            text_color=BLACK,
            points = [
                r"Computers use binary as their fundamental language.",
                r"All data in a computer (numbers, text, images, audio \& video, programs, even the entire internet) is represented using bits.",
                r"Although a single bit can only represent two states (ON/OFF), complex information can be represented using sequences of bits.",
                r"For representing complex information, all users must agree upon some standards.",
                r"Numbers are represented using a positional number system.",
                r"Special techniques enable representation of negative numbers.",
                r"Bitwise operators are operators that operate on individual bits of a number."
            ],
            **kwargs
        )

class TableOfContents(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Table of Contents",
            text_color=BLACK,
            points = [
                r"Binary Number System",
                r"Signed Number Representation",
                r"Bitwise Operators",
                r"Applications",
            ],
            **kwargs
        )
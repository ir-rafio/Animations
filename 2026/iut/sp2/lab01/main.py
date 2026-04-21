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

class Section_BinaryNumberSystem(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Binary\\Number\\System",
            **kwargs
        )

class BinaryNumberSystem(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Binary Number System",
            text_color=BLACK,
            points = [
                r"Binary number system is a positional number system with a \textbf{base} of $2$.",
                r"It uses $2$ symbols: $0$ and $1$. $0$ represents \texttt{OFF} and $1$ represents \texttt{ON}.",
                r"Each position of a binary number has a different \textbf{positional weight or significance}.",
                r"Binary number system provides a \textbf{one-to-one mapping} between numbers and sequences of bits.",
                r"For $n$ bits, there are $2^n$ \textbf{different bit sequences} which can represent $2^n$ \textbf{different numbers}.",
                r"For example, with $4$ bits, $16$ different numbers can be represented."
            ],
            **kwargs
        )
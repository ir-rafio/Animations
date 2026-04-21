from manim import *
from manim_slides import Slide
from props.presentation import *
from props.digitbox import *

colors = [
    GREEN_E,
    YELLOW,
    BLUE_E,
    RED_A,
    PURPLE_E,
    TEAL_A,
    DARK_BROWN,
    ORANGE
]

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

class DisplaySequences(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Binary Number System",
            text_color=BLACK,
            points = [rf"${i:04b}$" for i in range(16)],
            bullet_symbol = r"$? \rightarrow$",
            **kwargs
        )

    def present_points(self, run_time=1):
        self.play(Create(self.bullets), run_time=run_time)
    
class DecimalSymbols(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        add_header(self, "Binary Number System", BLACK)

        symbols_text = Text("Symbols in Base-10", color=BLACK)
        symbols_text.scale_to_fit_height(1)
        symbols_text.next_to(self.header_underline, DOWN, buff=0.5)
        symbols_text.align_to(self.header_underline, LEFT)

        symbols_group = VGroup()
        for i in range(10):
            box = DigitBox(
                base=10,
                value=i,
                height=1,
                bubble_color=colors[0],
                bubble_layout=GridLayout(9),
                dot_layout=None,
                stroke_color=BLACK
            )
            digit = DecimalNumber(i, num_decimal_places=0, color=BLACK)
            digit.scale_to_fit_height(1)

            digit_group = VGroup(box, digit)
            digit_group.arrange(RIGHT, buff=0.25)
            symbols_group.add(digit_group)
        
        symbols_group.arrange_in_grid(cols=5, buff=(0.75, 1))
        symbols_group.next_to(symbols_text, DOWN, buff=1)
        symbols_group.align_to(symbols_text, LEFT)

        self.play(Create(symbols_text), Create(symbols_group))

        self.next_slide()

        self.play(Uncreate(symbols_group), Uncreate(symbols_text))
        self.wait()
    
class DecimalCounting(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        add_header(self, "Binary Number System", BLACK)
        
        nb = NumberBox(
            n=3,
            base=10,
            value=0,
            height=2,
            colors=colors[:3],
            stroke_color=BLACK
        )
        nb.next_to(self.header_underline, DOWN, 0.5)

        self.play(FadeIn(nb))
        self.next_slide()

        for _ in range(12):
            self.play(nb.animate.increment())
            self.next_slide()

        self.play(nb.animate_to_value(19))
        self.next_slide()

        self.play(nb.animate.increment())
        self.next_slide()

        self.play(nb.animate_to_value(99))
        self.next_slide()

        self.play(nb.animate.increment())
        self.next_slide()

        self.play(nb.animate.increment())
        self.next_slide()

        self.play(nb.animate_to_value(125))
        self.next_slide(loop=True)

        self.play(Indicate(nb.weights))
        self.next_slide()

        self.play(nb.animate_to_value(354))
        self.next_slide()

        self.play(FadeOut(nb))
        self.wait()

class DecimalPositions(MathExpansionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Binary Number System",
            lhs_builder=["3", "5", "4"],
            rhs_builders=[
                [
                    "3", r"\times", "100", "+",
                    "5", r"\times", "10", "+",
                    "4"
                ],
                [
                    "3", "00", "+", "5", "0", "+", "4"
                ],
                [
                    "3", "5", "4"
                ]
            ],
            comparison_symbols=[
                r"\rightarrow",
                "=",
                "="
            ],
            text_color=BLACK,
            **kwargs
        )
    
class BinaryCounting(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        add_header(self, "Binary Number System", BLACK)
        
        base = 2
        bubble_layout = GridLayout(base - 1)

        nb = NumberBox(
            n=4,
            base=base,
            value=0,
            height=2,
            colors=colors[:4],
            bubble_layout=bubble_layout,
            dot_layout=RadialLayout(2, angle_offsets=[PI / 4]),
            stroke_color=BLACK,
            show_leading_zeroes=True
        )
        nb.to_edge(LEFT)

        symbols_text = Text("Symbols", color=BLACK)
        symbols_text.scale_to_fit_height(1)
        symbols_text.next_to(self.header_underline, DOWN, buff=0.5)
        symbols_text.align_to(self.header_underline, RIGHT)

        symbols_group = VGroup()
        for i in range(2):
            box = DigitBox(
                base=base,
                value=i,
                height=1.5,
                bubble_color=colors[0],
                bubble_layout=bubble_layout,
                dot_layout=None,
                stroke_color=BLACK
            )
            digit = DecimalNumber(i, num_decimal_places=0, color=BLACK)
            digit.scale_to_fit_height(1)

            digit_group = VGroup(box, digit)
            digit_group.arrange(RIGHT, buff=0.5)
            symbols_group.add(digit_group)
        
        symbols_group.arrange(DOWN, buff=0.5)
        symbols_group.next_to(symbols_text, DOWN, buff=0.5)
        symbols_group.align_to(symbols_text, RIGHT)

        self.play(Create(symbols_text), Create(symbols_group))

        self.next_slide()

        self.play(FadeIn(nb))
        self.next_slide()

        for _ in range(15):
            self.play(nb.animate.increment())
            self.next_slide()

        self.play(FadeOut(nb), Uncreate(symbols_group), Uncreate(symbols_text))
        self.wait()

class BinaryPositions(MathExpansionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Binary Number System",
            lhs_builder=["1", "1", "0", "1"],
            rhs_builders=[
                [
                    "1", r"\times", "8", "+",
                    "1", r"\times", "4", "+",
                    "0", r"\times", "2", "+",
                    "1"
                ],
                [
                    "8", "+", "4", "+", "1"
                ],
                [
                    "13"
                ]
            ],
            comparison_symbols=[
                r"\rightarrow",
                "=",
                "="
            ],
            text_color=BLACK,
            **kwargs
        )

class DisplayUnsigned(BulletSlide):
    def __init__(self, bits, show_all=False, **kwargs):

        self.bits = bits
        self.show_all = show_all

        max_val = 2**bits - 1

        if show_all:
            points = [
                rf"${i} \rightarrow {i:0{bits}b}$"
                for i in range(2**bits)
            ]
        else:
            points = (
                [rf"${i} \rightarrow {i:0{bits}b}$" for i in range(3)] +
                [r"$\dots$"] +
                [r"$\dots$"] +
                [rf"${i} \rightarrow {i:0{bits}b}$" for i in range(max_val - 2, max_val + 1)]
            )

        super().__init__(
            header_text=f"Binary Number System -- {bits} Bits",
            text_color=BLACK,
            points = points,
            bullet_symbol = "",
            **kwargs
        )

    def present_points(self, run_time=1):
        self.play(Create(self.bullets), run_time=run_time)

class DisplayUnsigned4(DisplayUnsigned):
    def __init__(self, **kwargs):
        super().__init__(bits=4, show_all=True, **kwargs)

class DisplayUnsigned8(DisplayUnsigned):
    def __init__(self, **kwargs):
        super().__init__(bits=8, show_all=False, **kwargs)

class DisplayUnsigned16(DisplayUnsigned):
    def __init__(self, **kwargs):
        super().__init__(bits=16, show_all=False, **kwargs)

class DisplayUnsigned32(DisplayUnsigned):
    def __init__(self, **kwargs):
        super().__init__(bits=32, show_all=False, **kwargs)

class DisplaySigned(BulletSlide):
    def __init__(self, bits, show_all=False, **kwargs):

        self.bits = bits
        self.show_all = show_all

        min_val = -(2 ** (bits - 1))
        max_val = (2 ** (bits - 1)) - 1

        def fmt(i):
            if i >= 0:
                return rf"${i} \rightarrow {i:0{bits}b}$"
            return rf"${i} \rightarrow {format((1 << bits) + i, f'0{bits}b')}$"

        if show_all:
            points = [
                fmt(i)
                for i in range(min_val, max_val + 1)
            ]
        else:
            start = [fmt(i) for i in range(min_val, min_val + 2)]

            middle = [fmt(-1), fmt(0)]

            end = [fmt(i) for i in range(max_val - 1, max_val + 1)]

            points = (
                start +
                [r"$\dots$"] +
                [r"$\dots$"] +
                middle +
                [r"$\dots$"] +
                [r"$\dots$"] +
                end
            )

        super().__init__(
            header_text=f"Signed Number Representation -- {bits} Bits",
            text_color=BLACK,
            points = points,
            bullet_symbol = "",
            **kwargs
        )

    def present_points(self, run_time=1):
        self.play(Create(self.bullets), run_time=run_time)

class DisplaySigned4(DisplaySigned):
    def __init__(self, **kwargs):
        super().__init__(bits=4, show_all=True, **kwargs)

class DisplaySigned8(DisplaySigned):
    def __init__(self, **kwargs):
        super().__init__(bits=8, show_all=False, **kwargs)

class DisplaySigned16(DisplaySigned):
    def __init__(self, **kwargs):
        super().__init__(bits=16, show_all=False, **kwargs)

class DisplaySigned32(DisplaySigned):
    def __init__(self, **kwargs):
        super().__init__(bits=32, show_all=False, **kwargs)

class Section_SignedRepresentation(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Signed\\Number\\Representation",
            **kwargs
        )

class SignedRepresentation1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Signed Number Representation",
            text_color=BLACK,
            points = [
                r"Computers need to work with negative numbers.",
                r"In \textbf{unsigned} variables, all bits are used to represent the \textbf{magnitude} (absolute value) of a number.",
                r"In signed variables, a \textbf{sign bit} (the leftmost bit) is reserved to represent the sign of a number.",
                r"If the sign bit of a number is $0$, it is \textbf{non-negative}. And if the sign bit is $1$, it is negative.",
            ],
            **kwargs
        )

class SignedRepresentation2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Signed Number Representation",
            text_color=BLACK,
            points = [
                r"One of the sequences for non-negative numbers is used by $0$. So, with a fixed number of bits, the number of different negative numbers that can be represented is \textbf{one more than} the number of different positive numbers.",
                r"For example, with $4$ bits, $16$ different numbers can be represented. In signed representation, $8$ of them are negative, $7$ of them are positive, and $1$ of them is $0$.",
                r"An effective representation of negative numbers should be consistent with arithmetic operations (addition, subtraction, $\dots$)."
            ],
            **kwargs
        )
        
class DiscoverNegatives(DisplaySigned4):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.nxt_note = VGroup(
            Tex(
                r"Result of going to the \textbf{next} number (adding $1$) in binary:",
                font_size=32,
                color=self.text_color
            ),
            Tex(r"-- Trailing $1$s become $0$.", font_size=32, color=self.text_color),
            Tex(r"-- The next $0$ becomes $1$.", font_size=32, color=self.text_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.nxt_note.next_to(self.bullets, RIGHT, aligned_edge=UP, buff=0.8)

        self.prv_note = VGroup(
            Tex(
                r"Result of going to the \textbf{previous} number (subtracting $1$) in binary:",
                font_size=32,
                color=self.text_color
            ),
            Tex(r"-- Trailing $0$s become $1$.", font_size=32, color=self.text_color),
            Tex(r"-- The next $1$ becomes $0$.", font_size=32, color=self.text_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.prv_note.align_to(self.nxt_note, LEFT)
        self.prv_note.to_edge(DOWN)

    def present_points(self, run_time=1):
        positives = VGroup(*[b.copy() for b in self.bullets[8:]])

        first_part = positives[:5]
        last_part = positives[5:]

        for bullet in first_part:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Write(self.nxt_note), run_time=run_time)
        self.next_slide()

        self.play(Write(VGroup(*last_part)), run_time=run_time)
        self.next_slide()

        self.play(Unwrite(positives), run_time=run_time)
        self.next_slide()

        reversed_bullets = list(reversed(self.bullets))

        first_rev = reversed_bullets[:5]
        middle_rev = reversed_bullets[5:10]
        last_rev = reversed_bullets[10:]

        for bullet in first_rev:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Write(self.prv_note), run_time=run_time)
        self.next_slide()

        for bullet in middle_rev:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Write(VGroup(*last_rev)), run_time=run_time)
        self.next_slide()
    
    def cleanup(self, run_time=1):
      self.play(
          Unwrite(self.bullets),
          Unwrite(self.nxt_note),
          Unwrite(self.prv_note),
          run_time=run_time
      )

class BinaryComplement(BulletSlide):
    def __init__(self, **kwargs):
        points = [
            r"Notice the divider line between the negative and non-negative numbers.",
            r"Each pair of numbers that are at the same distance from this divider are \textbf{complement numbers}.",
            r"The complement of a number $x$ is denoted as $\mathord{\sim}x$.",
            r"Notice that the complement of a number can be obtained by replacing all $1$s with $0$s and vice versa.",
            r"Notice that $0$ is on one side of the divider, not on the divider. Because of this, $\mathord{\sim}x \ne -x$.",
            r"Since the divider is just above $0$, $\mathord{\sim}x = -x - 1$. So, $-x = \mathord{\sim}x + 1$.",
            r"Another way to think about it:\\ If you add $x$ and $\mathord{\sim}x$, you get all $1$s, which is $-1$.",
            r"So, $x + \mathord{\sim}x = -1$, thus $\mathord{\sim}x = -1 - x$ and $-x = \mathord{\sim}x + 1$."
        ]

        super().__init__(
            header_text="Signed Number Representation",
            text_color=BLACK,
            points=points,
            **kwargs
        )

        self._build_number_bullets()
        self._setup_point_bullets()

        self._position_number_bullets()
        self._fit_point_bullets()
        self._position_point_bullets()

        self._create_divider()

    def fit_points_in_frame(self):
        pass

    def _build_number_bullets(self):
        bits = 4
        min_val = -(2 ** (bits - 1))
        max_val = (2 ** (bits - 1)) - 1

        def fmt(i):
            if i >= 0:
                return rf"${i} \rightarrow {i:0{bits}b}$"
            return rf"${i} \rightarrow {format((1 << bits) + i, f'0{bits}b')}$"

        self.number_bullets = VGroup(*[
            Tex(fmt(i), color=self.text_color)
            for i in range(min_val, max_val + 1)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        max_height = config.frame_height - 2 - self.header_mob.height
        if self.number_bullets.height > max_height:
            self.number_bullets.scale_to_fit_height(max_height)

    def _setup_point_bullets(self):
        self.point_bullets = self.bullets

    def _position_number_bullets(self):
        self.number_bullets.next_to(
            self.header_mob,
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        )

    def _fit_point_bullets(self):
        total_width = config.frame_width - 2
        left_w = self.number_bullets.width
        available_right = total_width - left_w - 1

        if self.point_bullets.width > available_right:
            self.point_bullets.scale_to_fit_width(available_right)

        max_height = config.frame_height - 2 - self.header_mob.height
        if self.point_bullets.height > max_height:
            self.point_bullets.scale_to_fit_height(max_height)

    def _position_point_bullets(self):
        self.point_bullets.next_to(
            self.number_bullets,
            RIGHT,
            aligned_edge=UP,
            buff=1
        )

    def _create_divider(self):
        top = self.number_bullets[7].get_bottom()
        bottom = self.number_bullets[8].get_top()

        y = (top + bottom) / 2

        left = self.number_bullets.get_left()
        right = self.number_bullets.get_right()

        self.divider = Line(
            [left[0], y[1], 0],
            [right[0], y[1], 0],
            color=BLACK
        )
    
    def present_points(self, run_time=1):
        self.play(Create(self.number_bullets), run_time=run_time)
        self.next_slide(auto_next=True)

        self.play(Create(self.divider), run_time=run_time)
        self.next_slide()

        self.play(Write(self.point_bullets[0]), run_time=run_time)
        self.next_slide(auto_next=True)

        self.play(Write(self.point_bullets[1]), run_time=run_time)
        self.next_slide(loop=True)

        for i in range(8):
            self.play(
                Indicate(self.number_bullets[7 - i]),
                Indicate(self.number_bullets[8 + i]),
                run_time=0.5
            )

        self.next_slide()

        for bullet in self.point_bullets[2:]:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

    def cleanup(self, run_time=1):
        self.play(
            Unwrite(self.number_bullets),
            Unwrite(self.point_bullets),
            Uncreate(self.divider),
            run_time=run_time
        )
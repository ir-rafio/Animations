from manim import *
from manim_slides import Slide
from props.presentation import *
from props.digitbox import *
from props.academia import *
from lab_info import *

sans_template = TexTemplate()
sans_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
Tex.set_default(tex_template=sans_template)

class Title_Bits(TitleSlide):
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
            points = [
                r"Computers use binary as their fundamental language.",
                r"All data in computers (numbers, text, images, audio \& video, programs, even the entire internet) is represented using bits.",
                r"Although a single bit can only represent two states (ON/OFF), complex information can be represented using sequences of bits.",
                r"For representing complex information, all users must agree upon some standards.",
                r"Numbers are represented using a positional number system.",
                r"Special techniques enable representation of negative numbers.",
                r"Bitwise operators are operators that operate on individual bits of a number."
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
                r"Binary Number System",
                r"Signed Number Representation",
                r"Bitwise Operators",
                r"Applications",
            ],
            **kwargs
        )

        add_footer(self)

class Section_BinaryNumberSystem(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Binary\\Number\\System",
            **kwargs
        )

        add_footer(self)

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

        add_footer(self)

class DisplaySequences(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Binary Number System",
            text_color=BLACK,
            points = [rf"${i:04b}$" for i in range(16)],
            bullet_symbol = r"$? \rightarrow$",
            **kwargs
        )

        add_footer(self)

    def present_points(self, run_time=1):
        self.play(Create(self.bullets), run_time=run_time)
    
class DecimalSymbols(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        add_header(self, "Binary Number System", BLACK)
        add_footer(self)

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
                bubble_color=GREEN,
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
        add_footer(self)

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
        
        add_footer(self)
    
class BinaryCounting(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        add_header(self, "Binary Number System", BLACK)
        add_footer(self)

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
        
        add_footer(self)

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
        
        add_footer(self)

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
        
        add_footer(self)

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
        
        add_footer(self)

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
        
        add_footer(self)

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
        
        add_footer(self)
        
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

        self.prv_note.next_to(self.nxt_note, DOWN, buff=1, aligned_edge=LEFT)
        
        add_footer(self)

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
            r"Another way to think about it:\\ If you add $x$ and $\mathord{\sim}x$, you get all $1$s, which is $-1$.\\ So, $x + \mathord{\sim}x = -1$, thus $\mathord{\sim}x = -1 - x$ and $-x = \mathord{\sim}x + 1$."
        ]

        super().__init__(
            header_text="Signed Number Representation",
            text_color=BLACK,
            points=points,
            **kwargs
        )
        
        add_footer(self)

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

class Section_BitwiseOperators(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Bitwise\\Operators",
            **kwargs
        )
        
        add_footer(self)

class BitwiseOperators(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Bitwise Operators",
            text_color=BLACK,
            points = [
                r"Bitwise operators are operators that operate on \textbf{individual bits} of an integer.",
                r"Each bit is processed \textbf{independently} (the result of one bit does not affect other bits).",
                r"Bitwise operators treat integer variables like \textbf{boolean arrays}.",
                r"Bitwise operators directly map to low-level hardware operations and are extremely fast.",
                r"In C, the bitwise operators are:\\ \texttt{\&} (AND), \texttt{|} (OR), \texttt{\^} (XOR), \texttt{\textasciitilde} (NOT), \texttt{<<} (left shift), and \texttt{>>} (right shift)."
            ],
            **kwargs
        )
        
        add_footer(self)

class BitwiseOR(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Bitwise Operators --- OR (\texttt{|})",
            text_color=BLACK,
            points = [
                r"Bitwise OR is a binary operator that operates on two integers by applying the OR operation to each pair of corresponding bits.",
                r"The $i$-th bit of the output depends only on the $i$-th bits of the inputs.",
                r"The $i$-th bit of the output is $1$ if \textbf{at least one} of the corresponding input bits is $1$.",
                r"Truth table: $0 \texttt{|} 0 = 0,\; 0 \texttt{|} 1 = 1,\; 1 \texttt{|} 0 = 1,\; 1 \texttt{|} 1 = 1$",
                r"Bitwise OR (\texttt{|}) should not be confused with logical OR (\texttt{||}). For example, $5 \texttt{|} 6 = 7$, but $5 \texttt{||} 6 = 1$."
            ],
            **kwargs
        )
        
        add_footer(self)


class BitwiseAND(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Bitwise Operators --- AND (\texttt{\&})",
            text_color=BLACK,
            points = [
                r"Bitwise AND is a binary operator that operates on two integers by applying the AND operation to each pair of corresponding bits.",
                r"The $i$-th bit of the output depends only on the $i$-th bits of the inputs.",
                r"The $i$-th bit of the output is $1$ if \textbf{both} corresponding input bits are $1$.",
                r"Truth table: $0 \texttt{\&} 0 = 0,\; 0 \texttt{\&} 1 = 0,\; 1 \texttt{\&} 0 = 0,\; 1 \texttt{\&} 1 = 1$",
                r"Bitwise AND (\texttt{\&}) should not be confused with logical AND (\texttt{\&\&}). For example, $5 \texttt{\&} 6 = 4$, but $5 \texttt{\&\&} 6 = 1$."
            ],
            **kwargs
        )
        
        add_footer(self)


class BitwiseXOR(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Bitwise Operators --- XOR (\texttt{\^{}})",
            text_color=BLACK,
            points = [
                r"Bitwise XOR is a binary operator that operates on two integers by applying the XOR operation to each pair of corresponding bits.",
                r"The $i$-th bit of the output depends only on the $i$-th bits of the inputs.",
                r"The $i$-th bit of the output is $1$ if \textbf{an odd number of} corresponding input bits are $1$.",
                r"Another way to think about it:\\ The $i$-th bit of the output is $1$ if the corresponding input bits are \textbf{different}.",
                r"Truth table: $0 \texttt{\^{}} 0 = 0,\; 0 \texttt{\^{}} 1 = 1,\; 1 \texttt{\^{}} 0 = 1,\; 1 \texttt{\^{}} 1 = 0$",
                r"\textbf{Cool Trick}: Applying XOR with $32$ changes the case of a character (converts an uppercase character to lowercase and vice versa)."
            ],
            **kwargs
        )
        
        add_footer(self)

class BitwiseNOT(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Bitwise Operators --- NOT (\texttt{\textasciitilde})",
            text_color=BLACK,
            points = [
                r"Bitwise NOT is a unary operator that flips each bit of a number.",
                r"It changes every $0$ to $1$ and every $1$ to $0$.",
                r"For signed integers, the result of Bitwise NOT is the \textbf{binary complement} of the number.",
                r"Bitwise NOT works on both signed and unsigned integers.",
                r"Bitwise NOT (\texttt{\textasciitilde}) should not be confused with logical NOT (\texttt{!})."
            ],
            **kwargs
        )
        
        add_footer(self)

class BitwiseShift(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Bitwise Operators --- Shift (\texttt{<<}, \texttt{>>})",
            text_color=BLACK,
            points = [
                r"Bitwise shift operators move the bits of a number left or right.",
                r"Left shift (\texttt{<<}) shifts all bits to the left and fills the empty right bits with $0$.",
                r"Right shift (\texttt{>>}) shifts all bits to the right and removes the rightmost bits.",
                r"Shifting left by $n$ bits multiplies the number by $2^n$.",
                r"Shifting right by $n$ bits divides the number by $2^n$ (discarding remainder).",
            ],
            **kwargs
        )
        
        add_footer(self)

class BitwiseOperatorDemo(Slide):
    def __init__(self, operator_name, op_func, op_sym, text_color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        self.operator_name = operator_name
        self.op_func = op_func
        self.op_sym = op_sym
        self.text_color = text_color

        self.num_bits = 8
        self.value_a = 5
        self.value_b = 6

        add_header(self, f"Bitwise Operators --- {self.operator_name}", text_color=self.text_color)
        add_footer(self)

        self._build_operands()
        self._build_truth_table()
        self._arrange_layout()

    def _build_operands(self):
        self.label_a = self._create_label(str(self.value_a))
        self.label_b = self._create_label(str(self.value_b))
        self.label_result = self._create_label("?", is_math=True)

        self.bits_a = self._create_bits(self.value_a)
        self.bits_b = self._create_bits(self.value_b)
        self.bits_result = self._create_placeholder_bits()

        self.bit_weights = self._create_weights()

        self.operands_group = VGroup(
            self.bit_weights,
            self._pair_label_bits(self.label_a, self.bits_a),
            self._pair_label_bits(self.label_b, self.bits_b),
            self._pair_label_bits(self.label_result, self.bits_result),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)

        self._align_columns()

    def _build_truth_table(self):
        raw_cells = [
            "A", "B", f"A {self.op_sym} B",
            0, 0, self.op_func(0, 0),
            0, 1, self.op_func(0, 1),
            1, 0, self.op_func(1, 0),
            1, 1, self.op_func(1, 1),
        ]

        self.truth_table = VGroup(*[
            Tex(str(x), color=self.text_color) for x in raw_cells
        ]).arrange_in_grid(cols=3, buff=0.4)

    def _create_label(self, value, is_math=False):
        value_tex = Tex(f"${value}$" if is_math else value, color=self.text_color)
        arrow = Tex(r"$\rightarrow$", color=self.text_color)
        return VGroup(value_tex, arrow).arrange(RIGHT, buff=1)

    def _pair_label_bits(self, label, bits):
        return VGroup(label, bits).arrange(RIGHT, buff=1)

    def _create_bits(self, number):
        bit_string = format(number, f"0{self.num_bits}b")
        return VGroup(*[
            Tex(bit, color=self.text_color) for bit in bit_string
        ]).arrange(RIGHT, buff=0.6)

    def _create_placeholder_bits(self):
        return VGroup(*[
            Tex("$?$", color=self.text_color) for _ in range(self.num_bits)
        ]).arrange(RIGHT, buff=0.6)

    def _create_weights(self):
        weights = []
        for i in range(self.num_bits - 1, -1, -1):
            value = 2 ** i
            label = str(value) if value <= 8 else rf"$2^{i}$"
            weights.append(Tex(label, color=GREY))
        return VGroup(*weights).arrange(RIGHT, buff=0.2)

    def _align_columns(self):
        for weight, bit_a, bit_r in zip(self.bit_weights, self.bits_a, self.bits_result):
            weight.align_to(bit_a, LEFT)
            bit_r.align_to(bit_a, RIGHT)

    def _arrange_layout(self):
        self.operands_group.next_to(self.header_mob, DOWN, aligned_edge=LEFT, buff=0.8)

        self.truth_table.next_to(self.header_mob, DOWN, buff=0.8)
        self.truth_table.align_to(self.header_underline, RIGHT)

    def construct(self):
        self.play(Create(self.truth_table))
        self.next_slide()

        self.play(Write(self.operands_group))
        self.next_slide()

        self._animate_bitwise_operation()
        self.next_slide()

        result_value = self.op_func(self.value_a, self.value_b)

        self.play(
            Transform(
                self.label_result[0],
                Tex(str(result_value), color=self.text_color).move_to(self.label_result[0])
            ),
            run_time=0.8
        )

        self.next_slide()

        self.play(
            Unwrite(self.operands_group),
            Uncreate(self.truth_table),
            run_time=1
        )
        self.next_slide()

    def _animate_bitwise_operation(self):
        result_value = self.op_func(self.value_a, self.value_b)
        result_bits = format(result_value, f"0{self.num_bits}b")

        for i in range(self.num_bits):
            idx = self.num_bits - 1 - i

            self.play(
                Indicate(self.bits_a[idx]),
                Indicate(self.bits_b[idx]),
                run_time=0.4
            )

            self.play(
                Transform(
                    self.bits_result[idx],
                    Tex(result_bits[idx], color=self.text_color).move_to(self.bits_result[idx])
                ),
                run_time=0.2
            )

            if(i < self.num_bits / 2): self.next_slide()

class DemoOR(BitwiseOperatorDemo):
    def __init__(self, **kwargs):
        super().__init__(
            operator_name="OR",
            op_func=lambda a, b: a | b,
            op_sym=r"\texttt{|}",
            text_color=BLACK,
            **kwargs
        )

class DemoAND(BitwiseOperatorDemo):
    def __init__(self, **kwargs):
        super().__init__(
            operator_name="AND",
            op_func=lambda a, b: a & b,
            op_sym=r"\texttt{\&}",
            text_color=BLACK,
            **kwargs
        )

class DemoXOR(BitwiseOperatorDemo):
    def __init__(self, **kwargs):
        super().__init__(
            operator_name="XOR",
            op_func=lambda a, b: a ^ b,
            op_sym=r"\texttt{\^{}}",
            text_color=BLACK,
            **kwargs
        )

class BitwiseShiftDemo(Slide):
    def __init__(self, operator_name, op_func, op_sym, text_color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        self.operator_name = operator_name
        self.op_func = op_func
        self.op_sym = op_sym
        self.text_color = text_color

        self.num_bits = 8
        self.value_a = 25
        self.shift_amount = 2
        self.result_value = self.op_func(self.value_a, self.shift_amount)

        add_header(self, f"Bitwise Operators --- {self.operator_name}", text_color=self.text_color)
        add_footer(self)

        self._build_expression()
        self._build_bit_rows()
        self._arrange_layout()

    def _build_expression(self):
        self.expression_intro = Tex(
            rf"Let $x = {self.value_a} {self.op_sym} {self.shift_amount}$",
            color=self.text_color
        )

        self.expression_result = Tex(
            rf"So, $x = {self.result_value}$",
            color=self.text_color
        )

    def _build_bit_rows(self):
        self.label_a = self._create_label(str(self.value_a))
        self.label_x = self._create_label(
            rf"{self.value_a} {self.op_sym} {self.shift_amount}",
            is_math=True
        )

        self.bits_a_buffer = self._create_buffered_bits(self.value_a)
        self.bits_shift_stage1 = self._create_buffered_bits(self.value_a)

        if self.op_sym == "<<":
            self.bits_shift_stage2 = self._create_left_shift_bits(self.value_a)
        else:
            self.bits_shift_stage2 = self._create_right_shift_bits(self.value_a)

        self.bits_final_buffer = self._create_buffered_bits(self.result_value)

        self.bits_a_visible = self.bits_a_buffer[2:10]
        self.bits_x_visible = self.bits_shift_stage1[2:10]

        self.bit_weights = self._create_weights()

        self.layout_group = VGroup(
            self.bit_weights,
            VGroup(self.label_a, self.bits_a_buffer).arrange(RIGHT, buff=0.8),
            VGroup(self.label_x, self.bits_shift_stage1).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.8)

        for w, bit in zip(self.bit_weights, self.bits_a_visible):
            w.align_to(bit, LEFT)

        self.visible_group = VGroup(
            self.bit_weights,
            self.label_a,
            self.bits_a_visible,
            self.label_x,
            self.bits_x_visible
        )

    def _create_label(self, text, is_math=False):
        value = Tex(rf"${text}$" if is_math else text, color=self.text_color)
        arrow = Tex(r"$\rightarrow$", color=self.text_color)
        return VGroup(value, arrow).arrange(RIGHT, buff=1)

    def _create_buffered_bits(self, number):
        bit_string = format(number, f"0{self.num_bits}b")
        padded = [""] * 2 + list(bit_string) + [""] * 2

        return VGroup(*[
            Tex(b if b else "-", color=self.text_color)
            for b in padded
        ]).arrange(RIGHT, buff=0.6)

    def _create_left_shift_bits(self, number):
        bit_string = format(number, f"0{self.num_bits}b")
        padded = list(bit_string) + [""] * 4

        return VGroup(*[
            Tex(b if b else "-", color=self.text_color)
            for b in padded
        ]).arrange(RIGHT, buff=0.6)

    def _create_right_shift_bits(self, number):
        bit_string = format(number, f"0{self.num_bits}b")
        padded = [""] * 4 + list(bit_string)

        return VGroup(*[
            Tex(b if b else "-", color=self.text_color)
            for b in padded
        ]).arrange(RIGHT, buff=0.6)

    def _create_weights(self):
        weights = []
        for i in range(self.num_bits - 1, -1, -1):
            value = 2 ** i
            label = str(value) if value <= 8 else rf"$2^{i}$"
            weights.append(Tex(label, color=GREY))
        return VGroup(*weights)

    def _arrange_layout(self):
        self.expression_intro.next_to(self.header_mob, DOWN, aligned_edge=LEFT, buff=0.8)
        self.layout_group.next_to(self.expression_intro, DOWN, aligned_edge=LEFT, buff=0.8)

        for i in range(len(self.bits_a_buffer)):
            self.bits_shift_stage2[i].align_to(self.bits_a_buffer[i], RIGHT)
            self.bits_final_buffer[i].align_to(self.bits_a_buffer[i], RIGHT)

            self.bits_shift_stage2[i].align_to(self.label_x, DOWN)
            self.bits_final_buffer[i].align_to(self.label_x, DOWN)

        self.expression_result.next_to(self.layout_group, DOWN, aligned_edge=LEFT, buff=0.8)

    def construct(self):
        self.play(Write(self.expression_intro))
        self.next_slide()

        self.play(Create(self.visible_group))
        self.next_slide()

        if self.op_sym == "<<":
            self.play(Transform(self.bits_x_visible, self.bits_shift_stage2[:-4]))
        else:
            self.play(Transform(self.bits_x_visible, self.bits_shift_stage2[4:]))
        self.next_slide()

        if self.op_sym == "<<":
            discarded = self.bits_x_visible[:2]
            self.bits_x_visible = self.bits_x_visible[2:]
            filled = self.bits_final_buffer[-4:-2]
        else:
            discarded = self.bits_x_visible[-2:]
            self.bits_x_visible = self.bits_x_visible[:-2]
            filled = self.bits_final_buffer[2:4]

        self.play(Indicate(discarded), run_time=0.5)
        self.play(FadeOut(discarded), run_time=0.5)
        self.next_slide()

        self.play(Write(filled))
        self.next_slide()

        self.play(Write(self.expression_result))
        self.next_slide()

        self.play(
            FadeOut(self.expression_intro),
            FadeOut(self.expression_result),
            FadeOut(self.label_a),
            FadeOut(self.label_x),
            FadeOut(self.bit_weights),
            FadeOut(self.bits_a_visible),
            FadeOut(self.bits_x_visible),
            FadeOut(filled),
            run_time=1
        )

class DemoLSHIFT(BitwiseShiftDemo):
    def __init__(self, **kwargs):
        super().__init__(
            operator_name="Left Shift",
            op_func=lambda a, b: a << b,
            op_sym="<<",
            text_color=BLACK,
            **kwargs
        )

class DemoRSHIFT(BitwiseShiftDemo):
    def __init__(self, **kwargs):
        super().__init__(
            operator_name="Right Shift",
            op_func=lambda a, b: a >> b,
            op_sym=">>",
            text_color=BLACK,
            **kwargs
        )

class Section_Applications(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Applications",
            **kwargs
        )
        
        add_footer(self)

class Bitmasks(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Applications --- Bitmasks",
            text_color=BLACK,
            points=[
                r"A bitmask is a sequence of bits with a specific pattern used to control or extract data from integers.",
                r"Bitmasks take advantage of different properties of bitwise operators.",
                r"For example, if one of the bits in an AND operation is $0$, the result is $0$ regardless of the other bit.",
                r"If one of the bits in an AND operation is $1$, the result copies the other bit."
            ],
            **kwargs
        )
        
        add_footer(self)

class Subsets(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Applications --- Subsets",
            text_color=BLACK,
            points=[
                r"A set of $n$ elements has $2^n$ subsets.",
                r"Each subset can be represented using a bitmask of $n$ bits, where each bit corresponds to an element in the set.",
                r"If the $i$-th bit of a bitmask is $0$, the $i$-th element is not included in the subset.",
                r"If the $i$-th bit of a bitmask is $1$, the $i$-th element is included in the subset.",
                r"Each subset corresponds to an integer from $0$ to $(2^n - 1)$.",
                r"If $a$ and $b$ are the bitmasks representing the sets $A$ and $B$, then $a \texttt{|} b$ will be the bitmask representing $A \cup B$.",
                r"If $a$ and $b$ are the bitmasks representing the sets $A$ and $B$, then $a \texttt{\&} b$ will be the bitmask representing $A \cap B$."
            ],
            **kwargs
        )
        
        add_footer(self)

class Problem_BinaryOf2025(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Applications",
            text_color=BLACK,
            bullet_symbol="",
            points=[
                r"What is the binary representation of $2025$?",
                r"A) \texttt{101101}",
                r"B) \texttt{11111101001}",
                r"C) \texttt{10010101010}",
                r"D) \texttt{11101101100}",
                r"E) \texttt{10101010111}"
            ],
            **kwargs
        )
        
        add_footer(self)

    def present_points(self, run_time=1):
        self.play(Create(self.bullets), run_time=run_time)
        self.next_slide()

        self.play(self.bullets[1].animate.set_color(RED_A), run_time=run_time)
        self.next_slide()

        self.play(
            self.bullets[3].animate.set_color(RED_A),
            self.bullets[4].animate.set_color(RED_A),
            run_time=run_time
        )
        self.next_slide()

        self.play(
            self.bullets[5].animate.set_color(RED_A),
            self.bullets[2].animate.set_color(PURE_GREEN),
            run_time=run_time
        )
        self.next_slide()

class Problem_Bitwise(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Applications",
            text_color=BLACK,
            points=[
                r"Check whether a number is \textbf{odd or even} using bitwise operators.",
                r"\textbf{Set} (make it $1$) the $i$-th bit of a number using bitwise operators.",
                r"\textbf{Clear} (make it $0$) the $i$-th bit of a number using bitwise operators.",
                r"\textbf{Toggle} (change) the $i$-th bit of a number using bitwise operators.",
                r"\textbf{Check} whether the $i$-th bit of a number is set ($1$) using bitwise operators.",
                r"Check whether a number is a \textbf{power of $2$} using bitwise operators."
            ],
            **kwargs
        )
        
        add_footer(self)

class Section_Summary(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title="Summary",
            **kwargs
        )
        
        add_footer(self)

class Summary1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Summary",
            text_color=BLACK,
            points=[
                r"Using $n$ bits, $2^n$ different sequences can be formed, each representing a unique number.",
                r"The bit sequences are interpreted using the binary number system, a positional system where each position has a weight given by a power of $2$.",
                r"By reserving one bit as a sign bit and slightly modifying the representation, both positive and negative numbers can be represented in a way that is consistent with arithmetic operations.",
                r"Bitwise operators operate directly on individual bits of an integer, effectively treating the integer as an array of boolean values."
            ],
            **kwargs
        )
        add_footer(self)


class Summary2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Summary",
            text_color=BLACK,
            points=[
                r"Shift operators move bits left or right, corresponding to multiplication or division by powers of $2$, within certain limits.",
                r"Specific bits within a number can be efficiently read and manipulated using carefully chosen bitmasks and bitwise operators.",
                r"Shift operators are often useful for generating specific bitmasks efficiently.",
                r"Analyzing binary representations can reveal useful mathematical observations. For example, the last $k$ bits of a number represent its value modulo $2^k$.",
                r"Bitmasks are commonly used to represent sets and bitwise operators are used to perform different set operations."
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
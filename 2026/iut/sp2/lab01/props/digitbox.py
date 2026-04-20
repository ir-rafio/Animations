from manim import *
import numpy as np
from .layout import *

class Bubble(VGroup):
    def __init__(
        self,
        radius,
        bubble_color,
        stroke_color=WHITE,
        dot_color=None,
        dot_layout=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.radius = radius

        self.circle = Circle(
            radius=radius,
            fill_color=bubble_color,
            fill_opacity=0,
            stroke_color=stroke_color
        )

        if dot_color is None: dot_color = bubble_color
        self.dots = self._create_dots(dot_layout, dot_color)

        self.add(self.circle)
        if(len(self.dots) > 0): self.add(self.dots)
    
    def _create_dots(self, layout, dot_color):
        dots = VGroup()
        if layout is None: return dots
        
        positions = layout.get_positions()
        ara = np.array(positions)

        max_length = Layout.max_length(positions)
        min_gap = Layout.min_gap(positions)

        target_distance = 0.65
        scale_factor = target_distance / max_length if max_length > 0 else target_distance
        ara *= scale_factor

        ara *= self.radius
        dot_radius = self.radius * min(
            0.9 - target_distance,
            min_gap * scale_factor * 0.9 / 2
        )

        for pos in ara:
            dots.add(
                Dot(
                    point=pos,
                    radius=dot_radius,
                    color=dot_color,
                    fill_opacity=0
                )
            )
            
        return dots
    
    def show_active(self, bubble_opacity=1.0, stroke_opacity=1.0):
        self.circle.set_fill(opacity=bubble_opacity)
        self.dots.set_fill(opacity=bubble_opacity * 0.8)
        self.circle.set_stroke(opacity=stroke_opacity)
        return self
    
    def show_inactive(self, stroke_opacity=1.0):
        self.set_fill(opacity=0)
        self.circle.set_stroke(opacity=stroke_opacity)
        return self
    
    def hide(self):
        self.set_fill(opacity=0)
        self.circle.set_stroke(opacity=0)
        return self
    
    def set_color(
        self,
        bubble_color=None,
        stroke_color=None,
        dot_color=None,
        stroke_opacity=None
    ):
        if bubble_color is not None: self.circle.set_fill(color=bubble_color)
        if stroke_color is not None: self.circle.set_stroke(color=stroke_color)
        if dot_color is not None: self.dots.set_fill(color=dot_color)
        if stroke_opacity is not None: self.circle.set_stroke(opacity=stroke_opacity)

        return self

class DigitBox(VGroup):
    def __init__(
        self,
        base=10,
        value=0,
        height=3,
        bubble_layout=GridLayout(9),
        dot_layout=TriangularLayout(10),
        box_color=None,
        bubble_color=GREEN_E,
        dot_color=YELLOW,
        stroke_color=WHITE,
        bubble_opacity=1.0,
        stroke_opacity=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.base = base
        self.value = ValueTracker(self._validate_value(value))

        self._validate_layouts(bubble_layout, dot_layout)
        
        self.bubble_opacity = bubble_opacity
        self.stroke_opacity = stroke_opacity
        self.is_visible = True

        self.box_color = box_color
        self.stroke_color = stroke_color

        self.box = Square(side_length=height)
        self.bubbles = self._create_bubbles(bubble_layout, dot_layout, bubble_color, dot_color, stroke_color, height)

        self._update_box()
        self._update_bubbles()
        
        self.box.add_updater(lambda m: self._update_box())
        self.bubbles.add_updater(lambda m: self._update_bubbles())

        self.add(self.box, self.bubbles)

    def _validate_value(self, v):
        if isinstance(v, float) and v.is_integer(): v = int(v)
        
        if not isinstance(v, int): raise TypeError("value must be an integer!")
        if v < 0: raise ValueError("value underflow!")
        if v >= self.base: raise ValueError("value overflow!")
        
        return v
    
    def _validate_layouts(self, bubble_layout, dot_layout):
        if bubble_layout is None:
            raise ValueError("bubble layout must not be None!")
        
        bubble_positions = bubble_layout.get_positions()
        if len(bubble_positions) != self.base - 1:
            raise ValueError(f"bubble layout must have exactly {self.base - 1} positions!")
        
        if dot_layout is None: return
        dot_positions = dot_layout.get_positions()
        if len(dot_positions) != self.base:
            raise ValueError(f"dot layout must have exactly {self.base} positions or be empty!")        

    def _update_box(self):
        if self.box is None: raise ValueError("box cannot be None!")
    
        if self.is_visible:
            if self.box_color is None: self.box.set_fill(opacity=0)
            else: self.box.set_fill(color=self.box_color, opacity=self.bubble_opacity)

            self.box.set_stroke(color=self.stroke_color, opacity=self.stroke_opacity)
        
        else:
            self.box.set_fill(opacity=0)
            self.box.set_stroke(opacity=0)
    
    def _create_bubbles(self, bubble_layout, dot_layout, bubble_color, dot_color, stroke_color, height):
        bubbles = VGroup()

        positions = bubble_layout.get_positions()
        ara = np.array(positions)

        border_distance = height / 2
        scale_factor = 0.65
        ara *= scale_factor

        ara *= border_distance
        min_gap = Layout.min_gap(positions)
        bubble_radius = border_distance * min(
            0.9 - scale_factor,
            min_gap * scale_factor * 0.9 / 2
        )

        for pos in ara:
            bubble = Bubble(
                radius=bubble_radius,
                bubble_color=bubble_color,
                stroke_color=stroke_color,
                dot_color=dot_color,
                dot_layout=dot_layout,
            )
            
            bubble.move_to(pos)
            bubbles.add(bubble)

        return bubbles
    
    def _update_bubbles(self):
        if self.is_visible:
            v = self.get_value()

            for i, bubble in enumerate(self.bubbles):
                if i < v: bubble.show_active(self.bubble_opacity, self.stroke_opacity)
                else: bubble.show_inactive(self.stroke_opacity)
        
        else:
            for bubble in self.bubbles: bubble.hide()
    
    def show(self):
        self.is_visible = True
        self.update()
        return self
    
    def hide(self):
        self.is_visible = False
        self.update()
        return self
    
    def get_value(self):
        return round(self.value.get_value())
    
    def set_value(self, v):
        v = self._validate_value(v)
        self.value.set_value(v)
        self.update()
        return self
    
    def animate_to_value(self, v):
        v = self._validate_value(v)
        return self.value.animate.set_value(v)
    
    def increment(self, cycle=True):
        v = self.get_value()

        v += 1
        if(cycle): v %= self.base

        self.set_value(v)

        return self
    
    def decrement(self, cycle=True):
        v = self.get_value()

        v -= 1
        if(cycle): v %= self.base

        self.set_value(v)

        return self
    
    def set_color(
        self,
        box_color=None,
        bubble_color=None,
        stroke_color=None,
        dot_color=None,
        bubble_opacity=None,
        stroke_opacity=None
    ):
        if box_color is not None: self.box_color = box_color
        if stroke_color is not None: self.stroke_color = stroke_color
        if bubble_opacity is not None: self.bubble_opacity = bubble_opacity
        if stroke_opacity is not None: self.stroke_opacity = stroke_opacity

        for bubble in self.bubbles:
            bubble.set_color(
                bubble_color=bubble_color,
                stroke_color=stroke_color,
                dot_color=dot_color,
                stroke_opacity=stroke_opacity
            )
        
        # self.update()
        self._update_box()
        self._update_bubbles()
        return self

class NumberBox(VGroup):
    def __init__(
        self,
        n=1,
        base=10,
        value=0,
        height=2,
        bubble_layout=GridLayout(9),
        dot_layout=TriangularLayout(10),
        colors=None,
        stroke_color=WHITE,
        stroke_opacity=1.0,
        show_leading_zeroes=False,
        show_digit_texts=True,
        show_weights=True,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.n = n
        self.base = base
        self.value = ValueTracker(self._validate_value(value))

        self.show_leading_zeroes = show_leading_zeroes
        self.show_weights = show_weights
        self.show_digit_texts = show_digit_texts

        self.stroke_color = stroke_color
        self.stroke_opacity = stroke_opacity

        self.boxes = self._create_boxes(bubble_layout, dot_layout, height, colors)
        self.weights = self._create_weights()
        self.digit_texts = self._create_digit_texts(colors)

        self._resize_weights(height / 2)
        self._resize_digit_texts(height)

        self.boxes.arrange(LEFT)
        self._position_texts()

        self.add(self.boxes, self.weights, self.digit_texts)
        self.update()

    def _validate_value(self, v):
        if isinstance(v, float) and v.is_integer(): v = int(v)
        
        if not isinstance(v, int): raise TypeError("value must be an integer!")
        if v < 0: raise ValueError("value underflow!")
        if v >= self.base ** self.n: raise ValueError("value overflow!")
        
        return v
    
    def _get_digits(self):
        v = self.get_value()
        digits = []

        for _ in range(self.n):
            digits.append(v % self.base)
            v //= self.base

        return digits
    
    def num_visible_digits(self):
        if self.show_leading_zeroes: return self.n

        if self.get_value() == 0: return 1

        digits = self._get_digits()
        while digits[-1] == 0: digits.pop()
        return len(digits)
    
    def _create_boxes(self, bubble_layout, dot_layout, height, colors):
        boxes = VGroup()
        digits = self._get_digits()

        if colors is None: raise ValueError("colors cannot be None!")
        if len(colors) != self.n: raise ValueError(f"Number of colors must be exactly {self.n}")
        if len(digits) != self.n: raise ValueError(f"Number of digits must be exactly {self.n}")

        for i in range(self.n):
            box = DigitBox(
                base=self.base,
                value=digits[i],
                height=height,
                bubble_layout=bubble_layout,
                dot_layout=dot_layout if i > 0 else None,
                bubble_color=colors[i],
                dot_color=colors[i - 1] if i > 0 else None,
                stroke_color=self.stroke_color,
                stroke_opacity=self.stroke_opacity
            )
            boxes.add(box)
        
        def updater(boxes):
            digits = self._get_digits()
            for box, digit in zip(boxes, digits):
                box.set_value(digit)
            
            k = self.num_visible_digits()
            for i, box in enumerate(boxes):
                if i < k: box.show()
                else: box.hide()

                box.set_color(stroke_color=self.stroke_color, stroke_opacity=self.stroke_opacity)
        
        boxes.add_updater(updater)
        return boxes
    
    def _create_weights(self):
        weights = VGroup()

        for i in range(self.n):
            wt = DecimalNumber(
                number=self.base ** i,
                color=self.stroke_color,
                fill_opacity=self.stroke_opacity,
                num_decimal_places=0
            )
            weights.add(wt)
        
        def updater(weights):
            k = self.num_visible_digits()
            for i, wt in enumerate(weights):
                if i < k and self.show_weights: wt.set_opacity(self.stroke_opacity)
                else: wt.set_opacity(0)

                wt.set_color(self.stroke_color)
        
        weights.add_updater(updater)
        return weights
    
    def _create_digit_texts(self, colors):
        digit_texts = VGroup()
        digits = self._get_digits()

        if colors is None: raise ValueError("colors cannot be None!")
        if len(colors) != self.n: raise ValueError(f"Number of colors must be exactly {self.n}")
        if len(digits) != self.n: raise ValueError(f"Number of digits must be exactly {self.n}")

        for i in range(self.n):
            dt = DecimalNumber(digits[i], color=colors[i], num_decimal_places=0)
            digit_texts.add(dt)
        
        def updater(digit_texts):
            digits = self._get_digits()
            for dt, digit in zip(digit_texts, digits):
                dt.set_value(digit)
            
            k = self.num_visible_digits()
            for i, dt in enumerate(digit_texts):
                if i < k and self.show_digit_texts: dt.set_opacity(self.stroke_opacity)
                else: dt.set_opacity(0)
        
        digit_texts.add_updater(updater)
        return digit_texts
    
    def _resize_weights(self, length):
        scale_factor = min(length / self.weights[-1].width, length / self.weights[-1].height)
        for wt in self.weights: wt.scale(scale_factor)
    
    def _resize_digit_texts(self, length):
        scale_factor = min(length / self.digit_texts[-1].width, length / self.digit_texts[-1].height)
        for wt in self.digit_texts: wt.scale(scale_factor)
    
    def _position_texts(self):
        for box, wt, dt in zip(self.boxes, self.weights, self.digit_texts):
            wt.next_to(box, UP)
            dt.next_to(box, DOWN)
    
    def get_value(self):
        return round(self.value.get_value())
    
    def set_value(self, v):
        v = self._validate_value(v)
        self.value.set_value(v)
        self.update()
        return self
    
    def animate_to_value(self, v):
        v = self._validate_value(v)
        return self.value.animate.set_value(v)
    
    def increment(self, cycle=True):
        v = self.get_value()

        v += 1
        if(cycle): v %= self.base ** self.n

        self.set_value(v)

        return self
    
    def decrement(self, cycle=True):
        v = self.get_value()

        v -= 1
        if(cycle): v %= self.base ** self.n

        self.set_value(v)

        return self
    
    def set_color(self, stroke_color=None, stroke_opacity=None):
        if stroke_color is not None: self.stroke_color = stroke_color
        if stroke_opacity is not None: self.stroke_opacity = stroke_opacity
        
        self.update()
        return self
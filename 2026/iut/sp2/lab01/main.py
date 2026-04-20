from manim import *
from manim_slides import Slide
from props.presentation import *

class TitleSlide(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title = r"Title\\Slide",
            **kwargs
        )
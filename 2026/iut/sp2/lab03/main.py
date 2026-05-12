from manim import *
from manim_slides import Slide
from props.presentation import *
from props.code_style import *
from props.function_slide import *
from lab_info import *

sans_template = TexTemplate()
sans_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
Tex.set_default(tex_template=sans_template)

class Title_Algorithms(TitleSlide):
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
            points=[
                r"Do you think that computer science is all about computers?",
                r"Computer science is actually \textbf{the science of computation.}",
                r"The field of computer science was developed by mathematicians before electronic computers.",
                r"The first step of programming is problem-solving, which has pretty much nothing to do with languages, syntax, or even computers.",
                r"An \textbf{algorithm} is a finite sequence of well-defined steps to solve a problem.",
                r"Algorithms have been studied and recorded since ancient times.",
                r"One of the major fields of computer science is the study of algorithms, focusing on their discovery and analysis."
            ],
            **kwargs
        )
        add_footer(self)
        
class TableOfContents(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Table of Contents",
            text_color=BLACK,
            points=[
                r"Basic Idea of Algorithms",
                r"Criteria for Choosing Algorithms",
                r"Time and Space Complexity",
                r"Asymptotic Analysis",
                r"Sorting Problem",
                r"Sorting Algorithms"
            ],
            **kwargs
        )
        add_footer(self)

class Section_Algorithms(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Basic Idea\\of\\Algorithms",
            **kwargs
        )
        add_footer(self)
        
class Algorithms(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Basic Idea of Algorithms",
            text_color=BLACK,
            points=[
                r"An algorithm is a \textbf{finite} \textbf{sequence} of \textbf{well-defined} steps to solve a problem.",
                r"A \textbf{problem} is a \textbf{well-defined relation} between a set of \textbf{inputs} and a set of \textbf{outputs}.",
                r"An algorithm can also be viewed as a list of instructions that can be followed to solve a problem.",
                r"An algorithm that successfully solves a problem is called a \textbf{solution} to that problem."
            ],
            **kwargs
        )
        add_footer(self)
        
class AlgorithmVsCode1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Basic Idea of Algorithms",
            text_color=BLACK,
            points=[
                r"The concept of algorithms is completely independent of programming/coding.",
                r"Roughly, programming is telling the computer what to do by giving it instructions in its language (a programming language).",
                r"The algorithm is the list of instructions, while code is the written form of those instructions in a programming language.",
                r"Before giving instructions to the computer for solving a problem, a programmer needs to know what instructions to give (the algorithm to solve the problem)."
            ],
            **kwargs
        )
        add_footer(self)

        self._build_figure("./assets/img/computers.jpg")

    def _build_figure(self, img_path):
        img = ImageMobject(img_path)
        img.scale_to_fit_height(5)

        label = Tex("Figure: Computer Room, NACA High Speed Flight Station (1949)", color=self.text_color)
        label.scale_to_fit_width(6)

        self.figure = Group(img, label).arrange(DOWN, buff=0.1)
        self.position_group(self.figure)
        self.figure.set_x(self.header_underline.get_x())
    
    def construct(self):
        super().construct()

        self.play(FadeIn(self.figure))
        self.next_slide()

        self.play(FadeOut(self.figure))
        self.next_slide()
        
class AlgorithmVsCode2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Basic Idea of Algorithms",
            text_color=BLACK,
            points=[
                r"Imagine a Japanese person asks you for directions to the nearest bank (assume you barely understand Japanese, and somehow understand the question).",
                r"To answer his question, will you first think about the route to the bank, or about which Japanese words to use?",
                r"No matter how fluent you are in Japanese, if you don't know where the bank is and how to get there, you cannot provide the answer."
            ],
            **kwargs
        )
        add_footer(self)
        
class AlgorithmVsCode3(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Basic Idea of Algorithms",
            text_color=BLACK,
            points=[
                r"Given any problem, a programmer first needs to understand the problem (the inputs and the outputs).",
                r"Next, he needs to find out the sequence of steps to solve the problem -- this is discovering an algorithm.",
                r"For this step, it helps to imagine that there is no computer and the programmer has to solve the problem himself. This leads him to discover solution ideas which can be formalized into an algorithm.",
                r"Once the programmer has the list of instructions in the algorithm, he can translate them to a programming language.",
                r"This results in a program that solves the problem. Given any input, it generates an output that matches the relation defined in the problem."
            ],
            **kwargs
        )
        add_footer(self)
        
class AlgorithmExample1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Algorithm Example --- Valid Triangle",
            text_color=BLACK,
            points=[
                r"\textbf{Problem}: Given three integers as side lengths, determine whether they can form a valid triangle.",
                r"\textbf{Input}: Three positive integers $a$, $b$, and $c$.",
                r"\textbf{Output}: \texttt{YES} or \texttt{NO}."
            ],
            **kwargs
        )
        add_footer(self)

        self.build_algo("./assets/algo/checkValidTriangle.txt")
        self.build_code("./assets/code/checkValidTriangle.c")

        self.side = VGroup(self.algo, self.code).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        self.fit_in_frame(self.side)
        group = VGroup(self.bullets, self.side).arrange(DOWN, buff=0.4)
        self.fit_in_frame(group)
        self.position_group(group)

    def build_algo(self, algo_file):
        self.algo = StylelessCode(
            code_file=algo_file,
            text_color=self.text_color
        )

    def build_code(self, code_file):
        self.code = StylelessCode(
            code_file=code_file,
            text_color=self.text_color
        )

    def present_points(self, run_time=1):
        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Create(self.algo), run_time=run_time)
        self.next_slide()

        self.play(Create(self.code), run_time=run_time)
        self.next_slide()
        
class AlgorithmExample2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Algorithm Example --- Get Min",
            text_color=BLACK,
            points=[
                r"\textbf{Problem}: Given an array of integers, determine the minimum value in the array.",
                r"\textbf{Input}: An integer array of size $n$.",
                r"\textbf{Output}: An integer value."
            ],
            **kwargs
        )
        add_footer(self)

        self.build_algo("./assets/algo/getMin.txt")
        self.build_code("./assets/code/getMin.c")

        self.side = VGroup(self.algo, self.code).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        self.fit_in_frame(self.side)
        group = VGroup(self.bullets, self.side).arrange(DOWN, buff=0.4)
        self.fit_in_frame(group)
        self.position_group(group)

    def build_algo(self, algo_file):
        self.algo = StylelessCode(
            code_file=algo_file,
            text_color=self.text_color
        )

    def build_code(self, code_file):
        self.code = StylelessCode(
            code_file=code_file,
            text_color=self.text_color
        )

    def present_points(self, run_time=1):
        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Create(self.algo), run_time=run_time)
        self.next_slide()

        self.play(Create(self.code), run_time=run_time)
        self.next_slide()
        
class AlgorithmExample3(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Algorithm Example --- Find Min",
            text_color=BLACK,
            points=[
                r"\textbf{Problem}: Given an array of integers, find where the minimum element in the array is.",
                r"\textbf{Input}: An integer array of size $n$.",
                r"\textbf{Output}: An index."
            ],
            **kwargs
        )
        add_footer(self)

        self.build_algo("./assets/algo/findMin.txt")
        self.build_code("./assets/code/findMin.c")

        self.side = VGroup(self.algo, self.code).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        self.fit_in_frame(self.side)
        group = VGroup(self.bullets, self.side).arrange(DOWN, buff=0.4)
        self.fit_in_frame(group)
        self.position_group(group)

    def build_algo(self, algo_file):
        self.algo = StylelessCode(
            code_file=algo_file,
            text_color=self.text_color
        )

    def build_code(self, code_file):
        self.code = StylelessCode(
            code_file=code_file,
            text_color=self.text_color
        )

    def present_points(self, run_time=1):
        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Create(self.algo), run_time=run_time)
        self.next_slide()

        self.play(Create(self.code), run_time=run_time)
        self.next_slide()

class Section_Criteria(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Criteria\\For\\Choosing\\Algorithms",
            **kwargs
        )
        add_footer(self)

class Criteria(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Criteria for Choosing Algorithms",
            text_color=BLACK,
            points=[
                r"For a given problem, there are often multiple possible algorithms. In such cases, one has to be selected.",
                r"There are different criteria or metrics that help decide the `better' algorithm.",
                r"The first and most essential criterion is correctness.",
                r"Other criteria include time complexity, space complexity, simplicity, and more.",
                r"An algorithm with low time and space complexity is called an \textbf{efficient} algorithm.",
                r"In real-world scenarios, trade-offs between time and space are often necessary."
            ],
            **kwargs
        )
        add_footer(self)
        
class Correctness(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Criteria for Choosing Algorithms --- Correctness",
            text_color=BLACK,
            points=[
                r"An algorithm is \textbf{correct} if it generates correct output for every valid input.",
                r"To prove the correctness of an algorithm, it is necessary to prove that for \textbf{any input in the domain}, the algorithm will \textbf{halt} and \textbf{generate the correct output}.",
                r"If a single input in the domain causes the algorithm to get stuck or generate the incorrect output, then the algorithm is incorrect.",
                r"An incorrect algorithm is useless, regardless of how fast it runs."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Complexity(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Time\\and\\Space\\Complexity",
            **kwargs
        )
        add_footer(self)
        
class TimeComplexity(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Time Complexity",
            text_color=BLACK,
            points=[
                r"If two algorithms correctly solve a problem, then the algorithm that generates the output faster is usually preferred.",
                r"Time complexity is a measurement of the time an algorithm needs for execution.",
                r"It is measured not in time units (seconds, minutes, ...), but in number of operations.",
                r"Formally, the time complexity of an algorithm is a function from the \textbf{input size} of the algorithm to the \textbf{number of operations} the algorithm performs for an input of that size.",
                r"Time complexity describes how the number of operations grows as the input size increases.",
                r"Time complexity is primarily affected by loops and recursion."
            ],
            **kwargs
        )
        add_footer(self)
        
class TimeComplexity2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Time Complexity",
            text_color=BLACK,
            points=[
                r"Although a computer is very fast in computation, a slow algorithm can hinder its performance.",
                r"For instance, \textbf{repeated addition} and \textbf{long multiplication} are two algorithms for multiplying two numbers.",
            ],
            **kwargs
        )
        add_footer(self)

        self.algo1 = StylelessCode(
            code_file="./assets/algo/repeatedAddition.txt",
            text_color=self.text_color
        )

        self.algo2 = StylelessCode(
            code_file="./assets/algo/longMultiplication.txt",
            text_color=self.text_color
        )

        self.side = VGroup(self.algo1, self.algo2).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        self.fit_in_frame(self.side)
        group = VGroup(self.bullets, self.side).arrange(DOWN, buff=0.4)
        self.fit_in_frame(group)
        self.position_group(group)

    def present_points(self, run_time=1):
        for bullet in self.bullets:
            self.play(Write(bullet), run_time=run_time)
            self.next_slide()

        self.play(Create(self.algo1), run_time=run_time)
        self.play(Create(self.algo2), run_time=run_time)
        self.next_slide()
        
class TimeComplexity3(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Time Complexity",
            text_color=BLACK,
            points=[
                r"Both repeated addition and long multiplication are correct algorithms, but long multiplication is much faster than repeated addition.",
                r"For small numbers, the difference in performance is not noticeable. But for large inputs, it becomes significant.",
                r"For multiplying two $25$-digit numbers, a school kid from class five using the long multiplication algorithm on pen and paper can get the output faster than the fastest supercomputer today running the repeated addition algorithm.",
                r"To keep credit cards or Facebook accounts secure, it is required to multiply hundred-digit numbers everyday, so using repeated addition is completely impractical."
            ],
            **kwargs
        )
        add_footer(self)
        
class SpaceComplexity(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Space Complexity",
            text_color=BLACK,
            points=[
                r"In addition to running time, it is often important to measure the memory required by an algorithm.",
                r"Space complexity of an algorithm is a function from the \textbf{input size} of the algorithm to the amount of \textbf{extra memory} the algorithm needs for an input of that size.",
                r"Space complexity only counts the memory used for temporary variables used by the algorithm; input and output are not included.",
                r"Space complexity is mainly affected by the use of temporary data structures and recursion."
            ],
            **kwargs
        )
        add_footer(self)

class ComplexityExample(Slide):
    def __init__(self, idx, complexity, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1

        code_file = f"./assets/code/tc{idx}.c"
        header_text = r"Time Complexity Example"

        self.text_color = BLACK
        add_header(self, header_text, text_color=self.text_color)
        add_footer(self)

        self.build_group(code_file, complexity)
        self.fit_group_in_frame()
        self.position_group()

    def construct(self):
        self.present()
        self.next_slide()
        self.cleanup()
        self.next_slide()
    
    def build_group(self, code_file, complexity):
        self.code = StylelessCode(
            code_file=code_file,
            text_color=self.text_color
        )
        self.complexity = Tex(complexity, color=self.text_color)
    
    def fit_group_in_frame(self):
        max_width = config.frame_width - 1
        max_height = config.frame_height - 2 - self.header_mob.height

        if self.code.width > max_width:
            self.code.scale_to_fit_width(max_width)

        if self.complexity.width > max_width:
            self.complexity.scale_to_fit_width(max_width)

        self.group = VGroup(self.code, self.complexity)
        self.group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        if self.group.height > max_height:
            self.group.scale_to_fit_height(max_height)
    
    def position_group(self):
        self.group.next_to(
            self.header_mob,
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        )

    def present(self, run_time=1):
        self.play(Write(self.code), run_time=run_time)
        self.next_slide()
        self.play(Write(self.complexity), run_time=run_time)
        self.next_slide()
    
    def cleanup(self, run_time=1):
      self.play(
          Unwrite(self.group),
          run_time=run_time
      )

class ComplexityExample1(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 1,
            complexity = r"\textbf{Time complexity} $T(n) = 7 \in \mathcal{O}(1)$",
            **kwargs
        )

class ComplexityExample2(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 2,
            complexity = r"\textbf{Time complexity} $T(n) = 4n \in \mathcal{O}(n)$",
            **kwargs
        )

class ComplexityExample3(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 3,
            complexity = r"\textbf{Time complexity} $T(n) = 4n + 4 \in \mathcal{O}(n)$",
            **kwargs
        )

class ComplexityExample4(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 4,
            complexity = r"\textbf{Time complexity} $T(n) = 5 \in \mathcal{O}(1)$",
            **kwargs
        )

class ComplexityExample5(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 5,
            complexity = r"\textbf{Time complexity} $T(n) \approx \dfrac{n(n + 1)}{2} + 2 \in \mathcal{O}(n^2)$",
            **kwargs
        )

class ComplexityExample6(ComplexityExample):
    def __init__(self, **kwargs):
        super().__init__(
            idx = 6,
            complexity = r"\textbf{Time complexity} $T(n) \in \mathcal{O}(n)$",
            **kwargs
        )

class Section_Asymptotic_Analysis(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Asymptotic\\Analysis",
            **kwargs
        )
        add_footer(self)
        
class AsymptoticAnalysis(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Asymptotic Analysis",
            text_color=BLACK,
            points=[
                r"If the time complexity of two algorithms are $100n$ and $n^2$ respectively, which one is faster?",
                r"The answer depends on the size of the input. For small values of $n$, $n^2$ can be smaller than $100n$.",
                r"However, \textbf{complexity analysis focuses on large inputs}, not small ones.",
                r"If $n$ is large enough, $n^2$ will always be greater than $kn$, no matter how large the constant $k$ is.",
                r"So, the \textbf{growth of a function} is more interesting than its exact values."
            ],
            **kwargs
        )
        add_footer(self)
        
class BigONotation(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Big-O Notation",
            text_color=BLACK,
            points=[
                r"\textbf{Big-O notation} is used to describe the growth rate of an algorithm's time or space complexity.",
                r"It focuses on the dominant term and ignores constant factors and lower-order terms.",
                r"Formally, a function $f(n)$ is in $\mathcal{O}(g(n))$ if there exist constants $c > 0$ and $n_0 > 0$ such that: $f(n) \le c \cdot g(n)$ for any $n > n_0$.",
                r"This definition simply means that beyond some input size $n_0$, the function $f(n)$ can not grow faster than a constant multiple of $g(n)$."
            ],
            **kwargs
        )
        add_footer(self)
        
class BigONotation2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Big-O Notation",
            text_color=BLACK,
            points=[
                r"Notations such as $\mathcal{O}(1)$, $\mathcal{O}(n)$, $\mathcal{O}(n^2)$, etc., are sets of functions.",
                r"For instance, $\mathcal{O}(n)$ represents the set of all functions whose growth is at most linear (e.g., $n$, $5n$, $\frac{n}{2}$, $100n + 20$, etc.).",
                r"It is easy to observe that smaller sets are subsets of larger sets, such as $\mathcal{O}(1) \subset \mathcal{O}(\log(n)) \subset \mathcal{O}(\sqrt{n}) \subset \mathcal{O}(n) \subset \mathcal{O}(n^2)$.",
                r"In practice, time or space complexity is expressed using \textbf{the smallest set} that accurately describes the growth of the function."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Sorting_Problem(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Sorting\\Problem",
            **kwargs
        )
        add_footer(self)

class SortingProblem(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Problem",
            text_color=BLACK,
            points=[
                r"The sorting problem is considered one of the most fundamental problems in computer science.",
                r"It appears frequently as a subroutine in many algorithms and applications.",
                r"Initially, sorting can be understood as the task of arranging numbers in ascending order.",
                r"\textbf{Input}: An array of size $n$.",
                r"\textbf{Output}: An array of size $n$ containing the same elements, arranged in sorted (ascending) order.",
                r"In most practical cases, sorting is performed in-place. As a result, no separate output array is produced; instead, the input array itself is modified and becomes sorted as a side effect."
            ],
            **kwargs
        )
        add_footer(self)
        
class SortingProblem2(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Problem",
            text_color=BLACK,
            points=[
                r"The elements of the input array and the output array must remain exactly the same; no element may be lost, and no new element may be introduced.",
                r"Because of this, a sorting algorithm often just performs a sequence of comparisons and swaps.",
                r"A sorted array (in non-decreasing order) satisfies this condition: For any integers $i$ and $j$ such that $0 \le i \le j \le n - 1$, the $i$-th element is less than or equal to the $j$-th element.",
                r"Sorting may also be performed in descending order or according to any well-defined transitive ordering on the data.",
                r"Sorting is not limited to numbers. Other types of data, such as characters, strings, or more complex data structures, can also be sorted as long as a well-defined ordering exists for that data type."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Sorting_Algorithms(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Sorting\\Algorithms",
            **kwargs
        )
        add_footer(self)
        
class SelectionSort(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Selection Sort",
            text_color=BLACK,
            points=[
                r"In a sorted array, which element will be at index $0$?",
                r"Which element will be at index $1$ and how to find it from the original array?",
                r"Selection sort is the simplest and most intuitive sorting algorithm.",
                r"The algorithm works by repeatedly selecting the smallest element from the unsorted portion of the array and placing it in its correct position by swapping."
            ],
            **kwargs
        )
        add_footer(self)

class SelectionSortCode1(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Selection Sort",
            points=[
                r"\texttt{void selectionSort(int ara[], int n):} sorts all \texttt{n} elements of \texttt{ara} using selection sort algorithm."
            ],
            code_file="./assets/code/selectionSort.c",
            intervals=[[1, 2, 10], [3, 5, 6, 9], [7], [8]],
            **kwargs
        )
        add_footer(self)

class SelectionSortCode2(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Selection Sort",
            points=[
                r"\texttt{int findFirst(int ara[], int l, int r):} returns the position of the first selected element in \texttt{ara[l \dots r]}."
            ],
            code_file="./assets/code/findFirst.c",
            intervals=[[1, 2, 12], [3], [5, 6, 7, 8, 9], [11]],
            **kwargs
        )
        add_footer(self)
        
class InsertionSort(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Insertion Sort",
            text_color=BLACK,
            points=[
                r"If all elements of an array except the last one create a sorted subarray, how to sort the array easily?",
                r"How to easily process the last element?",
                r"Insertion sort builds the sorted array incrementally.",
                r"At each step, one element from the unsorted portion is taken and inserted into its correct position in the sorted portion.",
                r"Initially, the first element is assumed to be in a sorted portion. Each subsequent elements is `pushed' left as many positions as needed.",
                r"The correctness of insertion is based on the transitivity law: if $a < b$ and $b < c$, then $a < c$."
            ],
            **kwargs
        )
        add_footer(self)

class InsertionSortCode1(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Insertion Sort",
            points=[
                r"\texttt{void insertionSort(int ara[], int n):} sorts all \texttt{n} elements of \texttt{ara} using insertion sort algorithm."
            ],
            code_file="./assets/code/insertionSort.c",
            intervals=[[1, 2, 5], [3, 4]],
            **kwargs
        )
        add_footer(self)

class InsertionSortCode2(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Insertion Sort",
            points=[
                r"\texttt{void pushLeft(int ara[], int k):} moves \texttt{ara[k]} left until the first \texttt{k+1} elements of \texttt{ara} are in the correct order."
            ],
            code_file="./assets/code/pushLeft.c",
            intervals=[[1, 2, 10], [3, 4, 9], [5, 6], [8]],
            **kwargs
        )
        add_footer(self)
        
class BubbleSort(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Bubble Sort",
            text_color=BLACK,
            points=[
                r"What is the easiest way to check if a given array is sorted?",
                r"In a sorted array, can an element ever be smaller than any element in its left?",
                r"Bubble sort is based on the idea that if all adjacent pairs are sorted, then the entire array is sorted.",
                r"In a single pass round, bubble sort checks all adjacent pairs in the array from left to right.",
                r"Whenever a pair is found to be out of order, the elements are immediately swapped.",
                r"After one round, the largest element of the array goes to the end.",
                r"After $(n - 1)$ rounds, the entire array gets sorted."
            ],
            **kwargs
        )
        add_footer(self)

class BubbleSortCode1(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Bubble Sort",
            points=[
                r"\texttt{void bubbleSort(int ara[], int n):} sorts all \texttt{n} elements of \texttt{ara} using bubble sort algorithm."
            ],
            code_file="./assets/code/bubbleSort.c",
            intervals=[[1, 2, 5], [3, 4]],
            **kwargs
        )
        add_footer(self)

class BubbleSortCode2(FunctionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Sorting Algorithm --- Bubble Sort",
            points=[
                r"\texttt{void runBubbleSortRound(int ara[], int n):} runs one round of bubble sort on all \texttt{n} elements of \texttt{ara}."
            ],
            code_file="./assets/code/runBubbleSortRound.c",
            intervals=[[1, 2, 8], [3, 4, 7], [5, 6]],
            **kwargs
        )
        add_footer(self)
        
class SortingTimeComplexity(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text=r"Sorting Algorithms",
            text_color=BLACK,
            points=[
                r"In selection sort, to place one element in the correct position, $\mathcal{O}(n)$ operations are required to find it and $\mathcal{O}(1)$ operation to swap it.",
                r"To place $n$ elements in the correct positions, selection sort needs $\mathcal{O}(n^2)$ operations, which is its time complexity.",
                r"In insertion sort, pushing one element to its correct position requires $\mathcal{O}(n)$ operations in the worst case ($\mathcal{O}(1)$ in the best case).",
                r"Insertion sort needs to push $(n - 1)$ elements, so the total time complexity is $\mathcal{O}(n^2)$.",
                r"The time complexity for one round of bubble sort is $\mathcal{O}(n)$.",
                r"Bubble sort needs $(n - 1)$ rounds to sort the array. Total time complexity is $\mathcal{O}(n^2)$."
            ],
            **kwargs
        )
        add_footer(self)

class Section_Summary(SectionSlide):
    def __init__(self, **kwargs):
        super().__init__(
            section_title=r"Summary",
            **kwargs
        )
        add_footer(self)

class Summary1(BulletSlide):
    def __init__(self, **kwargs):
        super().__init__(
            header_text="Summary",
            text_color=BLACK,
            points=[
                r"An algorithm is a finite sequence of well-defined steps that solves a problem.",
                r"Effective problem solving starts with understanding input-output relationships before coding.",
                r"Multiple algorithms may solve the same problem; prioritize correctness, then efficiency and simplicity.",
                r"Time complexity measures how operations grow with input size, while space complexity tracks memory usage.",
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
                r"Asymptotic analysis focuses on large inputs using Big-O notation to describe dominant growth.",
                r"Selection sort repeatedly selects the smallest remaining element.",
                r"Insertion sort builds a sorted portion by shifting elements into place.",
                r"Bubble sort swaps adjacent elements that are out of order."
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
from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class DerivativeMultiplication(FormatedScene):
    def construct(self):
        # region colors
        FUNCTION_COLOR = YELLOW
        VARIABLE_COLOR = RED
        DERIVATIVE_COLOR = CYAN1
        EIGENVALUE_COLOR = ORANGE
        # endregion

        title1=Title("Derivatives using Eigenvalues and Eigenfunctions")

        math1 = VGroup()
        math1 += MathTex(r"{{D}}{{f}} = {{\gamma}}{{f}}")
        math1 += MathTex(r"{{g(D)}}{{f}} = {{g(\gamma)}}{{f}}")
        math1.arrange(DOWN)

        math2 = VGroup()
        math2 += MathTex(r"{{i\hbar\partial_t}} {{\psi}} = {{E}} {{\psi}}")
        math2 += MathTex(r"{{-i\hbar\partial_{x}}} {{\psi}} = {{p}} {{\psi}}")

        math2 += MathTex(r"{{ E }} {{ = {1 \over 2m}}} {{ p ^2}} {{ + V \implies }} {{ i\hbar \partial_{t} }} {{ \psi }} {{ = \Big(-{\hbar^2 \over 2m} }} {{ \partial_{x} ^2}} {{ +V \Big) }} {{ \psi }}")
        math2 += MathTex(r"{{ E ^2}} {{ = }} {{ p^2}} {{ c^2 + \left(mc^2\right)^2 \implies - \hbar^2}} {{ \partial_{t} ^2}} {{ \psi }} {{= \Big( -\hbar^2}} {{ \partial_{x} ^2}} {{ c^2 + \left(mc^2\right)^2 \Big) }} {{ \psi }}")
        math2[0:3].arrange(DOWN)
        math2[3].next_to(math2[2],DOWN)

        mathvg = VGroup(*math1,*math2)

        deep_set_color_by_tex(mathvg, r"f", FUNCTION_COLOR)
        deep_set_color_by_tex(mathvg,r"E",EIGENVALUE_COLOR)
        deep_set_color_by_tex(mathvg, r"\gamma", EIGENVALUE_COLOR)
        deep_set_color_by_tex(mathvg, r"p", EIGENVALUE_COLOR)
        deep_set_color_by_tex(mathvg, r"x", VARIABLE_COLOR)
        deep_set_color_by_tex(mathvg,r"D",DERIVATIVE_COLOR)
        deep_set_color_by_tex(mathvg, r"\partial_{x}", DERIVATIVE_COLOR)
        deep_set_color_by_tex(mathvg, r"\partial_{t}", DERIVATIVE_COLOR)
        deep_set_color_by_tex(mathvg, r"\partial", DERIVATIVE_COLOR)
        deep_set_color_by_tex(mathvg, r"\psi", FUNCTION_COLOR)
        deep_set_color_by_tex(mathvg, r"+", WHITE)

        self.play(Write(title1))
        self.play(Write(math1[0]))
        self.play(Write(math1[1]))

        self.wait()
        self.play(FadeOut(math1[0]),FadeOut(math1[1]))

        self.play(Write(math2[0]),Write(math2[1]))
        self.play(Write(math2[2]))

        self.wait()
        self.play(FadeOut(math2[2]))
        self.play(Write(math2[3]))

        self.wait()





if __name__ == '__main__':
    scene = DerivativeMultiplication()
    scene.render(True)
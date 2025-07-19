from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class DerivativesAlgebraic(FormatedScene):
    def construct(self):
        # region colors
        Y0_COLOR = DARK_BLUE
        Y1_COLOR = GREEN
        DY_COLOR = YELLOW
        DX_COLOR = RED
        SLOPED_COLOR = CYAN1
        # endregion

        # region section1

        # region construction
        title1 = Title("The Product Rule")
        math1 = VGroup()
        math1 += MathTex(r"{{f(x+h)}} = {{h}}{{f'(x)}}")

        math2 = VGroup()
        math2 += MathTex(r"{{f(x+h)}}={{f_a(x+h)}}{{f_b(x+h)}}")
        math2 += MathTex(r"{{f(x+h)}}=\big( {{f_a(x)}} + {{h}} f_a'(x) \big) \big( {{f_b(x)}} + {{h}} f_b'(x) \big)")
        math2 += MathTex(r"{{f(x+h)}}={{f_a(x)}}{{f_b(x)}} + {{h}}{{ \big( f_a'(x)f_b(x)+f_a(x)f_b'(x) \big) }} + {{h^2}} f_a'(x)f_b'(x)")

        math3 = VGroup()
        math3 += MathTex(r"{{h}}{{f'(x)}} = {{h}}{{ \big( f_a'(x)f_b(x)+f_a(x)f_b'(x) \big) }}")
        math3 += MathTex(r"{{f'(x)}} = {{f_a'(x)f_b(x)+f_a(x)f_b'(x)}}")

        mathvg = VGroup(*math1,*math2,*math3)

        deep_set_color_by_tex(mathvg,r"h",DX_COLOR)
        deep_set_color_by_tex(mathvg, r"h^2", DX_COLOR)
        deep_set_color_by_tex(mathvg,r"f(x+h)",Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"f_a(x+h)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"f_b(x+h)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"f_b(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"f_a(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg,"f_a'(x)f_b(x)+f_a(x)f_b'(x)", WHITE)

        math1.next_to(title1, DOWN)
        math2.next_to(math1,DOWN)
        math2.scale(.9)
        math3.next_to(math2, DOWN)
        # endregion

        # region animations
        self.play(Write(title1))

        self.play(Write(math1[0]))
        self.play(Write(math2[0]))

        self.play(TransformMatchingTex(math2[0],math2[1]))
        self.play(TransformMatchingTex(math2[1], math2[2]))

        self.play(Circumscribe(math1[0][2],color=DX_COLOR))
        self.play(Circumscribe(math2[2][5],color=DX_COLOR))
        #self.play(math1[0][2:4].animate.shift(2*DOWN))
        self.play(Circumscribe(math1[0][2:4], color=DY_COLOR))
        self.play(Circumscribe(math2[2][5:7], color=DY_COLOR))

        self.play(FadeIn(math3[0]))
        self.play(TransformMatchingTex(math3[0],math3[1]))

        self.wait(1)

        self.play(Unwrite(title1), Unwrite(math3[1]), Unwrite(math2[2]))
        #endregion
        #endregion

        # region section2

        # region construction
        title2=Title("The Chain Rule")

        math4 = VGroup()
        math4 += MathTex(r"{{f(x+h)}}={{f_a \big (f_b(x+h) \big)}}")
        math4 += MathTex(r"{{f(x+h)}}=f_a \big( {{f_b(x)}}+ {{f_b(x+h)-f_b(x)}} \big)")
        math4 += MathTex(r"{{f(x+h)}}={{f_a \big( f_b(x) \big)}} + {{\big( f_b(x+h)-f_b(x) \big)}}{{f_a' \big( f_b(x) \big)}}")
        math4 += MathTex(r"{{f(x+h)}}={{f_a \big( f_b(x) \big)}} + {{h}}{{f_b'(x) f_a' \big( f_b(x) \big)}}")

        math5 = VGroup()
        math5 += MathTex(r"{{h}}{{f'(x)}}={{h}}{{f_b'(x)f_a' \big( f_b(x) \big)}}")
        math5 += MathTex(r"{{f'(x)}}={{f_b'(x)f_a' \big( f_b(x) \big)}}")

        mathvg2= VGroup(*math4,*math5)

        deep_set_color_by_tex(mathvg2, "h", DX_COLOR)
        deep_set_color_by_tex(mathvg2,"f(x+h)",Y1_COLOR)
        deep_set_color_by_tex(mathvg2, r"f_a \big (f_b(x+h) \big)", Y1_COLOR)
        deep_set_color_by_tex(mathvg2, r"f_b(x)", Y1_COLOR)
        deep_set_color_by_tex(mathvg2,r"f_a \big( f_b(x) \big)",Y0_COLOR)
        deep_set_color_by_tex(mathvg2,r"f_b(x)",Y0_COLOR)
        deep_set_color_by_tex(mathvg2, "f_b(x+h)-f_b(x)", DX_COLOR)
        deep_set_color_by_tex(mathvg2, r"\big( f_b(x+h)-f_b(x) \big)", DX_COLOR)
        deep_set_color_by_tex(mathvg2,r"f_a' \big( f_b(x) \big)",WHITE)


        math4.next_to(math1,DOWN)
        math5.next_to(math4,DOWN)

        # endregion

        # region animation
        self.play(Write(title2))
        self.play(Write(math4[0]))
        self.play(TransformMatchingTex(math4[0],math4[1]))
        self.play(TransformMatchingTex(math4[1], math4[2]))
        self.play(TransformMatchingTex(math4[2], math4[3]))

        self.play(Circumscribe(math1[0][2], color=DX_COLOR))
        self.play(Circumscribe(math4[3][4], color=DX_COLOR))
        self.play(Circumscribe(math1[0][2:4], color=DY_COLOR))
        self.play(Circumscribe(math4[3][4:6],color=DY_COLOR))

        self.play(Write(math5[0]))
        self.play(TransformMatchingTex(math5[0],math5[1]))

        self.wait(1)
        # endregion

        # endregion




if __name__ == '__main__':
    scene = DerivativesAlgebraic()
    scene.render(True)
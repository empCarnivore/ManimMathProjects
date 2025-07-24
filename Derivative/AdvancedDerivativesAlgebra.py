from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class AdvancedDerivativesAlgebraic(FormatedScene):
    def construct(self):
        # region colors
        Y0_COLOR = DARK_BLUE
        Y1_COLOR = GREEN
        DY_COLOR = YELLOW
        DX_COLOR = RED
        SLOPED_COLOR = CYAN1
        # endregion

        title1=Title("Higher Derivatives w Taylor Series")
        title2 = Title("Third Derivative Product Rule")
        title3 = Title("Third Derivative Chain Rule")

        math1 = VGroup()
        math1 += MathTex(r"{{y(x+h)}} = {{y(x)}} + {{h}} {{y'(x)}}")
        math1 += MathTex(r"{{y(x+h)}} = {{y(x)}} + {{h}} {{y'(x)}} + { {{h^2}} \over 2} {{y''(x)}} + { {{h^3}} \over 6} {{y'''(x)}} + ... + O \Big( { {{h^n}} \over n! } {{y^{(n)}(x)}} \Big)")
        math1[0].scale(.9)
        math1[1].scale(.9)

        math1.next_to(title1, DOWN)

        # region product rule
        math2 = VGroup()
        math2 += MathTex(r"{{f(x+h)}}={{f(x)}} + {{ {{h}} {{f'(x)}} }} + {{ { {{h^2}} \over 2} {{f''(x)}} }} + {{ { {{h^3}} \over 6 } {{f'''(x)}} }} + ...")
        math2[0].scale(.85)

        math3 = VGroup()
        math3 += MathTex(r"{{g(x+h)}}={{g(x)}} + {{ {{h}} {{g'(x)}} }} + {{ { {{h^2}} \over 2} {{g''(x)}} }} + {{ { {{h^3}} \over 6 } {{g'''(x)}} }} + ...")
        math3[0].scale(.85)

        math4 = VGroup()
        math4 += MathTex(r"{ {{h^3}} \over 6 } {{y'''(x)}} = {{\left.f(x)\right.}} {{ { {{h^3}} \over 6 } {{g'''(x)}} }} + {{ {{h}} {{f'(x)}} }} {{ { {{h^2}} \over 2 } {{g''(x)}} }} + {{ { {{h^2}} \over 2 } {{f''(x)}} }} {{ {{h}} {{g'(x)}} }} + {{ { {{h^3}} \over 6 } {{f'''(x)g(x)}} }}")
        math4 += MathTex(r"{ 1 \over 6 } {{y'''(x)}} = { 1 \over 6 } {{f(x) g'''(x)}} + { 1 \over 2 } {{f'(x)}} {{g''(x)}} + { 1 \over 2 } {{f''(x)}} {{g'(x)}} + { 1 \over 6 } {{f'''(x)g(x)}}")
        math4 += MathTex(r"{{y'''(x)}} = {{f(x) g'''(x)}} + 3 {{f'(x)}}{{g''(x)}} + 3 {{f''(x)}} {{g'(x)}} + {{f'''(x)g(x)}}")

        math4[0].scale(.8)
        math4[1].scale(.8)
        math4[2].scale(.8)

        math2.next_to(math1,DOWN)
        math3.next_to(math2, DOWN)
        math4.next_to(math3, DOWN)
        # endregion

        # region chain rule
        math5 = VGroup()
        math5 += MathTex(r"{{y(x+h)}}={{f \big( g(x+h) \big)}}")
        math5 += MathTex(r"{{y(x+h)}}=f \big( {{g(x)}} + {{\Delta g}} \big)")
        math5 += MathTex(r"{{y(x+h)}}={{f \big( g(x) \big)}} + {{\Delta g}} {{f' \big( g(x) \big)}} + {{{(\Delta g )^2}} \over 2} {{f'' \big( g(x) \big)}} + {{{(\Delta g )^3}} \over 6} {{f''' \big( g(x) \big)}} + ...")
        math5[0].scale(.85)
        math5[1].scale(.85)
        math5[2].scale(.8)

        math6 = VGroup()
        math6 += MathTex(r"{{\Delta g}} = {{h}} {{g'(x)}} + {{{h^2}} \over 2} {{g''(x)}} + {{{h^3}} \over 6} {{g'''(x)}} + ...")
        math6[0].scale(.85)

        math7 = VGroup()
        math7 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}}")
        math7 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}}")
        math7 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\Big( {{{h^2}} \over 2} g''(x) {{h}} g'(x) + {{h}} g'(x) {{{h^2}} \over 2} g''(x) \Big) \over 2} {{f'' \big( g(x) \big)}}")
        math7 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( {{h^3}} g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}}")
        math7 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( {{h^3}} g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}} + { \big( {{h}} g'(x) \big)^3 \over 6} {{f''' \big( g(x) \big)}}")
        math7 += MathTex(r"{1 \over 6} {{y'''(x)}} = \Big( { 1 \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}} + {g'(x)^3 \over 6} {{f''' \big( g(x) \big)}}")
        math7 += MathTex(r"{{y'''(x)}} = g'''(x) {{f' \big( g(x) \big)}} + 3 g'(x) g''(x) {{f'' \big( g(x) \big)}} + g'(x)^3 {{f''' \big( g(x) \big)}}")
        math7[0].scale(.85)
        math7[1].scale(.85)
        math7[2].scale(.8)
        math7[3].scale(.85)
        math7[4].scale(.75)
        math7[5].scale(.8)
        math7[6].scale(.85)

        math5.next_to(math1,DOWN)
        math6.next_to(math5,DOWN)
        math7.next_to(math6,DOWN)
        # endregion

        mathvg = VGroup(*math1,*math2,*math3,*math4,*math5,*math6,*math7)

        deep_set_color_by_tex(mathvg, r"h", DX_COLOR)
        deep_set_color_by_tex(mathvg,r"y(x+h)",Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"f(x+h)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"g(x+h)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"y(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"f(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"g(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"\Delta g", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"f \big( g(x+h) \big)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"f'", WHITE)
        deep_set_color_by_tex(mathvg, r"g'", WHITE)
        deep_set_color_by_tex(mathvg, r"\left.f(x)\right.", WHITE)

        self.play(Write(title1))
        self.play(Write(math1[1]))

        # region product rule animation
        self.play(Unwrite(title1))
        self.play(Write(title2))
        self.play(Write(math2[0]))
        self.play(Write(math3[0]))

        self.play(Write(math4[0][0:5]))

        self.play(Indicate(math2[0][2],color=ORANGE))
        self.play(Indicate(math3[0][12:15], color=PURPLE))

        self.play(Write(math4[0][5:10]))

        self.play(Indicate(math2[0][4:7], color=ORANGE))
        self.play(Indicate(math3[0][8:11], color=PURPLE))

        self.play(Write(math4[0][10:18]))

        self.play(Indicate(math2[0][8:11], color=ORANGE))
        self.play(Indicate(math3[0][4:7], color=PURPLE))

        self.play(Write(math4[0][18:26]))

        self.play(Indicate(math2[0][12:15], color=ORANGE))
        self.play(Indicate(math3[0][2], color=PURPLE))

        self.play(Write(math4[0][26:31]))

        self.play(TransformMatchingTex(math4[0],math4[1]))

        self.play(TransformMatchingTex(math4[1], math4[2]))

        self.wait(1)

        self.play(FadeOut(math4[2]),FadeOut(math3[0]),FadeOut(math2[0]),FadeOut(title2))
        # endregion

        #required because of bug

        self.play(Write(title3))

        self.play(Write(math5[0]))
        self.play(TransformMatchingTex(math5[0],math5[1]))
        self.play(TransformMatchingTex(math5[1], math5[2]))

        self.play(Write(math6[0]))

        self.play(Write(math7[0]))

        self.play(Indicate(math5[2][4:7], color=YELLOW))
        self.play(Indicate(math5[2][4],color=RED))
        self.play(Indicate(math6[0][10:13], color=ORANGE))

        self.play(TransformMatchingTex(math7[0],math7[1]))

        self.play(Indicate(math5[2][8:11], color=YELLOW))
        self.play(Indicate(math5[2][8], color=RED))
        self.play(Indicate(math6[0][2:5], color=ORANGE))
        self.play(Indicate(math6[0][6:9], color=PURPLE))
        self.wait()
        self.play(Indicate(math6[0][6:9], color=ORANGE))
        self.play(Indicate(math6[0][2:5], color=PURPLE))

        self.play(TransformMatchingTex(math7[1], math7[2]))
        self.wait()
        self.play(TransformMatchingTex(math7[2], math7[3]))

        self.play(Indicate(math5[2][12:15], color=YELLOW))
        self.play(Indicate(math5[2][12], color=RED))
        self.play(Indicate(math6[0][2:5], color=ORANGE))

        self.play(TransformMatchingTex(math7[3], math7[4]))

        self.play(TransformMatchingTex(math7[4], math7[5]))
        self.play(TransformMatchingTex(math7[5], math7[6]))

        self.wait()

if __name__ == '__main__':
    scene = AdvancedDerivativesAlgebraic()
    scene.render(True)
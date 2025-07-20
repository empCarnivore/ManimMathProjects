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

        math1 = VGroup()
        math1 += MathTex(r"{{y(x+h)}} = {{y(x)}} + {{h}} {{y'(x)}}")
        math1 += MathTex(r"{{y(x+h)}} = {{y(x)}} + {{h}} {{y'(x)}} + {{{h^2}} \over 2} {{y''(x)}} + {{{h^3}} \over 6} {{y'''(x)}} + ... + O \Big( {{{h^n}} \over n!} {{y^{(n)}(x)}} \Big)")
        math1[0].scale(.9)
        math1[1].scale(.9)

        math2 = VGroup()
        math2 += MathTex(r"{{y(x+h)}}={{f \big( g(x+h) \big)}}")
        math2 += MathTex(r"{{y(x+h)}}=f \big( {{g(x)}} + {{\Delta g}} \big)")
        math2 += MathTex(r"{{y(x+h)}}={{f \big( g(x) \big)}} + {{\Delta g}} {{f' \big( g(x) \big)}} + {{{(\Delta g )^2}} \over 2} {{f'' \big( g(x) \big)}} + {{{(\Delta g )^3}} \over 6} {{f''' \big( g(x) \big)}} + ...")
        math2[0].scale(.85)
        math2[1].scale(.85)
        math2[2].scale(.8)

        math3 = VGroup()
        math3 += MathTex(r"{{\Delta g}} = {{h}} {{g'(x)}} + {{{h^2}} \over 2} {{g''(x)}} + {{{h^3}} \over 6} {{g'''(x)}} + ...")
        math3[0].scale(.85)

        math4 = VGroup()
        math4 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}}")
        math4 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}}")
        math4 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\Big( {{{h^2}} \over 2} g''(x) {{h}} g'(x) + {{h}} g'(x) {{{h^2}} \over 2} g''(x) \Big) \over 2} {{f'' \big( g(x) \big)}}")
        math4 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( {{h^3}} g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}}")
        math4 += MathTex(r"{{{h^3}} \over 6} {{y'''(x)}} = \Big( { {{h^3}} \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( {{h^3}} g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}} + { \big( {{h}} g'(x) \big)^3 \over 6} {{f''' \big( g(x) \big)}}")
        math4 += MathTex(r"{1 \over 6} {{y'''(x)}} = \Big( { 1 \over 6} g'''(x) \Big) {{f' \big( g(x) \big)}} + {\big( g'(x) g''(x) \big) \over 2} {{f'' \big( g(x) \big)}} + {g'(x)^3 \over 6} {{f''' \big( g(x) \big)}}")
        math4 += MathTex(r"{{y'''(x)}} = g'''(x) {{f' \big( g(x) \big)}} + 3 g'(x) g''(x) {{f'' \big( g(x) \big)}} + g'(x)^3 {{f''' \big( g(x) \big)}}")
        math4[0].scale(.85)
        math4[1].scale(.85)
        math4[2].scale(.8)
        math4[3].scale(.85)
        math4[4].scale(.75)
        math4[5].scale(.8)
        math4[6].scale(.85)


        math1.next_to(title1,DOWN)
        math2.next_to(math1,DOWN)
        math3.next_to(math2,DOWN)
        math4.next_to(math3,DOWN)

        mathvg = VGroup(*math1,*math2,*math3,*math4)

        deep_set_color_by_tex(mathvg, r"h", DX_COLOR)
        deep_set_color_by_tex(mathvg,r"y(x+h)",Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"y(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"\Delta g", DX_COLOR)
        deep_set_color_by_tex(mathvg, r"f \big( g(x+h) \big)", Y1_COLOR)
        deep_set_color_by_tex(mathvg, r"g(x)", Y0_COLOR)
        deep_set_color_by_tex(mathvg, r"f'", WHITE)

        self.add(title1)
        self.add(math1[1])
        self.add(math2[2])
        self.add(math3[0])
        self.add(math4[6])


if __name__ == '__main__':
    scene = AdvancedDerivativesAlgebraic()
    scene.render(True)
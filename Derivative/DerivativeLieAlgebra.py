from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class DerivativeLieAlgebra(FormatedScene):
    def construct(self):
        # region colors
        Y0_COLOR = DARK_BLUE
        Y1_COLOR = GREEN
        DY_COLOR = YELLOW
        DX_COLOR = RED
        SLOPED_COLOR = CYAN1
        # endregion

        title1=Title("Lie Algebra Differentiation")

        math1 = VGroup()
        math1 += MathTex(r"{{[D,}}{{x}}{{]}} = {{D}} {{x}} - {{x}} {{D}}")
        math1 += MathTex(r"{{D}} {{x}} = {{[D,}}{{x}}{{]}} + {{x}} {{D}}")
        math1.next_to(title1,DOWN)

        math2 = VGroup()
        math2 += MathTex(r"{{[D,}}{{A}}{{]}} = -{{[}}{{A}}{{,D]}}")
        math2 += MathTex(r"{{D}}c = c{{D}} {{\implies}} {{[D,}}{{c}}{{A}}{{]}} = c{{[D,}}{{A}}{{]}}")
        math2 += MathTex(r"{{[D,}}{{A}}{{+}}{{B}}{{]}} = {{[D,}}{{A}}{{]}} + {{[D,}}{{B}}{{]}}")
        math2 += MathTex(r"{{[D,}}{{AB}}{{]}} = {{[D,}}{{A}}{{]}} {{B}} + {{A}} {{[D,}}{{B}}{{]}}")

        math3 = VGroup()
        math3 += MathTex(r"{{[D,}}{{f(g)}}{{]}} = {{f}}{{'}}{{(}}{{g}}{{)}}{{[D,}}{{g}}{{]}} + { {{f}}{{''}}{{(g)}} \over 2 } {{[[D,}}{{g}}{{],}}{{g}}{{]}}+...")
        math3 += MathTex(r"{{[D,}}{{g}}{{]}}{{g}}={{g}}{{[D,}}{{g}}{{]}} {{\implies}} {{[D,}}{{f(g)}}{{]}}={{f}}{{'}}{{(g)}}{{[D,}}{{g}}{{]}}")
        math3 += MathTex(r"{{[D,}}{{x}}{{]}}=1 {{\implies}} {{[D,}}{{f(}}{{x}}{{)}}{{]}}={{f}}{{'}}({{x}})")
        math3 += MathTex(r"{{[D,}}{{x}}{{]}}=1 {{\implies}} {{[}}{{g(}}{{D}}{{)}}{{,}}{{x}}{{]}}={{g}}{{'}}{{(}}{{D}}{{)}}")

        math4 = VGroup()
        math4 += MathTex(r"{{ad_D}}{{x}} = {{[D,}}{{x}}{{]}} {{\implies}} {{ad_D}} {{f(}}{{x}}{{)}} = {{ {d \over dx} }} {{f(}}{{x}}{{)}}={{f}}{{'}}{{(}}{{x}}{{)}}")
        math4 += MathTex(r"{{[{d \over dx},}}{{f(}}{{x}}{{)}}{{]}}={{f}}{{'}}{{(}}{{x}}{{)}} {{\implies}} {{ad_D}} = {{D}}")
        math4 += MathTex(r"{{D}}{{f(}}{{x}}{{)}}={{f}}{{'}}{{(}}{{x}}{{)}}")
        math4 += MathTex(r"{{D^2}}{{f(}}{{x}}{{)}}={{f}}{{''}}{{(}}{{x}}{{)}}")
        math4 += MathTex(r"{{D^3}}{{f(}}{{x}}{{)}}={{f}}{{'''}}{{(}}{{x}}{{)}}")
        math4 += MathTex(r"{{g(}}D{{)}}{{f(}}{{x}}{{)}} \text{is legitimized}")

        math5 = VGroup()
        math5 += MathTex(r" {{ad_D}} {{f(}}{{x}}{{)}} = {{f}}{{'}}{{(}}{{x}}{{)}} {{\iff}} {{Ad_{ \exp( D ) }}} {{f(}}{{x}}{{)}} = {{f(}}{{x}}+{{\left.1\left.}}{{)}}")
        math5 += MathTex(r" {{ad_{ xD} }} {{f(}}{{x}}{{)}} } = {{x}}{{f}}{{'}}{{(}}{{x}}{{)}} {{\iff}} {{Ad_{ \exp(xD) } }} {{f(}}{{x}}{{)}} = {{f(}}{{e}}{{x}}{{)}}")
        math5 += MathTex(r" {{ad_{ x\ln(x)D } }} {{f(}}{{x}}{{)}} = {{x}}{{\ln(}}{{x}}{{)}}{{f}}{{'}}{{(}}{{x}}{{)}} {{\iff}} {{Ad_{\exp( x\ln(x)D)} }} {{f(}}{{x}}{{)}} = {{f(}}{{x}}{{^e}}{{)}}")
        math5 += MathTex(r" {{ad_{ h(x)D } }} {{f(}}{{x}}{{)}} = {{h(}}{{x}}{{)}}{{f}}{{'}}{{(}}{{x}}{{)}} {{\iff}} {{Ad_{ \exp( h(x)D)} }} {{f}}{{(}}{{x}}{{)}} = {{f(}}{{q(}}{{x}}{{\left.)\right.}}{{)}}")

        mathvg=VGroup(*math1,*math2,*math3,*math4,*math5)
        deep_set_color_by_tex(mathvg, "x", DX_COLOR)
        deep_set_color_by_tex(mathvg,"D",SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "]", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, ",", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "[", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg,"f",DY_COLOR)
        deep_set_color_by_tex(mathvg, "g", DY_COLOR)
        deep_set_color_by_tex(mathvg, "A", DY_COLOR)
        deep_set_color_by_tex(mathvg, "B", DY_COLOR)
        deep_set_color_by_tex(mathvg, "(", DY_COLOR)
        deep_set_color_by_tex(mathvg, r")", DY_COLOR)
        deep_set_color_by_tex(mathvg, r"\left.)\right.", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "'", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "q", SLOPED_COLOR)

        deep_set_color_by_tex(mathvg, "+", WHITE)
        deep_set_color_by_tex(mathvg, "c", WHITE)
        deep_set_color_by_tex(mathvg, r"\iff  ", WHITE)
        deep_set_color_by_tex(mathvg, r"\left.1\left.", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "e", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "=", WHITE)
        deep_set_color_by_tex(mathvg, r"\implies", WHITE)
        deep_set_color_by_tex(mathvg, r"\over", WHITE)
        deep_set_color_by_tex(mathvg, "Ad", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, "ad", SLOPED_COLOR)
        deep_set_color_by_tex(mathvg, r"{d \over dx}", SLOPED_COLOR)

        self.add(title1)

        self.play(Write(math4[0]))
        self.play(FadeOut(math4[0]))
        self.play(Write(math4[1]))
        self.play(FadeOut(math4[1]))
        self.play(Write(math4[2]))
        self.play(FadeOut(math4[2]))
        self.play(Write(math4[3]))
        self.play(FadeOut(math4[3]))







if __name__ == '__main__':
    scene = DerivativeLieAlgebra()
    scene.render(True)
from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class DerivativesAlgebraic(FormatedScene):
    def construct(self):
        title1 = Title("Product Rule")
        math1 = VGroup()
        math1 += MathTex(r"f(x)=g(x)h(x)")
        math1 += MathTex(r"f(x+dx)=g(x+dx)h(x+dx)")
        math1 += MathTex(r"f(x+dx)=(g(x)+dx g'(x))(h(x)+dx h'(c))")
        math1 += MathTex(r"f(x+dx)=g(x)h(x)+dx g(x)h'(c)+dx g'(x)h(x)+dx^2 g'(x)h'(x)")
        math1 += MathTex(r"f(x+dx)=g(x)h(x)+dx g(x)h'(c)+dx g'(x)h(x)")
        math1 += MathTex(r"f(x+dx)=f(x)+dx (g(x)h'(c)+ g'(x)h(x))")
        math1 += MathTex(r"f(x+dx)-f(x)=dx (g(x)h'(c)+ g'(x)h(x))")
        math1 += MathTex(r"df(x)=dx (g(x)h'(c)+ g'(x)h(x))")
        math1 += MathTex(r"\frac{df(x)}{dx}=g(x)h'(c)+ g'(x)h(x)")
        math1 += MathTex(r"f'(x)=g(x)h'(c)+ g'(x)h(x)")

        title2=Title("Chain Rule")
        math2 = VGroup()
        math2 += MathTex(r"f(x)=g(h(x))")
        math2 += MathTex(r"f(x+dx)=g(h(x+dx))")
        math2 += MathTex(r"f(x+dx)=g(h(x)+dh)")
        math2 += MathTex(r"f(x+dx)=g(h(x))+dh g'(h(x))")
        math2 += MathTex(r"f(x+dx)=g(h(x))+dx h'(x)g'(h(x))")
        math2 += MathTex(r"f(x+dx)=f(x)+dx h'(x)g'(h(x))")
        math2 += MathTex(r"f(x+dx)-f(x)=dx h'(x)g'(h(x))")
        math2 += MathTex(r"df(x)=dx h'(x)g'(h(x))")
        math2 += MathTex(r"\frac{df(x)}{dx}=h'(x)g'(h(x))")
        math2 += MathTex(r"f'(x)=h'(x)g'(h(x))")


if __name__ == '__main__':
    scene = DerivativesAlgebraic()
    scene.render(True)
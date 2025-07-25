from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class DerivativesLieAlgebra(FormatedScene):
    def construct(self):
        title1=Title("Lie Algebra Differentiation")

        math1 = VGroup()
        math1 += MathTex(r"[D,x] = D x - x D")
        math1 += MathTex(r"D x = [D,x] + x D")

        math2 = VGroup()
        math2 += MathTex(r"[D,A]=-[A,D]")
        math2 += MathTex(r"Dc=cD \implies [D,cA]=c[D,A]")
        math2 += MathTex(r"[D,A+B]=[D,A]+[D,B]")
        math2 += MathTex(r"[D,AB]=[D,A]B+A[D,B]")

        math3 = VGroup()
        math3 += MathTex(r"[D,f(g)]=f'(g)[D,g]+\frac{f''(g)}{2}[[D,g],g]+...")
        math3 += MathTex(r"[D,g]g=g[D,g] \implies [D,f(g)]=f'(g)[D,g]")
        math3 += MathTex(r"[D,x]=1 \implies [D,f(x)]=f'(x)")
        math3 += MathTex(r"[D,x]=1 \implies [g(D),x]=g'(D)")

        math4 = VGroup()
        math4 += MathTex(r"ad_Dx = [D,x] \text{and} D=ad_D \implies Df(x)=f'(x)")
        math4 += MathTex(r"D^2f(x) = f''(x)")
        math4 += MathTex(r"D^3f(x) = f'''(x)")
        math4 += MathTex(r"D^3f(x) = f'''(x)")

        math5 = VGroup()
        math5 += MathTex(r" ad_D f(x) = f'(x) \iff Ad_D f(x) = f(x+1)")
        math5 += MathTex(r" ad_{xD} f(x) = xf'(x) \iff Ad_{xD} f(x) = f(ex)")
        math5 += MathTex(r" ad_{x\ln(x)D} f(x) = x\ln(x)f'(x) \iff Ad_{x\ln(x)D} f(x) = f(x^e)")
        math5 += MathTex(r" ad_{h(x)D} f(x) = h(x)f'(x) \iff Ad_{h(x)D} f(x) = f(g(x))")


if __name__ == '__main__':
    scene = DerivativesLieAlgebra()
    scene.render(True)
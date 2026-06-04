
from manim.utils.color.X11 import CYAN1

from FormatedScene import *

class ExplainError(FormatedScene):
    def construct(self):

        title= Title("Floating Point vs Reals")

        real_vs_float=VGroup()
        real_vs_float += Text("Real")
        real_vs_float += Text("Float")

        associative_property=VGroup()
        associative_property+=MathTex(
            r"(a \cdot b) \cdot c &= a \cdot ( b \cdot c)\\",
            r"(a + b) + c &= a + ( b + c)"
        )

        distributive_property=VGroup()
        distributive_property+=MathTex(r"c ( x + y ) = cx + cy")

        inverses_property=VGroup()
        inverses_property+=MathTex(
            r"\text{If } x \text{ exist, then } {x^{-1}} \text{ exist.} \\",
            r"a \cdot x \cdot x^{-1}=a \\",
            r"a + x - x = a"
        )

        bijective_property=VGroup()
        bijective_property+=MathTex(
            r"\text{If } a + x = b \text{, and } c \neq a\\",
            r"\text{then } c + x \neq b"
        )

        continuous_property=VGroup()
        continuous_property+=MathTex(
            r"\text{Given } a<b\\",
            r"\text{then } a<c<b \text{ exist}"
        )

if __name__ == '__main__':
    scene = ExplainError()
    scene.render(True)
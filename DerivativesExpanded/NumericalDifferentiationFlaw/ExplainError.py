
from manim.utils.color.X11 import CYAN1

from FormatedScene import *

class ExplainError(FormatedScene):
    def construct(self):

        title= Title("Floating Point's Failure to be Reals")

        associative_property=VGroup()
        associative_property+=MathTex(
            r"(a \cdot b) \cdot c & = a \cdot ( b \cdot c)\\",
            r"(a + b) + c &= a + ( b + c)"
        )
        associative_property += MathTex(
            r"(a \cdot b) \cdot c & \neq a \cdot ( b \cdot c)\\",
            r"(a + b) + c & \neq a + ( b + c)"
        )

        distributive_property=VGroup()
        distributive_property+=MathTex(r"c ( x + y ) = cx + cy")
        distributive_property += MathTex(r"c ( x + y ) \neq cx + cy")

        inverses_property=VGroup()
        inverses_property+=MathTex(
            r"a \cdot x \cdot x^{-1} = a \\",
            r"a + x - x = a"
        )

        inverses_property += MathTex(
            r"a \cdot x \cdot x^{-1} \neq a \\",
            r"a + x - x \neq a"
        )


        mathvg=VGroup(
            *associative_property,
            *distributive_property,
            *inverses_property,
        )

        associative_property.next_to(title,3*DOWN)
        distributive_property.next_to(associative_property,DOWN)
        inverses_property.next_to(distributive_property,DOWN)

        self.add(title,
                 associative_property[0],
                 distributive_property[0],
                 inverses_property[0],)

        self.wait(10)


if __name__ == '__main__':
    scene = ExplainError()
    scene.render(True)
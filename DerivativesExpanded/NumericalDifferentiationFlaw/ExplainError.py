
from manim.utils.color.X11 import CYAN1

from FormatedScene import *

class ExplainError(FormatedScene):
    def construct(self):

        title= Title("Floating Point's Failure to be Reals")

        associative_property_m=VGroup()
        associative_property_a = VGroup()
        associative_property_m+=MathTex(
            r"(a \cdot b) \cdot c & {{=}} a \cdot ( b \cdot c)"
        )
        associative_property_a+=MathTex(
            r"(a + b) + c & {{=}} a + ( b + c)"
        )
        associative_property_m += MathTex(
            r"(a \cdot b) \cdot c & {{\neq}} a \cdot ( b \cdot c)")
        associative_property_a += MathTex(
            r"(a + b) + c & {{\neq}} a + ( b + c)"
        )

        distributive_property=VGroup()
        distributive_property+=MathTex(r"c ( x + y ) {{=}} cx + cy")
        distributive_property += MathTex(r"c ( x + y ) {{\neq}} cx + cy")

        inverses_property_m=VGroup()
        inverses_property_a = VGroup()
        inverses_property_m+=MathTex(
            r"a \cdot x \cdot x^{-1} {{=}} a",)
        inverses_property_a += MathTex(
            r"a + x - x {{=}} a"
        )
        inverses_property_m += MathTex(
            r"a \cdot x \cdot x^{-1} {{\neq}} a",)
        inverses_property_a += MathTex(
            r"a + x - x {{\neq}} a"
        )

        texts=[
            associative_property_m,
            associative_property_a,
            distributive_property,
            inverses_property_m,
            inverses_property_a,
        ]

        mathvg=VGroup(
            *associative_property_m,
            *associative_property_a,
            *distributive_property,
            *inverses_property_m,
            *inverses_property_a,
        )

        associative_property_m.next_to(title,3*DOWN)
        associative_property_a.next_to(associative_property_m,  DOWN)
        distributive_property.next_to(associative_property_a,DOWN)
        inverses_property_m.next_to(distributive_property,DOWN)
        inverses_property_a.next_to(inverses_property_m, DOWN)


        self.play(Write(
            title,
        ))

        self.play(
            LaggedStart(
            *[
                Write(text[0]) for text in texts
            ]
            ,lag_ratio=.5)
        )

        self.play(Indicate(associative_property_m[0]),Indicate(associative_property_a[0]))

        self.wait()

        self.play(Indicate(distributive_property[0]))

        self.wait()

        self.play(Indicate(inverses_property_m[0]),Indicate(inverses_property_a[0]))

        self.wait()

        self.play(
            *[TransformByIndexMap(text[0],text[1],([2],[2])) for text in texts]
        )

        self.wait()


if __name__ == '__main__':
    scene = ExplainError()
    scene.render(True)
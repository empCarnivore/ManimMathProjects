from FormatedScene import *


class HAlgebra(FormatedScene):
    def construct(self):
        title = Title("Power Rule with Non-Commutative Algebra")

        the_core = VGroup()
        the_core += MathTex(r"f({{ x }}) = {{x^{ }}{{n}} } \implies f'({{ x }}) = {{ n }}{{ x^{}}{{ n }} - 1}")

        lie_algebra = VGroup()
        lie_algebra += MathTex(r"{{D}} {{x}} = 1 + {{x}} {{D}}")

        proof_by_induction = VGroup()
        proof_by_induction += MathTex(r"{{ D }} ({{x}} \cdot {{x^{ }} {{n}} - 1} ) {{=}} ({{D}} {{x}}) {{x^{ }} {{n}} - 1}")
        proof_by_induction += MathTex(r"{{ D }} ({{x}} \cdot {{x^{ }} {{n}} - 1} ) {{=}} (1 + {{x}} {{D}}) {{x^{ }} {{n}} - 1}")
        proof_by_induction += MathTex(r"{{ D }} {{x^{ }} {{n}} } {{=}} {{x^{ }} {{n}} - 1} + {{x}} {{D}} {{x^{ }} {{n}} - 1}")


if __name__ == '__main__':
    scene = HAlgebra()
    scene.render(True)
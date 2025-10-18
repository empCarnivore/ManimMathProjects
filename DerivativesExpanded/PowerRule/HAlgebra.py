from FormatedScene import *


class HAlgebra(FormatedScene):
    def construct(self):
        title = Title("Power Rule by Small Changes")

        the_core = VGroup()
        the_core += MathTex(r"f({{x}}) = {{x}}^{ {{n}} } \implies f'({{x}}) = {{?}}")
        the_core += MathTex(r"f({{x}}) = {{x}}^{ {{n}} } \implies f'({{x}}) = {{n}} {{x}}^{ {{n}} - 1}")

        the_source = VGroup()
        the_source += MathTex(r"f({{x}} + {{h}}) {{=}} {{( {{x}} + {{h}} )}}^{ {{n}} }")
        the_source += MathTex(r"f({{x}} + {{h}}) {{=}} {{( {{x}} + {{h}} )}} {{( {{x}} + {{h}} )}} ...")

        the_guild = VGroup()
        the_guild += MathTex(r"{{h}}f'({{x}}) = {{?}}")
        the_guild += MathTex(r"{{h}}f'({{x}}) = {{h}} {{x}}^{ {{n}} - 1} + {{...}}")
        the_guild += MathTex(r"{{h}}f'({{x}}) = {{h}} {{x}}^{ {{n}} - 1} + {{h}} {{x}}^{ {{n}} - 1} + {{...}}")
        the_guild += MathTex(r"{{h}}f'({{x}}) = {{n}} {{h}}{{x}}^{ {{n}} - 1}")
        the_guild += MathTex(r"f'({{x}}) = {{n}} {{x}}^{ {{n}} - 1}")





if __name__ == '__main__':
    scene = HAlgebra()
    scene.render(True)
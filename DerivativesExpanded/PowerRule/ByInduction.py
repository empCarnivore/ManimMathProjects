from FormatedScene import *


class ByInduction(FormatedScene):
    def construct(self):
        # region initialize
        title = Title("Power Rule with Non-Commutative Algebra")

        the_core = VGroup()
        the_core += MathTex(r"f({{ x }}) = {{x^{ }}{{n}} } \implies f'({{ x }}) = {{ n }}{{ x^{}}{{ n }} - 1}")

        lie_algebra = VGroup()
        lie_algebra += MathTex(r"{{D}} {{x}} = 1 + {{x}} {{D}}")

        proof_by_induction = VGroup()
        proof_by_induction += MathTex(r"{{ D }} ({{x}} \cdot {{x^{ }}{{n}} - 1} ) {{=}} ({{D}}{{x}}) {{x^{ }}{{n}} - 1}")
        proof_by_induction += MathTex(r"{{ D }} ({{x}} \cdot {{x^{ }}{{n}} - 1} ) {{=}} ({{1}} + {{x}}{{D}}) {{x^{ }}{{n}} - 1}")
        proof_by_induction += MathTex(r"{{ D }}{{ x^{ }}{{n} }}{{=}}{{x^{ }}{{n}} - 1} {{+}}{{x}}{{D}}{{x^{ }}{{n}} - 1}")

        finish = VGroup()
        finish += MathTex(r"{{n}}{{x^{ }}{{n}} - 1} {{=}}{{x^{ }}{{n}} - 1} + {{x}}{{(n-1)}}{{x^{ }}{{n}} - 2}")
        finish += MathTex(r"{{n}} = 1 \implies f'({{x}}) = 1")

        math_vg = VGroup(*the_core, *lie_algebra, *proof_by_induction, *finish)
        # endregion

        # region color
        x_color = RED
        D_color = PURPLE
        n_color = BLUE

        deep_set_color_by_tex(math_vg, r"x", x_color)
        deep_set_color_by_tex(math_vg, r"D", D_color)
        deep_set_color_by_tex(math_vg, r"n", n_color)
        # endregion

        # region arrange
        the_core.next_to(title, DOWN)
        lie_algebra.next_to(the_core,DOWN)
        proof_by_induction.next_to(lie_algebra,DOWN)
        finish[0].next_to(proof_by_induction,DOWN)
        finish[1].next_to(finish[0], DOWN)
        # endregion

        # region animations
        self.play(Write(title))

        self.play(Write(the_core[0]))

        self.play(Write(lie_algebra[0]))

        self.play(Write(proof_by_induction[0]))

        self.play(TransformByIndexMap(proof_by_induction[0],proof_by_induction[1], ([9,10],[11,12]), ([],[9,10]) ))
        self.wait()

        self.play(FadeOut(lie_algebra[0]))
        self.wait()

        self.play(TransformByIndexMap(proof_by_induction[1],proof_by_induction[2], (range(1,7),[1,2]), ([7],[3]), ([8],[]), ([13],[]), ([9,14,15,16],range(4,7)), ([10],[7]), ([11,12],[8,9]), (range(14,17),range(10,13)) ))
        self.wait()

        self.play(Write(finish[0]))
        self.wait()

        self.play(Write(finish[1]))
        self.wait()
        # endregion



if __name__ == '__main__':
    scene = ByInduction()
    scene.render(True)
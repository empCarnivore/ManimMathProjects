from FormatedScene import *


class Associations(FormatedScene):
    def construct(self):
        title = Title("More on this")

        power_rule_equation = VGroup()
        power_rule_equation += MathTex(r"f( {{x}} ) = { {{x^}}{{n}} \over {{n}}! } \implies f'( {{x}} ) = { {{x^{ }}{{n - 1} }} \over ({{n - 1}})! }")

        power_rule_iter = VGroup()
        power_rule_iter += MathTex(r"{{0}} \leftarrow {{1}} ...")
        power_rule_iter += MathTex(r"{{0}} \leftarrow {{1}} \leftarrow {{x}} ...")
        power_rule_iter += MathTex(r"{{0}} \leftarrow {{1}} \leftarrow {{x}} \leftarrow { {{x^{ }}{{2} }} \over {{2}} } ...")

        math_vg = VGroup(*power_rule_equation, *power_rule_iter)

        # region color
        x_color = RED
        n_color = BLUE

        deep_set_color_by_tex(math_vg, r"x", x_color)
        deep_set_color_by_tex(math_vg, r"n", n_color)
        deep_set_color_by_tex(math_vg, r"0", n_color)
        deep_set_color_by_tex(math_vg, r"1", n_color)
        deep_set_color_by_tex(math_vg, r"2", n_color)
        deep_set_color_by_tex(math_vg, r"3", n_color)
        deep_set_color_by_tex(math_vg, r"6", n_color)

        # endregion
        self.play(Write(title))

        self.play(Write(power_rule_equation[0]))
        self.wait()


if __name__ == '__main__':
    scene = Associations()
    scene.render(True)
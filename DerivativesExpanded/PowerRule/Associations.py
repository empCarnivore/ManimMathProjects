from FormatedScene import *


class Associations(FormatedScene):
    def construct(self):
        title = Title("More on this")

        power_rule_equation = VGroup()
        power_rule_equation += MathTex(r"f( {{x}} ) = { {{x^}}{{n}} \over {{n}}! } \implies f'( {{x}} ) = { {{x^{ }}{{n - 1} }} \over ({{n - 1}})! }")

        power_rule_iter = VGroup()
        power_rule_iter += MathTex(r"1 \leftarrow x")
        power_rule_iter += MathTex(r"x \leftarrow { x^2 \over 2 }")
        power_rule_iter += MathTex(r"{ x^2 \over 2 } \leftarrow { x^3 \over 6 }")

        taylor_series = VGroup()
        SHARED=r"{ {{h}}{{ ^{a} }} \over {{a}}! }  f{{ ^{(b)} }} ( {{x}} )"
        taylor_series += MathTex(r"f({{x}}+{{h}}) = \sum_{ {{a}}={{b}}={{c}} | {{c}} \in \mathbb{Z} }",
                                 SHARED)
        taylor_series += MathTex(r"{d \over d{{x}}} f({{x}}+{{h}}) = \sum_{ {{a}}={{c}},{{b}}={{c}}+1 | {{c}} \in \mathbb{Z} }",
                                 SHARED)
        taylor_series += MathTex(r"{d \over d{{h}}} f({{x}}+{{h}}) = \sum_{ {{a}}={{c}}-1,{{b}}={{c}} | {{c}} \in \mathbb{Z} }",
                                 SHARED)


        math_vg = VGroup(*power_rule_equation, *taylor_series)

        power_rule_equation.next_to(title,DOWN)
        power_rule_iter.arrange(DOWN)
        power_rule_iter.next_to(power_rule_equation,DOWN)
        taylor_series[0].next_to(title,DOWN)
        taylor_series[1].next_to(title,DOWN)
        taylor_series[2].next_to(taylor_series[1],DOWN)

        # region color
        x_color = RED
        n_color = BLUE
        h_color = YELLOW

        deep_set_color_by_tex(math_vg, r"x", x_color)
        deep_set_color_by_tex(math_vg, r"h", h_color)
        deep_set_color_by_tex(math_vg, r"n", n_color)
        deep_set_color_by_tex(math_vg, r"2", n_color)
        deep_set_color_by_tex(math_vg, r"3", n_color)
        deep_set_color_by_tex(math_vg, r"6", n_color)
        deep_set_color_by_tex(math_vg, r"c", n_color)

        # endregion
        self.play(Write(title))

        self.play(Write(power_rule_equation[0]))
        self.wait()

        for i in power_rule_iter:
            self.play(Write(i))
            self.wait()

        self.play(FadeOut(power_rule_equation[0]))
        self.wait()

        self.play(FadeOut(power_rule_iter))
        self.wait()

        self.play(Write(taylor_series[0]))
        self.wait()

        self.play(FadeOut(taylor_series[0]))
        self.wait()

        self.play(Write(taylor_series[1]))
        self.wait()

        self.play(Write(taylor_series[2]))
        self.wait()



if __name__ == '__main__':
    scene = Associations()
    scene.render(True)
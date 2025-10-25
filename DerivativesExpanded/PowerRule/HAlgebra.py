from FormatedScene import *


class HAlgebra(FormatedScene):
    def construct(self):

        # region initialize
        title = Title("Power Rule by Small Changes")

        the_core = VGroup()
        the_core += MathTex(r"f({{ x }}) = {{x^{ }}{{n}} } \implies f'({{ x }}) = {{ ? }}")
        the_core += MathTex(r"f({{ x }}) = {{x^{ }}{{n}} } \implies f'({{ x }}) = {{ n }}{{ x^{}}{{ n }} - 1}")

        the_source = VGroup()
        the_source += MathTex(r"f( {{ x }} + {{ h }} ) = {{ ( }}{{ x }} + {{ h }}{{ )^{ }}{{ n } }}")
        the_source += MathTex(r"f( {{ x }} + {{ h }} ) = {{ ( }}{{ x }} + {{ h }}{{ ) }}{{ ( }}{{ x }} + {{ h }}{{ ) }} ... ( {{ x }} + {{ h }}{{ ) }} \text{ | n times}")

        the_guide = VGroup()
        the_guide += MathTex(r"{{ h }}f'({{ x }}) = {{ ? }}")
        the_guide += MathTex(r"{{ h }}f'({{ x }}) = {{ h }}{{ x^{ }}{{ n }} - 1} + {{ ... }}")
        the_guide += MathTex(r"{{ h }}f'({{ x }}) = {{ h }}{{ x^{ }}{{n}} - 1} + {{ h }}{{ x^{ }}{{ n }} - 1} + {{ ... }}")
        the_guide += MathTex(r"{{ h }}f'({{ x }}) = {{ h }}{{ x^{ }}{{n}} - 1} + {{ h }}{{ x^{ }}{{ n }} - 1} + {{ ... }}{{ h }}{{ x^{ }}{{ n }} - 1} {{\text{ | n times} }}")
        the_guide += MathTex(r"{{ h }}f'({{ x }}) = {{ n }}{{ h }}{{ x^{ }}{{ n }} - 1}")
        the_guide += MathTex(r"f'({{ x }}) = {{n}}{{ x^{ }}{{n}} - 1}")

        math_vg = VGroup(*the_core, *the_source, *the_guide)
        # endregion

        # region color
        x_color = RED
        h_color = YELLOW
        n_color = BLUE

        deep_set_color_by_tex(math_vg,r"x",x_color)
        deep_set_color_by_tex(math_vg,r"h",h_color)
        deep_set_color_by_tex(math_vg,r"n",n_color)
        # endregion

        # region arrange
        the_core.next_to(title,DOWN)
        the_source.next_to(the_core,DOWN)
        the_guide.next_to(the_source,DOWN)
        # endregion

        # region animation
        self.play(Write(title))
        self.wait()

        self.play(Write(the_core[0]))
        self.wait()

        self.add(the_source[0])
        self.wait()

        self.play(Write(the_guide[0]))
        self.wait()

        self.play(TransformByIndexMap(the_source[0],the_source[1],(range(4,11),range(4,21))))
        self.wait()

        self.play(Indicate(the_source[1][8],color=h_color))
        self.play(Indicate(the_source[1][11],color=x_color),Indicate(the_source[1][16],color=x_color))
        self.wait()

        self.play(TransformByIndexMap(the_guide[0],the_guide[1],([4],range(4,9))))
        self.wait()

        self.play(Indicate(the_source[1][13], color=h_color))
        self.play(Indicate(the_source[1][6], color=x_color), Indicate(the_source[1][16], color=x_color))
        self.wait()

        self.play(TransformByIndexMap(the_guide[1], the_guide[2],([8],range(8,13))))
        self.wait()

        self.play(Indicate(the_source[1][18], color=h_color))
        self.play(Indicate(the_source[1][6], color=x_color), Indicate(the_source[1][11], color=x_color))
        self.wait()

        self.play(TransformByIndexMap(the_guide[2], the_guide[3],([12],range(12,18 ) ) ))
        self.wait()

        self.play(FadeOut(the_source[1]))
        self.wait()

        self.play(TransformByIndexMap(the_guide[3], the_guide[4],(range(4,18),range(4,9))))
        self.wait()

        self.play(TransformByIndexMap(the_guide[4], the_guide[5],([0],[]),([5],[]) ))
        self.wait()

        self.play(TransformByIndexMap(the_core[0],the_core[1],([8],range(8,12))))
        self.wait()








        # endregion


if __name__ == '__main__':
    scene = HAlgebra()
    scene.render(True)
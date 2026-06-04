
from manim.utils.color.X11 import CYAN1

from FormatedScene import *

class ExplainError(FormatedScene):
    def construct(self):

        title= Title("Floating Point vs Reals")

        RealFloat=VGroup()
        RealFloat += Text("Real")
        RealFloat += Text("Float")



if __name__ == '__main__':
    scene = ExplainError()
    scene.render(True)
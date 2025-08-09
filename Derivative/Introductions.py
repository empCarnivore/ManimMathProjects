
from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class Introductions(FormatedScene):
    def construct(self):
        title1 = Title(r"Goals:")

        text1 = VGroup()
        text1 += Tex(r"Introduce Differentiation and other topics in a novel way", color=RED)
        text1 += Tex(r"Derive Core and Complex behaviors", color=YELLOW)
        text1 += Tex(r"Build Connections, Curiosity, and Intuition", color=GREEN)
        text1 += Tex(r"Create a starting point for further research and videos",color=BLUE)

        text1.arrange(DOWN, buff=.5)
        text1.next_to(title1, DOWN)
        text1.shift(DOWN)

        self.play(Write(title1))

        for i in text1:
            self.play(Write(i))
            self.wait()

if __name__ == '__main__':
    scene = Introductions()
    scene.render(True)


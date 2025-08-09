
from manim.utils.color.X11 import CYAN1

from FormatedScene import *


class VidIntro(FormatedScene):
    def construct(self):
        text1=VGroup()
        text1+=Text(r"Abstract Math",color=BLUE)
        text1+=Text(r"AbsMath",color=BLUE)

        self.play(Write(text1[0]))
        self.wait()
        self.play(Transform(text1[0],text1[1]))
        self.play(Write(text1[1]))
        self.wait()

if __name__ == '__main__':
    scene = VidIntro()
    scene.render(True)

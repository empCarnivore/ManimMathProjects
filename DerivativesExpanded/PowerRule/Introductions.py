from FormatedScene import *


class Introductions(FormatedScene):
    def construct(self):
        title1 = Title(r"Goals:")

        text1 = VGroup()
        text1 += Tex(r"Derive and Prove the product rule", color=RED)
        text1 += Tex(r"Use the small changes method", color=GREEN)
        text1 += Tex(r"Use induction and algebraic methods", color=BLUE)

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

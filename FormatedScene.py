# Graphics and Animation
from manim import *
import os
import numpy


def lambda_circle(n):
    """
        lambda_circle(2)(t)=(cos(2*t),sin(2*t))
    """
    return lambda t: (numpy.cos(n * t), numpy.sin(n * t), 0)


class FormatedScene(Scene):
    def write_and_fade(self, *stuff, run_time=5, wait_time=10, group_transformations=(), **kwargs):
        """
        writes stuff taking a default of 5 seconds with kwargs passed to play and
        waits a default of 10 seconds
        then it fades
        """
        stuff_group = VGroup(*stuff)
        stuff_group.arrange(DOWN, aligned_edge=LEFT)
        for transformations in group_transformations:
            transformations(stuff_group)

        self.add(stuff_group)
        self.play(Write(stuff_group), run_time=run_time, **kwargs)

        self.wait(wait_time)
        self.play(FadeOut(stuff_group))

    def setup(self):
        """
        This is meant to be implemented by any scenes which
        are commonly subclassed, and have some common setup
        involved before the construct method is called.
        """
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "..//media/images/BackGround2.jpg"
        abs_file_path = os.path.join(script_dir, rel_path)

        background = ImageMobject(abs_file_path)
        background.height = self.camera.frame_height
        background.width = self.camera.frame_width
        background.set_opacity(.15)
        self.add(background)
        return super().setup()
# Graphics and Animation
import copy

from manim import *
from MF_Tools import *
import os
import numpy

def lambda_circle(n):
    """
        lambda_circle(2)(t)=(cos(2*t),sin(2*t))
    """
    return lambda t: (numpy.cos(n * t), numpy.sin(n * t), 0)

def deep_set_color_by_tex(your_object,text,your_color):
    if isinstance(your_object,MathTex):
        your_MathTex=your_object
        your_MathTex.set_color_by_tex(text,your_color)
    elif isinstance(your_object,VGroup):
        your_VGoup = your_object
        for object_of_your_VGroup in your_VGoup:
            deep_set_color_by_tex(object_of_your_VGroup,text,your_color)

class FormatedScene(Scene):

    def transform_arranged_group_by_matching_index(self,mobject_from: VMobject, mobject_to: VMobject, TheTransformation,time_scaler=1):
        if len(mobject_from) != len(mobject_to):
            raise ValueError("Length mismatch")

        intermediate_to = copy.deepcopy(mobject_to)
        intermediate_from = copy.deepcopy(mobject_from)

        # resize by bigger object
        for index in range(len(mobject_from)):
            if mobject_from[index].width > intermediate_to[index].width:
                mobject_to[index].stretch_to_fit_width(mobject_from[index].width)
            elif mobject_from[index].width < intermediate_to[index].width:
                intermediate_from[index].stretch_to_fit_width(intermediate_to[index].width)
        mobject_to.arrange_submobjects()
        intermediate_from.arrange_submobjects()
        for index in range(len(mobject_from)):
            mobject_to[index].become(intermediate_to[index])
            intermediate_from[index].become(mobject_from[index])

        mobject_to.move_to(intermediate_to)
        intermediate_from.move_to(mobject_from)

        first_position_shift = [mobject_from[index].animate.become(intermediate_from[index]) for index in
                                range(len(mobject_from))]
        the_transformation = [TheTransformation(mobject_from[index], mobject_to[index]) for index in
                              range(len(mobject_from))]
        last_position_shift = [mobject_to[index].animate.become(intermediate_to[index]) for index in
                               range(len(mobject_from))]
        self.play(AnimationGroup(first_position_shift),run_time=.25)
        self.play(AnimationGroup(*the_transformation),run_time=.5)
        self.play(AnimationGroup(FadeOut(mobject_from, run_time=0), last_position_shift),run_time=.25)

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
        rel_path = "media/images/BackGround2.jpg"
        abs_file_path = os.path.join(script_dir, rel_path)

        background = ImageMobject(abs_file_path)
        background.height = self.camera.frame_height
        background.width = self.camera.frame_width
        background.set_opacity(.15)
        self.add(background)
        return super().setup()
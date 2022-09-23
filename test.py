from manim import *

# https://stackoverflow.com/questions/66642657/is-it-possible-to-run-manim-programmatically-and-not-from-the-command-line
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file

Quality_16_9 = {"LOW": [512, 288],
                "MEDIUM": [768, 432],
                "HD": [1280, 720],
                "FULL_HD": [1920, 1080],
                "4K": [4096, 2160],
                "8K": [7680, 4320]
                }
FrameRate = 60
Quality = "HD"

# https://gitlab1.cs.cityu.edu.hk/gsalter2/dockers/-/blob/37836f254c8fcc10f70b991eb0c6f5c31378bcb4/manim/docs/source/tutorials/configuration.rst
config.background_color = BLACK
config.frame_rate = FrameRate
config.pixel_width, config.pixel_height = Quality_16_9[Quality]


class Graphing(Scene):
    def construct(self):

        plane = (
            NumberPlane(x_range=[-3,3,1], y_range=[0,16,4])
            .to_edge(DOWN)
            .add_coordinates()
        )

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x: x**2, x_range=[-3,3], color=GREEN)
        func_label = (
            MathTex("f(x)=x^2")
            .scale(0.6).next_to(parab, UR, buff=0.5)
            .set_color(GREEN)
            .set_color(GREEN)
        )

        area = plane.get_riemann_rectangles(graph=parab, x_range=[-2,3], dx=0.2, stroke_width=0.1, stroke_color=GREEN)

        self.play(DrawBorderThenFill(plane))
        self.play(Write(VGroup(labels,parab,func_label)), run_time=3)
        self.wait()
        self.play(Create(area))
        self.wait()

        

# if you implement this program on PyCharm, you will not save the movie.
# use this command instead to save rendered images
# manim -pql main.py FollowingGraphCamera
if __name__ == '__main__':
    scene = Graphing()
    scene.render()  # That's it!
    
    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)

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
FrameRate = 15

# https://gitlab1.cs.cityu.edu.hk/gsalter2/dockers/-/blob/37836f254c8fcc10f70b991eb0c6f5c31378bcb4/manim/docs/source/tutorials/configuration.rst
config.background_color = BLACK
config.frame_rate = FrameRate
config.pixel_width, config.pixel_height = Quality_16_9["LOW"]


class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3,3), y_range=(-3,3))
        curve=ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve,x_range=(-2,0))
        self.play(Create(ax))
        self.play(Write(curve), run_time=1)
        self.play(FadeIn(area), run_time=1)

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))
        self.wait()
        
        
        
        

# if you implement this program on PyCharm, you will not save the movie.
# use this command instead to save rendered images
# manim -pql main.py FollowingGraphCamera
if __name__ == '__main__':
    scene = SquareToCircle()
    scene.render()  # That's it!
    
    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)

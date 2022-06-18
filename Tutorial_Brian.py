from manim import *

# https://stackoverflow.com/questions/66642657/is-it-possible-to-run-manim-programmatically-and-not-from-the-command-line
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file

Quality_16_9 = {"LOW"       :[512,288],
                "MEDIUM"    :[768,432],
                "HD"        :[1280,720],
                "FULL_HD"   :[1920,1080],
                "4K"        :[4096,2160],
                "8K"        :[7680,4320]
                }
FrameRate = 15

# https://gitlab1.cs.cityu.edu.hk/gsalter2/dockers/-/blob/37836f254c8fcc10f70b991eb0c6f5c31378bcb4/manim/docs/source/tutorials/configuration.rst
config.background_color = BLACK
config.frame_rate = FrameRate
config.pixel_width, config.pixel_height = Quality_16_9["LOW"]

class Test(Scene):
    def construct(self):

        circ = Circle(radius = 2.4, color = RED)

        self.play(Create(circ))
        self.wait()

class Pith(Scene):
    def construct(self):
        rect = Rectangle(height=3.0, width=4.0, stroke_color=BLUE)
        sq = Square(
            side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75
        )

        self.play(Create(rect), run_time=2)
        self.wait()

class Texting(Scene):
    def construct(self):
        name = Tex("Haruki").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_opacity=0.75, fill_color=GREEN).shift(LEFT*3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq))
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2),tri.animate.to_edge(DL), run_time=3)
        self.wait()

class Errors(Scene):
    def construct(self):

        c = Circle(radius=2, stroke_color=WHITE, stroke_opacity=0.75, fill_color=WHITE, fill_opacity=0.75)

        self.play(FadeIn(c), run_time=3)

class Library(Scene):
    def construct(self):

        ax = Axes(x_range=[0,5],y_range=[0,20])
        self.play(Create(ax))

class Getters(Scene):
    def construct(self):

        rect = Rectangle(height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda : Line(
                start=rect.get_bottom(), end=circ.get_top(), buff=0.2
            ).add_tip()
        )

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()

        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)

class Upddaters(Scene):
    def construct(self):

        num = MathTex("ln(2)")
        box = always_redraw(
            lambda:SurroundingRectangle(
                num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5
            )
        )

        name = always_redraw(lambda: Tex("Haruki").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT*2), run_Time=2)
        self.wait()

class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(3.5)

        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time=3, rate_function=smooth)
        self.wait()

class Graphing(Scene):
    def construct(self):

        plane = (
            NumberPlane(x_range=[-4,4,2], x_length=7, y_range=[0,16,4], y_length=5)
            .to_edge(DOWN)
            .add_coordinates()
        )

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x: x**2, x_range=[-4,4], color=GREEN)
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
        
        
class UpdaterGraph(Scene):
    def construct(self):
        k= ValueTracker(-3)

        ax = Axes(x_range=[-3,3,1], y_range=[-10,10,2], x_length=10, y_length=6).to_edge(DOWN).add_coordinates().set_color(WHITE)

        func = ax.plot(lambda x: 0.5*x**3-1*x, x_range=[-3,3], color=BLUE)

        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=k.get_value(),
                graph=func,
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=3
            )
        )

        pt = always_redraw(
            lambda : Dot().move_to(ax.c2p(k.get_value(),func.underlying_function(k.get_value())))
        )

        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(3), run_time=3)

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





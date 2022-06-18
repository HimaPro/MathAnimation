from manim import *

# https://stackoverflow.com/questions/66642657/is-it-possible-to-run-manim-programmatically-and-not-from-the-command-line
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file

Quality_16_9 = {"LOW"       :[512,288],
                "MEDIUM"    :[768,432],
                "HD"        :[1280,720],
                "FULL_HD"   :[1920,1080],
                "4K"        :[4096,2160],
                "8K"        :[7680,4320]}
FrameRate = 15

# https://gitlab1.cs.cityu.edu.hk/gsalter2/dockers/-/blob/37836f254c8fcc10f70b991eb0c6f5c31378bcb4/manim/docs/source/tutorials/configuration.rst
config.background_color = WHITE
config.frame_rate = FrameRate
config.pixel_width, config.pixel_height = Quality_16_9["LOW"]

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        # self.camera.background_color=WHITE

        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        ax.color=BLACK
        # ax = Axes(x_range=[-1, 10], y_range=[-1, 10]).set_color(RED)

        graph = ax.plot(lambda x: np.sin(x), color=GRAY, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph), color=BLUE)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph), color=GREEN)

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))



# if you implement this program on PyCharm, you will not save the movie.
# use this command instead to save rendered images
# manim -pql main.py FollowingGraphCamera
if __name__ == '__main__':
    scene = FollowingGraphCamera()
    scene.render()  # That's it!

    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)

from manim import *

# https://stackoverflow.com/questions/66642657/is-it-possible-to-run-manim-programmatically-and-not-from-the-command-line
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.background_color=WHITE

        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10]).set_color(BLACK)
        # ax.color=BLACK
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI]).set_color(BLACK)
        # graph.set_color(BLACK)

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph)).set_color(BLUE)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph)).set_color(GREEN)

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))


if __name__ == '__main__':
    scene = FollowingGraphCamera()
    scene.render()  # That's it!

    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)

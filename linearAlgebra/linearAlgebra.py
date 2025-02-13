from manim import *
import numpy as np

def planeTransformation2D(scene, matrix, size=30):
    # Plane
    grid = NumberPlane(
        x_range=[-size, size],
        y_range=[-size, size],
    )
    
    scene.play(
        scene.camera.frame.animate.scale(3)  # Reduce el marco para hacer zoom out
    )
    
    # Crear la cuadrícula
    scene.play(
        Create(grid, run_time=3, lag_ratio=0.1),
    )    
    scene.wait()

    scene.play(
        grid.animate.apply_function(
        lambda p: np.array([
        matrix[0][0] * p[0] + matrix[0][1] * p[1],
        matrix[1][0] * p[0] + matrix[1][1] * p[1],
        p[2],
        ])
    ),
    run_time=5,
    )
    scene.wait()

def graphVector(scene, vector):
    pass

class test (MovingCameraScene):
    def construct(self):
        planeTransformation2D(self, [[2, 0], [1, -2]])
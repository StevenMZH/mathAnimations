from manim import *
import numpy as np

class OpeningManim(Scene):
    def construct(self):
        # Crear la cuadrícula
        grid = NumberPlane(
            x_range=[-30, 30],  # Ajustar el rango del eje X
            y_range=[-30, 30],  # Ajustar el rango del eje Y
        )
        grid_title = Tex("Unit 2: Linear Transformation", font_size=72)

        self.add(grid, grid_title)
        self.play(
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        # Aplicar la transformación lineal de shear (sesgo)
        shear_factor = 0.5  # Factor de shear, puedes modificar este valor
        self.play(
            grid.animate.apply_function(
                lambda p: np.array([
                    p[0] + 2 * p[1],  # Desplazamiento en X según Y
                    p[1] + 2 * p[0],  # No cambiar la coordenada Y
                    p[2],  # No cambiar la coordenada Z
                ])
            ),
            run_time=5,
        )
        self.wait()

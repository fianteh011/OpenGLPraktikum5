from matrix import Matrix
from math import sin, cos, radians

class Camera:
    def __init__(self):
        self.camera_pos = Matrix.Vec3(0.0, 4.0, 3.0)
        self.camera_front = Matrix.Vec3(0.0, 0.0, -1.0)
        self.camera_up = Matrix.Vec3(0.0, 1.0, 0.0)
        self.camera_right = Matrix.Vec3(1.0, 0.0, 0.0)

        self.mouse_sensitivity = 0.01
        self.jaw = -90
        self.pitch = 0

    def get_view_matrix(self):
        return Matrix.makeLook_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
    

    def process_mouse_movement(self, xoffset, yoffset, constrain_pitch=True):
        xoffset *= self.mouse_sensitivity
        yoffset *= self.mouse_sensitivity

        self.jaw += xoffset
        self.pitch += yoffset

        if constrain_pitch:
            if self.pitch > 45:
                self.pitch = 45
            if self.pitch < -45:
                self.pitch = -45

        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = Matrix.Vec3(0.0, 0.0, 0.0)
        front[0] = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front[1] = sin(radians(self.pitch))
        front[2] = sin(radians(self.jaw)) * cos(radians(self.pitch))

        # Kamerakoordinatensystem (siehe CG_6_SoSe21, Folie 5)
        self.camera_front = Matrix.normalise(front)
        self.camera_right = Matrix.normalise(Matrix.cross(self.camera_front, Matrix.Vec3(0.0, 1.0, 0.0)))
        self.camera_up = Matrix.normalise(Matrix.cross(self.camera_right, self.camera_front))

    # Camera method for the WASD movement of the camera
    def process_keyboard(self, direction, velocity):
        if direction == "FORWARD":
            self.camera_pos += self.camera_front * velocity
        if direction == "BACKWARD":
            self.camera_pos -= self.camera_front * velocity
        if direction == "LEFT":
            self.camera_pos -= self.camera_right * velocity
        if direction == "RIGHT":
            self.camera_pos += self.camera_right * velocity

















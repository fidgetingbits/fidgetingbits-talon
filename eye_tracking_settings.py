from talon import app
from talon.types import Point2d
from talon_plugins import eye_zoom_mouse

if app.platform == "mac":
    eye_zoom_mouse.config.screen_area = Point2d(100, 75)
    eye_zoom_mouse.config.img_scale = 6
elif app.platform == "win":
    eye_zoom_mouse.config.screen_area = Point2d(200, 150)
    eye_zoom_mouse.config.img_scale = 4.5
elif app.platform == "linux":
    eye_zoom_mouse.config.screen_area = Point2d(200, 150)
    eye_zoom_mouse.config.img_scale = 6

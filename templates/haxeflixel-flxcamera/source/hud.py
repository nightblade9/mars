from flixel import FlxSprite
from flixel.group import FlxGroup
from flixel.text import FlxText
from flixel.util import FlxColor
import math

class Hud(FlxGroup):
    def __init__(self):
        super(Hud, self).__init__()
        self.width = 200
        self.height = 180

        x = 10000

        self.background = FlxSprite(x, 0)
        self.background.makeGraphic(self.width, self.height, FlxColor.BLACK)
        self.add(self.background)

        x += 6
        start_y = 10

        self.add(FlxText(x, start_y, self.width, "[W,A,S,D] or arrows to control the orb.")) 

        self.add(FlxText(x, start_y + 20, 300, "[H] to change follow style."))
        self._txt_style = FlxText(x, start_y + 33, self.width, "LOCKON")
        self._add_green_text(self._txt_style)

        self.add(FlxText(x, start_y + 55, self.width, "[U] or [J] to change lerp."))
        self._txt_lerp = FlxText(x, start_y + 68, self.width, "Camera lerp: 1")
        self._add_green_text(self._txt_lerp)

        self.add(FlxText(x, start_y + 95, self.width, "[I] or [K] to change lead."))
        self._txt_lead = FlxText(x, start_y + 108, self.width, "Camera lead: 0")
        self._add_green_text(self._txt_lead)

        self.add(FlxText(x, start_y + 135, self.width, "[O] or [L] to change zoom."))
        self._txt_zoom = FlxText(x, start_y + 148, self.width, "Camera zoom: 1")
        self._add_green_text(self._txt_zoom)

    def _add_green_text(self, text):
        text.setFormat(None, 11, 0x55FF55)
        self.add(text)

    def update_style(self, string):
        self._txt_style.text = string

    def update_cam_lerp(self, lerp):
        self._txt_lerp.text = "Camera lerp: {}".format(lerp)

    def update_cam_lead(self, lead):
        self._txt_lead.text = "Camera lead: {}".format(lead)

    def update_zoom(self, zoom):    
        self._txt_zoom.text = "Camera Zoom: {}".format(math.floor(zoom * 10) / 10)

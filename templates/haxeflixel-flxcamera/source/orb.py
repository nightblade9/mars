from flixel import FlxG
from flixel import FlxSprite
from flixel.addons.nape import FlxNapeSprite
from openfl import Assets

class Orb(FlxNapeSprite):
		
	def __init__(self):
		super(Orb, self).__init__(FlxG.width / 2, FlxG.height / 2, "assets/Orb.png")
		self.createCircularBody(18)
		self.body.allowRotation = false
		self.setDrag(0.98, 1)
		self._shadow = None
	
	@haxe:override
	def update(elapsed):
		super.update(elapsed)
		
		if (FlxG.camera.target != null && FlxG.camera.followLead.x == 0): # target check is used for debug purposes.
			x = Math.round(x) # Smooths camera and orb shadow following. Does not work well with camera lead.
			y = Math.round(y) # Smooths camera and orb shadow following. Does not work well with camera lead.
		
		self._shadow.x = round(x)
		self._shadow.y = round(y)
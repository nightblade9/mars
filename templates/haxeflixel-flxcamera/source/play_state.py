
import flash.Lib
import flash.display.BlendMode
import flixel.FlxCamera
import flixel.FlxG
import flixel.FlxSprite
import flixel.FlxState
import flixel.addons.nape.FlxNapeSpace
import flixel.math.FlxMath
import flixel.math.FlxRect
import flixel.util.FlxColor
import nape.geom.Vec2
import openfl.Assets
# WAS: using flixel.util.FlxSpriteUtil
import flixel.util.FlxSpriteUtil

class PlayState(FlxState):

    # Demo arena boundaries
    _LEVEL_MIN_X = 0
    _LEVEL_MAX_X = 0
    _LEVEL_MIN_Y = 0
    _LEVEL_MAX_Y = 0

    def __init__(self):
        self._orb = None
        self._orb_shadow = None
        self._hud = None
        self._hud_cam = None
        self._overlay_camera = None
        self._deadzone_overlay = None

    @haxe:override
    def create(): 
        
        FlxNapeSpace.init()
        
        PlayState._LEVEL_MIN_X = -FlxG.stage.stageWidth / 2
        PlayState._LEVEL_MAX_X = FlxG.stage.stageWidth * 1.5
        PlayState._LEVEL_MIN_Y = -FlxG.stage.stageHeight / 2
        PlayState._LEVEL_MAX_Y = FlxG.stage.stageHeight * 1.5
        
        super(PlayState, self).create()
        
        FlxG.mouse.visible = False
        
        FlxNapeSpace.velocityIterations = 5
        FlxNapeSpace.positionIterations = 5
        
        self._createFloorTiles()
        FlxNapeSpace.createWalls(LEVEL_MIN_X, LEVEL_MIN_Y, LEVEL_MAX_X, LEVEL_MAX_Y)
        # Walls border.
        self.add(FlxSprite(-FlxG.width / 2, -FlxG.height / 2, "assets/Border.png"))
        
        # Player orb
        self._orb_shadow = FlxSprite(FlxG.width / 2, FlxG.height / 2, "assets/self._orb_shadow.png")
        self._orb_shadow.centerOffsets()
        self._orb_shadow.blend = BlendMode.MULTIPLY
        
        self.orb = Orb()
        
        self.add(self._orb_shadow)
        self.add(self.orb)
        
        self.orb.shadow = self._orb_shadow
        
        # Other orbs
        for i in range(5):
        
            otherself._orb_shadow = FlxSprite(100, 100, "assets/Otherself._orb_shadow.png")
            otherself._orb_shadow.centerOffsets()
            otherself._orb_shadow.blend = BlendMode.MULTIPLY
            
            otherOrb = Orb()
            otherOrb.loadGraphic("assets/OtherOrb.png", True, 140, 140)
            otherOrb.createCircularBody(50)
            otherOrb.setBodyMaterial(1, 0.2, 0.4, 0.5)
            otherOrb.antialiasing = True
            otherOrb.setDrag(1, 1)
            
            self.add(otherself._orb_shadow)
            self.add(otherOrb)
            
            otherOrb.shadow = otherself._orb_shadow
            
            if i == 0: 
				otherOrb.body.position.setxy(320 - 400, 240 - 400)
				otherOrb.animation.frameIndex = 0
			elif i == 1: 
				otherOrb.body.position.setxy(320 + 400, 240 - 400) 
				otherOrb.animation.frameIndex = 4
			elif i == 2:
				otherOrb.body.position.setxy(320 + 400, 240 + 400) 
				otherOrb.animation.frameIndex = 3
			elif i == 3:
				otherOrb.body.position.setxy(-300, 240) 
				otherOrb.animation.frameIndex = 2
			elif i == 4:
				otherOrb.body.position.setxy(0, 240 + 400) 
				otherOrb.animation.frameIndex = 1
		
            otherOrb.body.velocity.setxy(FlxG.random.int(75, 150), FlxG.random.int(75, 150))

        self._hud = HUD()
        self.add(self._hud)

        # Camera Overlay
        self._deadzone_overlay = FlxSprite(-10000, -10000)
        self._deadzone_overlay.makeGraphic(FlxG.width, FlxG.height, FlxColor.TRANSPARENT, True)
        self._deadzone_overlay.antialiasing = True

        self._overlay_camera = FlxCamera(0, 0, 640, 720)
        self._overlay_camera.bgColor = FlxColor.TRANSPARENT
        self._overlay_camera.follow(self._deadzone_overlay)
        FlxG.cameras.self.add(self._overlay_camera)
        self.add(self._deadzone_overlay)
        
        FlxG.camera.setScrollBoundsRect(LEVEL_MIN_X, LEVEL_MIN_Y,
            LEVEL_MAX_X + Math.abs(LEVEL_MIN_X), LEVEL_MAX_Y + Math.abs(LEVEL_MIN_Y), True)
        FlxG.camera.follow(orb, LOCKON, 1)
        self._drawDeadzone() # now that deadzone is present
        
        self._hud_cam = FlxCamera(440, 0, self._hud.width, self._hud.height)
        self._hud_cam.zoom = 1 # For 1/2 zoom out.
        self._hud_cam.follow(self._hud.background, FlxCameraFollowStyle.NO_DEAD_ZONE)
        self._hud_cam.alpha = .5
        FlxG.cameras.self.add(self._hud_cam)
    
    
    def _drawDeadzone(self): 
    
        self._deadzone_overlay.fill(FlxColor.TRANSPARENT)
        dz = FlxG.camera.deadzone
        if dz == None:
            return

        lineLength = 20
        lineStyle = LineStyle(color = FlxColor.WHITE, thickness = 3)
        
        # adjust points slightly so lines will be visible when at screen edges
        dz.x += lineStyle.thickness / 2
        dz.width -= lineStyle.thickness
        dz.y += lineStyle.thickness / 2
        dz.height -= lineStyle.thickness
        
        # Left Up Corner
        self._deadzone_overlay.drawLine(dz.left, dz.top, dz.left + lineLength, dz.top, lineStyle)
        self._deadzone_overlay.drawLine(dz.left, dz.top, dz.left, dz.top + lineLength, lineStyle)
        # Right Up Corner
        self._deadzone_overlay.drawLine(dz.right, dz.top, dz.right - lineLength, dz.top, lineStyle)
        self._deadzone_overlay.drawLine(dz.right, dz.top, dz.right, dz.top + lineLength, lineStyle)
        # Bottom Left Corner
        self._deadzone_overlay.drawLine(dz.left, dz.bottom, dz.left + lineLength, dz.bottom, lineStyle)
        self._deadzone_overlay.drawLine(dz.left, dz.bottom, dz.left, dz.bottom - lineLength, lineStyle)
        # Bottom Right Corner
        self._deadzone_overlay.drawLine(dz.right, dz.bottom, dz.right - lineLength, dz.bottom, lineStyle)
        self._deadzone_overlay.drawLine(dz.right, dz.bottom, dz.right, dz.bottom - lineLength, lineStyle)
    
    
    def setZoom(zoom):
    
        FlxG.camera.zoom = FlxMath.bound(zoom, 0.5, 4)
        self._hud.updateZoom(FlxG.camera.zoom)
    

    def _createFloorTiles():
    
		floorImg = Assets.getBitmapData("assets/FloorTexture.png")
        imgWidth = floorImg.width
        imgHeight = floorImg.height
        i = LEVEL_MIN_X 
        j = LEVEL_MIN_Y 
        
        while (i <= LEVEL_MAX_X)  
        
            while (j <= LEVEL_MAX_Y)
            
                self.add(FlxSprite(i, j, floorImg))
                j += imgHeight
            
            i += imgWidth
            j = LEVEL_MIN_Y
        
    
    
    @haxe:override
    def update(elapsed):
        
        super(PlayState, self).update(elapsed)
        
        speed = 20
        if (FlxG.keys.anyPressed([A, LEFT]))
            orb.body.applyImpulse(Vec2(-speed, 0))
        if (FlxG.keys.anyPressed([S, DOWN]))
            orb.body.applyImpulse(Vec2(0, speed))
        if (FlxG.keys.anyPressed([D, RIGHT]))
            orb.body.applyImpulse(Vec2(speed, 0))
        if (FlxG.keys.anyPressed([W, UP]))
            orb.body.applyImpulse(Vec2(0, -speed))
            
        if (FlxG.keys.justPressed.Y) 
            self._setStyle(1)
        if (FlxG.keys.justPressed.H) 
            self._setStyle( -1)
            
        if (FlxG.keys.justPressed.U)
            self._setLerp(.1)
        if (FlxG.keys.justPressed.J)
            self._setLerp( -.1)
            
        if (FlxG.keys.justPressed.I)
            self._setLead(.5)
        if (FlxG.keys.justPressed.K)
            self._setLead( -.5)
            
        if (FlxG.keys.justPressed.O)
            self._setZoom(FlxG.camera.zoom + .1)
        if (FlxG.keys.justPressed.L)
            self._setZoom(FlxG.camera.zoom - .1)
            
        if (FlxG.keys.justPressed.M)
            FlxG.camera.shake()
    
    
    def _setLead(lead):
    
        cam = FlxG.camera
        cam.followLead.x += lead
        cam.followLead.y += lead
        
        if (cam.followLead.x < 0):
            cam.followLead.x = 0
            cam.followLead.y = 0
        
        self._hud.updateCamLead(cam.followLead.x)
    
    
    def _setLerp(lerp):
        cam = FlxG.camera
        cam.followLerp += lerp
        cam.followLerp = Math.round(10 * cam.followLerp) / 10 # adding or subtracting .1 causes roundoff errors
        self._hud.updateCamLerp(cam.followLerp)
    
    
    def _setStyle(i):
        # TODO: use Pythonic reflection instead?
        newCamStyleIndex = Type.enumIndex(FlxG.camera.style) + i
        if newCamStyleIndex < 0:
			newCamStyleIndex = newCamStyleIndex + 6
		else:
			newCamStyleIndex = newCamStyleIndex % 6
        
		# TODO: use Pythonic reflection instead?
        newCamStyle = Type.createEnumIndex(FlxCameraFollowStyle, newCamStyleIndex)
        FlxG.camera.follow(self._orb, newCamStyle, FlxG.camera.followLerp)
        self._drawDeadzone()
        
        self._hud.updateStyle(Std.string(FlxG.camera.style))
        
        if (FlxG.camera.style == SCREEN_BY_SCREEN)
            self._setZoom(1)

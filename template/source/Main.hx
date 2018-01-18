package C:.Users.me.Code.dragon.;
import flixel.FlxGame;
import openfl.display.Sprite;
import PlayState;
class Main extends Sprite {
function new() {
super();
this.addChild(new FlxGame(0, 0, PlayState));
}
}
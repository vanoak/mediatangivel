extends Node2D

# add to a Node2d node

var width = ProjectSettings.get_setting("display/window/size/width")
var height = ProjectSettings.get_setting("display/window/size/height")

var t = 0

func x1(t):
	return int(sin(t/10) * 100 + sin(t / 5) * 100 +width/2)
	
func y1(t):
	return int(cos(t / 10) * 100 + height/2)
	
func x2(t):
	return int(sin(t/10) * 200 + sin(t) * 2 +width/2)

func y2(t):
	return int(cos(t / 20) * 200 + cos(t/12) * 20 + height/2)

func _draw():
	for i in range(20):
		draw_line(Vector2(x1(t+i),y1(t+i)),Vector2(x2(t+i),y2(t+i)), Color(0.0,0.0,0.0), 1.0, true)
		t = t+0.3
		
func _process(delta):
	update()

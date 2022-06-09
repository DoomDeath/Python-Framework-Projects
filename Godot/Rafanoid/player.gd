extends KinematicBody2D



var mov = Vector2.ZERO
export var SPEED  = 4

func _physics_process(delta):
	mov = move_and_slide(mov)
	
	
	var fps = 1.0 / delta
	print("FPS: %d" % fps)
	if Input.is_action_pressed("mover_derecha"):
		position.x += SPEED
		
		
	
	if Input.is_action_pressed("mover_izquierda"):
		position.x -= SPEED           

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

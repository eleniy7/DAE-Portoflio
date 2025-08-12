extends CharacterBody2D

signal health_depleted

var health = 100.0

func _physics_process(delta):
	# Movement speed
	const SPEED = 600.0
	
	# Use built-in Godot input actions so no extra setup needed
	var direction = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = direction * SPEED
	move_and_slide()
	
	# Play animations
	if velocity.length() > 0.0:
		%HappyBoo.play_walk_animation()
	else:
		%HappyBoo.play_idle_animation()
	
	# Damage detection
	const DAMAGE_RATE = 6.0
	var overlapping_mobs = %HurtBox.get_overlapping_bodies()
	if overlapping_mobs:
		health -= DAMAGE_RATE * overlapping_mobs.size() * delta
		%HealthBar.value = health
		
		# If dead, signal the Game script
		if health <= 0.0:
			health_depleted.emit()

# Reset player state (called from respawn button)
func reset_player(start_pos: Vector2):
	health = 100.0
	%HealthBar.value = health
	position = start_pos

var last_checkpoint_position: Vector2

func set_checkpoint(pos: Vector2):
	last_checkpoint_position = pos

func respawn():
	position = last_checkpoint_position
	# You can also reset health or other states here
	show()
func _ready():
	last_checkpoint_position = position

func game_over():
	$Player.hide()
	await get_tree().create_timer(1.0).timeout
	$Player.respawn()

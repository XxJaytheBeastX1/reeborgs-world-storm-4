def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
while object_here():
    take()

while not at_goal():
    if wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    else:
        while object_here():
            take()
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

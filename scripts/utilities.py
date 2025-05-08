def go_to(goal_x, goal_y):
    # get starting position
    start_x = get_pos_x()
    start_y = get_pos_y()
    # calculate distance from start to goal
    x_distance = goal_x - start_x
    x_over_edge_distance = get_world_size() - abs(x_distance)
    y_distance = goal_y - start_y
    y_over_edge_distance = get_world_size() - abs(y_distance)
    # determite if to go over the edge and set directions to move for x
    if x_distance >= 0:
        if x_over_edge_distance < abs(x_distance):
            x_distance = x_over_edge_distance
            x_direction = West
        else:
            x_direction = East
    else:
        if x_over_edge_distance < abs(x_distance):
            x_distance = x_over_edge_distance
            x_direction = East
        else:
            x_direction = West
    # determite if to go over the edge and set directions to move for y
    if y_distance >= 0:
        if y_over_edge_distance < abs(y_distance):
            y_distance = y_over_edge_distance
            y_direction = South
        else:
            y_direction = North
    else:
        if y_over_edge_distance < abs(y_distance):
            y_distance = y_over_edge_distance
            y_direction = North
        else:
            y_direction = South
    # move distance in direction for x
    for _ in range(abs(x_distance)):
        move(x_direction)
    # move distance in direction for y
    for _ in range(abs(y_distance)):
        move(y_direction)

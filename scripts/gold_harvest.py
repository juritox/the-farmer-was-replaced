direction = North


def go_straight(direction):
    return move(direction)


def turn_right():
    global direction
    if direction == North:
        direction = East
    elif direction == East:
        direction = South
    elif direction == South:
        direction = West
    elif direction == West:
        direction = North


def turn_left():
    global direction
    if direction == North:
        direction = West
    elif direction == East:
        direction = North
    elif direction == South:
        direction = East
    elif direction == West:
        direction = South


def gold_harvest(amount):
    clear()
    cost = get_world_size() * num_unlocked(Unlocks.Mazes)
    print("Harvesting Treasure", amount, "times")

    while amount > 0 + get_world_size():
        if get_ground_type() != Grounds.Grassland:
            till()
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))

        while True:
            if get_entity_type() == Entities.Treasure:
                quick_print("Treasure found!")
                harvest()
                break
            turn_right()
            if go_straight(direction):
                continue
            turn_left()
            if go_straight(direction):
                continue
            turn_left()
            go_straight(direction)
        amount -= cost
        quick_print("Remaining amount:", amount)

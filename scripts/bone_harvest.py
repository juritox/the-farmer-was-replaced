def bone_harvest(amount):
    if get_world_size() % 2 != 0:
        set_world_size(get_world_size() - 1)
    clear()
    change_hat(Hats.Dinosaur_Hat)
    print("Harvesting Bone", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            move(East)
        if not move(North):
            if not move(West):
                quick_print("Unable to move anymore!")
                break
        for _ in range(get_world_size() - 2):
            for _ in range(get_world_size() - 2):
                move(West)
            move(North)
            for _ in range(get_world_size() - 2):
                move(East)
        for _ in range(get_world_size()):
            move(South)
            amount -= get_world_size()
        quick_print("Remaining amount:", amount)

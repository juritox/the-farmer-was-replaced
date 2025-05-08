def hay_harvest(amount):
    clear()
    print("Harvesting Hay", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
                amount -= 1
            move(North)
        move(East)
        quick_print("Remaining amount:", amount)

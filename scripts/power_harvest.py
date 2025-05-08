def measure_petals():
    petals = []
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            petals.append(measure())
            #  harvest sunflowers with 15 petals right away
            if measure() == 15:
                if can_harvest():
                    harvest()
                    petals.remove(15)
            move(North)
        move(East)
    max_petals = max(petals)
    quick_print("Max petals returned:", max_petals)
    quick_print("All petals returned:", petals)
    return max_petals, petals


def power_harvest(amount, water_threshold):
    clear()
    cost = get_cost(Entities.Sunflower)[Items.Carrot]
    print("Harvesting Sunflower", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                if plant(Entities.Sunflower):
                    amount -= cost
                if get_water() < water_threshold and num_items(Items.Water) > amount // 100:
                    use_item(Items.Water)
                move(North)
            move(East)
        quick_print("Remaining amount:", amount)
        max_petals, petals = measure_petals()
        while len(petals) > 0:
            for _ in range(get_world_size()):
                for _ in range(get_world_size()):
                    if measure() == max_petals:
                        if can_harvest():
                            harvest()
                            petals.remove(max_petals)
                            if max_petals not in petals:
                                break  # current max petals no longer available
                    if max_petals not in petals:
                        break
                    move(North)
                move(East)
            if len(petals) > 0:
                max_petals = max(petals)
                quick_print("Current max petals:", max_petals)

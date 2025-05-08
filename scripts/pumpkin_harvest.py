def detect_dead_pumpkin():
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            if get_entity_type() != Entities.Pumpkin:
                return True
            move(North)
        move(East)
    return False


def pumpkin_harvest(amount, water_threshold):
    clear()
    cost = get_cost(Entities.Pumpkin)[Items.Carrot]
    print("Harvesting Pumpkin", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                if get_ground_type() != Grounds.Soil:
                    till()
                if plant(Entities.Pumpkin):
                    amount -= cost
                if get_water() < water_threshold and num_items(Items.Water) > amount // 100:
                    use_item(Items.Water)
                move(North)
            move(East)
        quick_print("Remaining amount:", amount)
        if not detect_dead_pumpkin():
            if can_harvest():
                harvest()

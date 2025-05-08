def carrot_harvest(amount, water_threshold):
    clear()
    cost = get_cost(Entities.Carrot)[Items.Wood]
    print("Harvesting Carrot", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            if plant(Entities.Carrot):
                amount -= cost
            if get_water() < water_threshold and num_items(Items.Water) > amount // 100:
                use_item(Items.Water)
            move(North)
        move(East)
        quick_print("Remaining amount:", amount)

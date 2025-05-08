def wood_harvest(amount, water_threshold, fertilizer_enabled=False):
    clear()
    if fertilizer_enabled:
        print("Harvesting Wood with Weird_Substance", amount, "times")
    else:
        print("Harvesting Wood", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Grassland:
                till()
            if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
                if plant(Entities.Tree):
                    amount -= 1
            elif get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
                if plant(Entities.Tree):
                    amount -= 1
            else:
                if plant(Entities.Bush):
                    amount -= 1
            if get_entity_type() == Entities.Tree:
                if get_water() < water_threshold and num_items(Items.Water) > amount // 100:
                    use_item(Items.Water)
                if fertilizer_enabled and num_items(Items.Fertilizer) > amount // 100:
                    use_item(Items.Fertilizer)
            move(North)
        move(East)
        quick_print("Remaining amount:", amount)

def on_edge(x, y):
    return x == 0 or x == get_world_size() - 1 or y == 0 or y == get_world_size() - 1


def swap_inner_cacti():
    swap_count = 0
    current_size = measure()
    if measure(North) < current_size:
        swap(North)
        swap_count += 1
    if measure(East) < current_size:
        swap(East)
        swap_count += 1
    if measure(South) > current_size:
        swap(South)
        swap_count += 1
    if measure(West) > current_size:
        swap(West)
        swap_count += 1
    return swap_count


def swap_edge_cacti(x, y):
    swap_count = 0
    current_size = measure()
    # bottom-left corner
    if x == 0 and y == 0:
        if measure(North) < current_size:
            swap(North)
            swap_count += 1
        if measure(East) < current_size:
            swap(East)
            swap_count += 1
    # bottom-right corner
    elif x == get_world_size() - 1 and y == 0:
        if measure(North) < current_size:
            swap(North)
            swap_count += 1
        if measure(West) > current_size:
            swap(West)
            swap_count += 1
    # top-left corner
    elif x == 0 and y == get_world_size() - 1:
        if measure(East) < current_size:
            swap(East)
            swap_count += 1
        if measure(South) > current_size:
            swap(South)
            swap_count += 1
    # top-right corner
    elif x == get_world_size() - 1 and y == get_world_size() - 1:
        if measure(South) > current_size:
            swap(South)
            swap_count += 1
        if measure(West) > current_size:
            swap(West)
            swap_count += 1
    # left edge column
    elif x == 0:
        if measure(North) < current_size:
            swap(North)
            swap_count += 1
        if measure(East) < current_size:
            swap(East)
            swap_count += 1
        if measure(South) > current_size:
            swap(South)
            swap_count += 1
    # right edge column
    elif x == get_world_size() - 1:
        if measure(North) < current_size:
            swap(North)
            swap_count += 1
        if measure(South) > current_size:
            swap(South)
            swap_count += 1
        if measure(West) > current_size:
            swap(West)
            swap_count += 1
    # bottom edge row
    elif y == 0:
        if measure(North) < current_size:
            swap(North)
            swap_count += 1
        if measure(East) < current_size:
            swap(East)
            swap_count += 1
        if measure(West) > current_size:
            swap(West)
            swap_count += 1
    # top edge row
    elif y == get_world_size() - 1:
        if measure(East) < current_size:
            swap(East)
            swap_count += 1
        if measure(South) > current_size:
            swap(South)
            swap_count += 1
        if measure(West) > current_size:
            swap(West)
            swap_count += 1
    return swap_count


def sort_cacti():
    all_sorted = False
    while not all_sorted:
        swap_count = 0
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                if not on_edge(get_pos_x(), get_pos_y()):
                    swap_count += swap_inner_cacti()
                else:
                    swap_count += swap_edge_cacti(get_pos_x(), get_pos_y())
                move(North)
            move(East)
        quick_print(swap_count, "swaps")
        if swap_count == 0:
            all_sorted = True
            quick_print("All cacti sorted!")


def cactus_harvest(amount, water_threshold):
    clear()
    cost = get_cost(Entities.Cactus)[Items.Pumpkin]
    print("Harvesting Cactus", amount, "times")

    while amount > 0 + get_world_size():
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                if plant(Entities.Cactus):
                    amount -= cost
                if get_water() < water_threshold and num_items(Items.Water) > amount // 100:
                    use_item(Items.Water)
                move(North)
            move(East)

        sort_cacti()
        if can_harvest():
            harvest()
        quick_print("Remaining amount:", amount)

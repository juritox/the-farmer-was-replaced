from gold_harvest import *
from bone_harvest import *
from power_harvest import *
from hay_harvest import *
from wood_harvest import *
from carrot_harvest import *
from pumpkin_harvest import *
from cactus_harvest import *
from auto_unlock import *

# priority options: None, "Gold", "Power", "Bone", "Hay", "Wood", "Carrot", "Pumpkin", "Cactus", "Weird_Substance"
priority = None
amount = 100000
WATER_THRESHOLD = 0.75


def main():
    global amount
    global priority

    while True:
        if priority:
            # Only harvest the prioritized resource
            if priority == "Gold":
                gold_harvest(amount)
            elif priority == "Power":
                power_harvest(amount, WATER_THRESHOLD)
            elif priority == "Bone":
                bone_harvest(amount)
            elif priority == "Hay":
                hay_harvest(amount)
            elif priority == "Wood":
                wood_harvest(amount, WATER_THRESHOLD)
            elif priority == "Carrot":
                carrot_harvest(amount, WATER_THRESHOLD)
            elif priority == "Pumpkin":
                pumpkin_harvest(amount, WATER_THRESHOLD)
            elif priority == "Cactus":
                cactus_harvest(amount, WATER_THRESHOLD)
            elif priority == "Weird_Substance":
                wood_harvest(amount, WATER_THRESHOLD, True)
            else:
                print("Unknown PRIORITY:", priority)
                priority = None
            continue  # Skip the rest of the loop

        # Power
        elif num_items(Items.Power) < amount and num_items(Items.Carrot) > amount:
            power_harvest(amount // 10, WATER_THRESHOLD)
        # Gold
        elif num_items(Items.Gold) < amount and num_items(Items.Weird_Substance) > amount:
            gold_harvest(amount // 10)
        # Weird_Substance
        elif num_items(Items.Weird_Substance) < amount and num_items(Items.Fertilizer) > amount // 10:
            wood_harvest(amount // 10, WATER_THRESHOLD, True)
        # Bone
        elif num_items(Items.Bone) < amount:
            bone_harvest(amount // 10)
        # Cactus
        elif num_items(Items.Cactus) < amount and num_items(Items.Pumpkin) > amount:
            cactus_harvest(amount // 10, WATER_THRESHOLD)
        # Pumpkin
        elif num_items(Items.Pumpkin) < amount and num_items(Items.Carrot) > amount:
            pumpkin_harvest(amount, WATER_THRESHOLD)
        # Carrot
        elif num_items(Items.Carrot) < amount and num_items(Items.Hay) > amount and num_items(Items.Wood) > amount:
            carrot_harvest(amount, WATER_THRESHOLD)
        # Wood
        elif num_items(Items.Wood) < amount:
            wood_harvest(amount // 10, WATER_THRESHOLD)
        # Hay
        elif num_items(Items.Hay) < amount:
            hay_harvest(amount // 10)
        else:
            print(amount, "of everything collected!")
            auto_unlock()
            if amount < 10000:
                amount *= 10
            else:
                amount *= 2
            quick_print("Now harvesting", amount, "of everything...")


if __name__ == "__main__":
    main()

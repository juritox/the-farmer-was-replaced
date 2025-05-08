def auto_unlock():
    quick_print("Upgrading unlocks...")
    for upgrade in Unlocks:
        if get_cost(upgrade) != {}:
            cost = get_cost(upgrade)
            if unlock(upgrade):
                quick_print("--------------------")
                print("Unlocked", upgrade)
                quick_print("Cost:", cost)
                quick_print("--------------------")
                do_a_flip()
            else:
                quick_print(upgrade, "unable to upgrade")
                quick_print("Cost:", cost)

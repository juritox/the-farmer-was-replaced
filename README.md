# The Farmer Was Replaced Scripts

Here are my scripts for *The Farmer Was Replaced*, a great automation game [available on Steam](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/). The game uses a language similar to Python to program a farming drone. The goal is to harvest crops and spend them to unlock new functions. The endgame involves competing on the leaderboard while optimizing and refining your code so that the drone can harvest as many crops as possible, as quickly as possible.

## My Goals in the Game

I will be sharing my own scripts here, which I will gradually improve. I’ll also describe what each script currently implements and discuss possible optimizations to improve them further. My goal is to write the most optimal code I can and achieve a high rank on the leaderboard by doing so. I also include compressed GIFs that showcase what my scripts are doing currently in the game.

## Differences Between the Game Scripting Language and Python

The game's scripting language is essentially a simplified form of Python. It uses its own built-in functions like `plant()`, `harvest()`, `move()`, `measure()`, `quick_print()`, and others. A good overview of the game's syntax is available on [this Wiki page](https://thefarmerwasreplaced.wiki.gg/wiki/Tooltips_Code).

That being said, some Python features are not available in the game. For example, you cannot use type annotations or docstrings, so my scripts will be documented only with simple comments and notes here. Additionally, importing modules from Python’s standard library is not possible, so advanced features like sorting must be implemented from scratch which adds an extra layer of challenge.

## Game Version Used

My scripts work on the early access version of the game where the [Simulation Update](https://store.steampowered.com/news/app/2060160/view/783160409258459178) was the latest major update. You can check the versions of the game on [SteamDB Patches page](https://steamdb.info/app/2060160/patchnotes/).

> **Note:** There is no guarantee that my scripts will continue to work after future game updates. Always read patch notes to see if any code changes may break compatibility, and update scripts as needed.

```
Latest tested game BuildID: 17763496
Last tested: 2025-05-09
```

## Scripts Overview

### `main`
![main](media/images/main.png)

This is my main script that handles the management of other scripts and runs them to balance resource harvesting.

#### Currently Implemented

- Adjustable `priority` variable that sets the script to harvest only the selected resource and ignore the others. Set to `None` to disable priority harvesting and use the if-else decision tree instead.
- Adjustable `amount` variable to specify how much of each resource should be harvested.
- Adjustable `WATER_THRESHOLD` constant to set the minimum *Water* level required to trigger watering after planting. Values should range from `0` to `1`.
- Management of other harvesting scripts using an if-else decision tree.
- Automatic execution of the `auto_unlock` script each time all resources have been cycled through.
- Automatic increment of the `amount` after each full harvesting cycle.

#### Possible Optimizations

- Improve resource management by adjusting individual resource ratios instead of just a general amount for all.
- Fixing the if-else decision tree to ensure that the resource gathering cycle doesn’t repeat until all resources have been gathered at least to the specified `amount`.
- Adding better control over the use of *Fertilizer*.
- Adding timing and performance monitoring for each script.

### `hay_harvest`
![hay_harvest](media/gifs/hay_harvest.gif)

A simple script to repeatedly harvest *Hay*.

#### Currently Implemented

- Accepts an `amount` argument to control when to stop the script, decrementing it after each harvest.
- Uses the `clear()` function at the start to ensure all tiles are converted to *Grassland*, where *Hay* grows automatically.
- Iterates through the entire field and harvests *Hay* on each tile where possible.

#### Possible Optimizations

- Since *Hay* grows very quickly, it may be more efficient to traverse only the edges of the field, reducing the time spent returning to the next column for harvesting.
- Checks using `can_harvest()` could be omitted to save additional ticks if it is guaranteed that *Hay* will always be fully grown before each harvest.

### `wood_harvest`
![wood_harvest](media/gifs/wood_harvest.gif)

Wood can be harvested in the game from a *Tree* or a *Bush*. Each *Tree* yields 5 *Wood* when harvested, while a *Bush* yields only 1 *Wood*. The catch is that trees can't be planted adjacent to each other-if they are, their growth time doubles for each *Tree* directly to the north, east, west, or south. The optimal strategy is to plant trees in a checkerboard pattern and fill the remaining tiles with other plants. To maximize *Wood* harvesting, this script fills the rest of the field with bushes.

#### Currently Implemented

- Accepts an `amount` argument to control when to stop the script, decrementing it after each harvest.
- Accepts a `water_threshold` argument to control the minimum *Water* level required to trigger watering after planting.
- Accepts a `fertilizer_enabled` argument to control whether trees are fertilized (default is `False`).
- Can also be used to harvest *Weird_Substance* when *Fertilizer* is applied to trees.
- Tiles the ground to *Grassland* if it is not already *Grassland*.
- Plants trees in a checkerboard pattern to avoid growth penalties.
- Plants bushes in the spaces between trees to maximize *Wood* harvesting.
- Iterates through the entire field and harvests *Tree* or *Bush* on each tile where possible.

#### Possible Optimizations

- Tiling the ground may not be necessary, as both trees and bushes can grow on either *Grassland* or *Soil*.
- Harvesting *Weird_Substance* could be improved by leveraging its spreading mechanic and avoiding unnecessary use of *Fertilizer*.
- Movement efficiency could be improved to reduce the time spent returning to the next column for harvesting.

### `carrot_harvest`
![carrot_harvest](media/gifs/carrot_harvest.gif)

Planting *Carrot* costs *Wood* and *Hay*. They need to be planted on the *Soil* type of ground. This script automates planting, watering, and harvesting carrots.

#### Currently Implemented

- Accepts an `amount` argument to control when to stop the script, decrementing by the *Wood* cost of a *Carrot* after each planting.
- Accepts a `water_threshold` argument to control the minimum *Water* level required to trigger watering after planting.
- Tills the ground to *Soil* before planting if it’s not already *Soil*.
- Iterates through the entire field and harvests *Carrots* on each tile where possible.

#### Possible Optimizations

- Since *Carrot* grow very quickly, it may be more efficient to traverse only the edges of the field to reduce the time spent returning to the next column for harvesting.
- Checks using `can_harvest()` could be omitted to save additional ticks if it is guaranteed that *Carrot* will always be fully grown before each harvest.
- Tilling the ground could be omitted if the field is already prepared as *Soil*. This could be achieved by sharing a state variable like `is_all_soil` between scripts.

### `pumpkin_harvest`
![pumpkin_harvest](media/gifs/pumpkin_harvest.gif)

Planting *Pumpkin* costs *Carrot*. *Pumpkin* must be planted on *Soil*. Another mechanic for *Pumpkin* is that if all pumpkins in a square of the field are fully grown, they will form a giant *Pumpkin* that yields *n* times more *Pumpkin*, where *n* is the size of the square they formed. The optimal strategy is to fill the whole field with just one giant *Pumpkin* before harvesting for maximum yield. However, there is a 20% chance that each *Pumpkin* will die once fully grown, creating a hole in the field that must be found and replanted.

#### Currently Implemented

- Accepts an `amount` argument to control when to stop the script, decrementing by the *Carrot* cost of a *Pumpkin* after each planting.
- Accepts a `water_threshold` argument to control the minimum *Water* level required to trigger watering after planting.
- Tills the ground to *Soil* before planting if it’s not already *Soil*.
- Includes a helper function `detect_dead_pumpkin()` that traverses the whole field and returns `True` if it finds a hole in the pumpkins, and `False` otherwise.
- Harvests the field only after confirming there are no holes, ensuring that one giant *Pumpkin* fills the entire field for maximum yield.

#### Possible Optimizations

- Tilling the ground could be omitted if the field is already prepared as *Soil*. This could be managed by sharing a state variable like `is_all_soil` between scripts.
- Use of *Fertilizer* could speed up the growth of the last pumpkins before the final giant *Pumpkin* forms.
- The `detect_dead_pumpkin()` function currently checks the whole field every time; it could be optimized to store and recheck only previously found holes.

### `cactus_harvest`
![cactus_harvest](media/gifs/cactus_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `bone_harvest`
![bone_harvest](media/gifs/bone_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `weird_substance_harvest`

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `gold_harvest`
![gold_harvest](media/gifs/gold_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `power_harvest`
![power_harvest](media/gifs/power_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `polyculture_harvest`

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `utilities`

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `auto_unlock`

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `run_simulation`

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.
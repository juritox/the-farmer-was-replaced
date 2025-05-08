# The Farmer Was Replaced Scripts

Here are my scripts for *The Farmer Was Replaced*, a great automation game [available on Steam](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/). The game uses a language similar to Python to program a farming drone. The goal is to harvest crops and spend them to unlock new functions. The endgame involves competing on the leaderboard while optimizing and refining your code so that the drone can harvest as many crops as possible, as quickly as possible.

## My Goals in the Game

I will be sharing my own scripts here, which I will gradually improve. I’ll also describe what each script currently implements and discuss possible optimizations to improve them further. My goal is to write the most optimal code I can and achieve a high rank on the leaderboard by doing so.

## Differences Between the Game Scripting Language and Python

The game's scripting language is essentially a simplified form of Python. It uses its own built-in functions like `plant()`, `harvest()`, `move()`, `measure()`, `quick_print()`, and others. A good overview of the game's syntax is available on [this Wiki page](https://thefarmerwasreplaced.wiki.gg/wiki/Tooltips_Code).

That being said, some Python features are not available in the game. For example, you cannot use type annotations or docstrings, so my scripts will be documented only with simple comments and notes here. Additionally, importing modules from Python’s standard library is not possible, so advanced features like sorting must be implemented from scratch which adds an extra layer of challenge.

## Game Version Used

My scripts work on the early access version of the game where the [Simulation Update](https://store.steampowered.com/news/app/2060160/view/783160409258459178) was the latest major update. You can check the versions of the game on [SteamDB Patches page](https://steamdb.info/app/2060160/patchnotes/).

> **Note:** There is no guarantee that my scripts will continue to work after future game updates. Always read patch notes to see if any code changes may break compatibility, and update scripts as needed.

```bash
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
- Adjustable `WATER_THRESHOLD` constant to set the minimum water level required to trigger watering after planting. Values should range from `0` to `1`.
- Management of other harvesting scripts using an if-else decision tree.
- Automatic execution of the `auto_unlock` script each time all resources have been cycled through.
- Automatic increment of the `amount` after each full harvesting cycle.

#### Possible Optimizations

- Improve resource management by adjusting individual resource ratios instead of just a general amount for all.
- Fixing the if-else decision tree to ensure that the resource gathering cycle doesn’t repeat until all resources have been gathered at least to the specified `amount`.
- Adding timing and performance monitoring for each script.

### `hay_harvest`
![hay_harvest](media/gifs/hay_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `wood_harvest`
![wood_harvest](media/gifs/wood_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `carrot_harvest`
![carrot_harvest](media/gifs/carrot_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

### `pumpkin_harvest`
![pumpkin_harvest](media/gifs/pumpkin_harvest.gif)

To be documented.

#### Currently Implemented

To be documented.

#### Possible Optimizations

To be documented.

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
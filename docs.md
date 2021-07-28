# hypixel_py
Python wrapper for the Hypixel API. Includes QOL features such as WLR and KDR precalculated, still very much a WIP in very early stages of development.

# Additional values: (`HypixelConnection.get_player_stats()`)
## `['player']['IGN']`

Consolidates `['player']['displayname']` and `['player']['playername']`.

Returns the player's IGN.
## `['player']['rank']`
Consolidates `['player']['newPackageRank']` and `['player']['monthlyPackageRank']`.

Returns:
```py
'DEFAULT'
'VIP'
'VIP_PLUS'
'MVP'
'MVP_PLUS'
# Returns MVP_PLUS_PLUS instead of SUPERSTAR.
'MVP_PLUS_PLUS'
```

## `['player']['networkLVL']`

Formula:
```py
(sqrt((2 * data['player']['networkExp']) + 30625) / 50) - 2.5
```
Returns the player's network level, rounded to the nearest integer.
## `['player']['stats']['Duels']['melee_misses']`
Returns the player's melee misses in Duels.
## `['player']['stats']['Duels']['melee_hit_miss_ratio']`
Returns the player's melee hit/miss ratio in Duels.
## `['player']['stats']['Duels']['win_loss_ratio']`
Returns the player's **overall** Duels win/loss ratio.
## `['player']['stats']['Duels']['kill_death_ratio']`
Returns the player's **overall** Duels kill/death ratio. It is normal for this value to differ from win/loss ratio.
![roliLib banner](https://github.com/ThunderFound/rolilib/assets/90287659/b7c011fb-69b6-4c9e-8514-9f919d5f84af)
## Installation

```bash
pip install rolilib
```
    
## Examples

### Item's name and RAP
```python
import rolilib

item = rolilib.getItem('138932314')   # Item's id

print('Name:', item.name)
print('RAP:', item.rap)
```

Output:
```bash
Name: Dominus Aureus
RAP: 4316150
```

### Player's name, id and RAP
```python
import rolilib

player = rolilib.getPlayer('Rolimon')   # Letter case does not matter

print('Name:', player.name)
print('Id:', player.id)
print('RAP:', player.rap)

print('--------------------')

player = rolilib.getPlayer('489694314')   # Also, you can pass id

print('Name:', player.name)
print('Id:', player.id)
print('RAP:', player.rap)
```

Output:
```bash
Name: Rolimon
Id: 152588760
RAP: 478207
--------------------
Name: And23102
Id: 489694314
RAP: 2155
```

### Every limited's name
```python
import rolilib

limiteds = rolilib.getLimiteds()   # Gets data of every limited item. From oldest to newest
print(limiteds.name)   # Prints only names of limiteds
```

Output: (I won't show the full output because it contains more than 50,000 characters)
```bash
['Red Baseball Cap', 'Classic ROBLOX Viking Helm', 'The Classic ROBLOX Fedora', 'Domino Crown' ... 'Vault Commando', 'Vault Swordpack', 'Vault Glider Wings', 'Daemonshank']
```
## Documentation

### rolilib.getItem()

#### getItem().id

Returns item's id

#### getItem().name

Returns item's name

#### getItem().acronym

Returns item's acronym

#### getItem().rap

Returns item's rap

#### getItem().value

Returns item's value

#### getItem().default_value

Returns item's original/default value

#### getItem().demand

Returns item's demand

| Unassigned | Terrible   | Low        | Normal     | High       | Amazing    |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| -1         | 0          | 1          | 2          | 3          | 4          |

#### getItem().trend

Returns item's trend

| Unassigned | Unstable   | Lowering   | Stable     | Raising    | Fluctuating |
| ---------- | ---------- | ---------- | ---------- | ---------- | ----------  |
| -1         | 0          | 1          | 2          | 3          | 4           |

#### getItem().projected

Returns whether the item is projected

| False | True  |
| ----- | ----- |
| -1    | 1     |

#### getItem().hyped

Returns whether the item is hyped

| False | True  |
| ----- | ----- |
| -1    | 1     |

#### getItem().rare

Returns whether the item is rare

| False | True  |
| ----- | ----- |
| -1    | 1     |

### rolilib.getPlayer()

#### getPlayer().id

Returns players's id

#### getPlayer().name

Returns players's username

#### getPlayer().value

Returns players's value

#### getPlayer().rap

Returns players's rap

#### getPlayer().rank

Returns players's rank in leaderboard

| Outside top 1000 | Inside top 1000      |
| ---------------- | -------------------- |
| None             | Value from 1 to 1000 |

#### getPlayer().premium

Returns whether the player has premium

#### getPlayer().privacy_enabled

Returns whether the player has inventory private

#### getPlayer().terminated

Returns whether the player is terminated

#### getPlayer().stats_updated

Returns when player's stats were updated the last time. Returns unix timestamp

#### getPlayer().stats_updated_utc

Returns when player's stats were updated the last time. Returns date in UTC

#### getPlayer().last_scan

Returns when player's stats were scanned the last time. Returns unix timestamp

#### getPlayer().last_scan_utc

Returns when player's stats were scanned the last time. Returns date in UTC

#### getPlayer().last_online

Returns when the player was online last time. Returns unix timestamp

#### getPlayer().last_online_utc

Returns when the player was online last time. Returns date in UTC

#### getPlayer().last_location

Returns where was the player when he was checked the last time



## You can also try out these packages

[rolimons.py](https://github.com/wa1ker38552/rolimons.py)

[rolipy](https://github.com/acierp/rolipy)

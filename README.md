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

## You can also try out these packages

[rolimons.py](https://github.com/wa1ker38552/rolimons.py)

[rolipy](https://github.com/acierp/rolipy)

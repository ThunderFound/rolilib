# rolilib

**rolilib** is an open source API Wrapper for [Rolimons](https://www.rolimons.com/)


## Installation

```bash
pip install rolilib
```
    
## Examples

### Items name and RAP
```python
import rolilib

item = rolilib.getItem('138932314')

print('Name:', item.name)
print('RAP:', item.rap)
```
Output:
```bash
Name: Dominus Aureus
RAP: 4316150
```

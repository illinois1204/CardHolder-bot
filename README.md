python -B -m bot.main  

another way: make `root.py` in root of project with
```
# flake8: noqa
from bot import main
```
and use:
```
pymon root.py
```
# Install packages
#### Dependencies:
```sh
pip install -r requirements.txt
```
#### Dev-Dependencies:
```sh
pip install -r requirements-dev.txt
```


# Launch bot
#### Default launch using module start
```sh
python -m bot.main
```
```sh
python -B -m bot.main
```
> flag `-B` is disable `__pychache__`

#### Hot reloading launch
1. Make file `root.py` in project's root directory
2. Put with:
    ```py
    # flake8: noqa
    from bot import main
    ```
3. Run with:
    ```sh
    pymon root.py
    ```

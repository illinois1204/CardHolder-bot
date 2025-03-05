# Prerequirement
#### Dependencies:
```sh
pip install -r requirements.txt
```
#### Dev-Dependencies:
```sh
pip install -r requirements-dev.txt
```
#### Make storage directory:
```sh
mkdir -p storage/{any,defined}
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

#### Docker run
When start container with `docker run` set option:

Token (required)
```sh
-e BOT_TOKEN="..."
```
Volume for persistent (optional)
```sh
-v host_path:/app/storage
```

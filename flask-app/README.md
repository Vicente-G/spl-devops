# flask-app

A simple Flask app with gunicorn and logging. First up, clone this repo to test it out!

```sh
git clone https://github.com/Vicente-G/spl-devops && cd spl-devops/flask-app
```

## Installing with `venv`

Execute the following commands (in that order) on the terminal located on this project's folder:
```sh
python -m venv .venv
source ./.venv/bin/activate
python -m pip install -r requirements.txt
```

## Running with `venv`

Use plain python for development server:
```sh
python ./src/__init__.py --debug
```

Or `gunicorn` to setup the service: (can add workers with -w #)
```sh
python -m gunicorn -b 0.0.0.0:8080 'src:create_app()'
```

## Installing with `pdm`

It is highly encouraged to develop over pdm, because of linting and format tools available in the `pyproject.toml` file. To begin with, one must install `pdm` with the following options:
```sh
python -m pip install --user pdm # Then may use with "python -m pdm"
brew install pdm # If homebrew available
```

Then, you can simply run:
```sh
pdm sync
```

And everything is now set and done. With pdm you can access the scripts defined at the `pyproject.toml` file.

## Running with pdm

Now you can simply start servers for development or with gunicorn respectively:
```sh
pdm run dev
pdm run start # Can also add workers with - -w #
```

But you can also use dev tools for checking and fixing the code quality:
```sh
pdm run check
pdm run fix
```

And run tests:
```sh
pdm run test
```


## Exporting `pdm` changes to `pip`

In case you were wondering.
```sh
pdm list --freeze > requirements.txt
```
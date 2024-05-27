# A Python Polylith repo

> Step by step demo on how to use polylith concept with poetry to build  quote generating cli & web apps.

## Setup for dev

For re-usable `poetry` let's use `pipx` ([install instructions](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx))

    pipx install poetry==1.8

Sometimes it makes sense to set an alias like `alias poetry18="pipx run poetry==1.8"` to your shell does not get confused.

Init the repo

    poetry init

--> package name: "experiment"


Add polylith plugins

    poetry self add poetry-multiproject-plugin
    poetry self add poetry-polylith-plugin


Creating the polylith workspace

    poetry poly create workspace --name experiment --theme loose

Installing the workspace env

    poetry install

Adding some dependencies

    poetry add -G dev pytest
    poetry install

## Building apps

### A typer cli app

    poetry poly create component --name quotes

Add `def generate_*_quote` to the new `core.py` and adjust `__init__.py` to include the functions.

Update pyproject.toml

    poetry poly sync

Add tests to `tests/components/experiment/quotes/test_core.py`.

Add cli component

    poetry poly create base --name typer_cli
    poetry add typer
    poetry poly sync
    poetry install

Add project to expose component

    poetry poly create project --name quotes_cli

Edit `projects/quotes_cli/pyproject.toml` by manually adding the `typer_cli` base and script entry under `[tool.poetry.scripts]`.

We should also have added the `quotes` component but were lazy. Let's do that via

    cd projects/quotes_cli
    poetry poly sync

Nice, isn't it?

Now let's build the project (if already in the quotes_cli dir)

    poetry build-project

Let's install it

    poetry install

Now we can run our cli using

    quotes_cli Tom Lehrer

### A fastapi app

It's pretty much identically to the above

    poetry poly create base --name fastapi_app
    poetry add fastapi

Add app code to `bases/fastapi_app/core.py` and a test to `test/bases/experiment/fastapi_app/test_core.py`.

The project

    poetry poly create project --name quotes_app

Manually add bases dependency to `projects/quotes_app/pyproject.toml` and

    poetry poly sync

Then

    cd projects/quotes_app
    poetry add uvicorn fastapi
    poetry build-project

to automatically generate a *.whl file. Next create a Dockerfile to use that wheel and place it in the projects dir. From the quotes_app dir

    docker build -t myimage .
    docker run -d --name mycontainer -p 8000:8000 myimage

To sanity check the docker image is running

    docker ps -a

If it's not running

    docker logs -t myimage

to read the logs.

If it is running check localhost:8000/quote in your browser :)

## The development dir

    poetry add -G dev jupyter

The point of the `development` dir is to do development and move code later to appropriate bases / components.

See for example the notebook `development/something.ipynb`, calling code from the `quotes` base and local code from `development/something.py`.

## Summary & Docs
The official Polylith documentation:
[high-level documentation](https://polylith.gitbook.io/polylith)

A Python implementation of the Polylith tool:
[python-polylith](https://github.com/DavidVujic/python-polylith)

Above broken down:

* `components` = core functionality, computing things
* `bases` = exposing components, e.g. as rest api, cli, to be used in projects for deployments
* `development` = for interactive development, e.g. dump your dev scripts and notebooks here
* `project` = infra stuff for deployment, pyproject.toml pointing to relevant components and a base, Dockerfile, ...

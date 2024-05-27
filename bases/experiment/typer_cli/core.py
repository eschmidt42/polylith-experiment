# -*- coding: utf-8 -*-
"""

Example:

    python components/experiment/typer_cli/core.py Tom Lehrer

"""

import typer
from experiment.quotes.core import (
    generate_douglas_adams_quote,
    generate_tom_lehrer_quote,
)

app = typer.Typer()


@app.command()
def get_quote(forename: str, surname: str):
    if forename.lower() == "tom" and surname.lower() == "lehrer":
        quote = generate_tom_lehrer_quote()
        typer.echo(quote)
    elif forename.lower() == "douglas" and surname.lower() == "adams":
        quote = generate_douglas_adams_quote()
        typer.echo(quote)
    else:
        typer.echo("No matching quotes found.")


def main():
    app()


if __name__ == "__main__":
    main()

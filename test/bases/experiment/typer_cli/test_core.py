# -*- coding: utf-8 -*-
from experiment.typer_cli import core
from unittest.mock import patch


def test_sample():
    assert core is not None


@patch("experiment.typer_cli.core.generate_tom_lehrer_quote")
@patch("typer.echo")
def test_get_quote_tom_lehrer(mock_echo, mock_quote):
    mock_quote.return_value = "This is a Tom Lehrer quote."
    core.get_quote("Tom", "Lehrer")
    mock_echo.assert_called_once_with("This is a Tom Lehrer quote.")


@patch("experiment.typer_cli.core.generate_douglas_adams_quote")
@patch("typer.echo")
def test_get_quote_douglas_adams(mock_echo, mock_quote):
    mock_quote.return_value = "This is a Douglas Adams quote."
    core.get_quote("Douglas", "Adams")
    mock_echo.assert_called_once_with("This is a Douglas Adams quote.")


@patch("typer.echo")
def test_get_quote_no_match(mock_echo):
    core.get_quote("John", "Doe")
    mock_echo.assert_called_once_with("No matching quotes found.")

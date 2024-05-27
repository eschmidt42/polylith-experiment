# -*- coding: utf-8 -*-
from experiment.quotes import generate_douglas_adams_quote, generate_tom_lehrer_quote


def test_douglas_adams():
    quote = generate_douglas_adams_quote()
    assert quote
    assert isinstance(quote, str)


def test_tom_lehrer():
    quote = generate_tom_lehrer_quote()
    assert quote
    assert isinstance(quote, str)

# -*- coding: utf-8 -*-
from fastapi import FastAPI
from experiment.quotes.core import (
    generate_douglas_adams_quote,
    generate_tom_lehrer_quote,
)
import random

app = FastAPI()


@app.get("/quote")
def get_quote():
    random_quote = random.choice(
        [generate_tom_lehrer_quote(), generate_douglas_adams_quote()]
    )
    return {"quote": random_quote}

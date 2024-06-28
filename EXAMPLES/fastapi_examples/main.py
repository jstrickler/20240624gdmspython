import json
from fastapi import FastAPI
from .potus import fetch_president, fetch_all_presidents

app = FastAPI()




# home page
@app.get("/")
def home():
    return {"Resources": "/presidents"}

@app.put("/presidents")
def put_president():
    pass

# retrieve one record
@app.get("/presidents/{term_id}")
def get_president(term_id: int):
    row = fetch_president(term_id)
    return row

# retrieve all records
@app.get("/presidents")
def get_all_president():
    rows = fetch_all_presidents()
    return rows
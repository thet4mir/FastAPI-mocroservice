from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return {"Hello": "World"}

@app.post("/")
def home_details_view():
    return {"Hello": "World"}
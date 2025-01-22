from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the public subscription system!"}

@app.get("/subscriptions")
def get_subscriptions():
    with open("public/subscriptions/subscriptions.txt", "r") as f:
        return f.readlines()
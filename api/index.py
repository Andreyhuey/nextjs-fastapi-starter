from fastapi import FastAPI, status

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/hi", status_code=status.HTTP_200_OK)
def hi():
    return {"message": "testing"}
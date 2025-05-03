from fastapi import FastAPI


# This is a simple FastAPI application that serves as a math calculator API.
# It includes a root endpoint that returns a welcome message.

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Math calculator is online"}

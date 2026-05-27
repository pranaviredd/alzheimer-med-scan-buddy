from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Alzheimer Med Scan Buddy Running"
    }

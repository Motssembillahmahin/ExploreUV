# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///

from fastapi import FastAPI
import uvicorn


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "This is the root to check the endpoint of the UV server"}

def main():
    print("Hello from exploreuv!")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    

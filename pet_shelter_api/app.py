import uvicorn
from fastapi import FastAPI


app = FastAPI()


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(app)

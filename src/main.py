from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_index():
    return {"Hello": "World"}


@app.get("/api/v1/hello-world/")
def get_hello_world():
    return {"what": "H", "where": "H", "version": 1.0}


@app.get("/api/v1/xin-chao/")
def get_xin_chao():
    return {"name": "Xin chao anh em!"}

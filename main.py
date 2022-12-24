from fastapi import FastAPI
app = FastAPI()
@app.get("/apicount")
def root():
    print("Inside API root()")
    return 178
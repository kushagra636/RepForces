from fastapi import FastAPI
# from app.routes import auth

app = FastAPI(title="RepForces API")

# app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "RepForces Backend Running"}
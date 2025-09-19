from fastapi import FastAPI
app = FastAPI()
from .routes import router_auth


app.include_router(router_auth)

@app.get("/")
async def root():
  return {"message": "Hello World"}
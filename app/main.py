from fastapi import FastAPI
app = FastAPI()


from .routes import all_routers

for router in all_routers:
    app.include_router(router)

@app.get("/")
async def root():
  return {"message": "Hello world, to consult the documentation add /docs to the url"}
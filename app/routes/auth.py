from fastapi import APIRouter

router_auth = APIRouter( 
  prefix="/auth",
  tags=["auth"]
)

@router_auth.get("/login")
async def login():
  return {"message": "Login"}

@router_auth.get("/logout")
async def logout():
  return {"message": "Logout"}
from fastapi import APIRouter

router_auth = APIRouter( 
  prefix="/auth",
  tags=["auth"]
)

@router_auth.get("/")
async def root():
  
  return {"message": "Hello World"}

@router_auth.post("/login")
async def login():
  return {"message": "Login"}

@router_auth.post("/register")
async def register():
  return {"message": "register"}

@router_auth.post("/refresh")
async def refresh():
  return {"message": "refresh"}
from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.core.auth import hash_password, verify_password, create_access_token, verify_token
from app.core.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.db.deps import get_db

router = APIRouter()

fake_db = {}  

@router.post("/register")
def register(username: str, email: str, password: str):
    if username in fake_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = hash_password(password)
    fake_db[username] = {
        "email": email,
        "hashed_password": hashed
    }
    return {"msg": "User created"}

@router.post("/login")
def login(username: str, password: str):
    user = fake_db.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def me(user = Depends(get_current_user)):
    return user

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.execute("SELECT * FROM users")
    return users.fetchall()
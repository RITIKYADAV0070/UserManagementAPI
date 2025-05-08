from fastapi import FastAPI, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth, database
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]  # For development

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for checking if the server is working
@app.get("/")
def read_root():
    return {"message": "API is running!"}

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = auth.create_access_token({"sub": str(db_user.id)})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/profile/{id}", response_model=schemas.UserOut)
def get_profile(id: int, authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]
    user_id = auth.decode_token(token)
    if not user_id or int(user_id) != id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    db_user = crud.get_user(db, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/profile/{id}", response_model=schemas.UserOut)
def update_profile(id: int, updates: schemas.UserUpdate, authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]
    user_id = auth.decode_token(token)
    if not user_id or int(user_id) != id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    db_user = crud.get_user(db, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, db_user, updates)

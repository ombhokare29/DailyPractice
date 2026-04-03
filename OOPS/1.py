from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# simple in-memory storage
users = []

a
class User(BaseModel):
    name: str
    age: int

 
@app.post("/users")
def create_user(user: User):
    if user.age < 18:
        return {"error": "User must be 18+"} 

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age
    }

    users.append(new_user)
    return {"data": new_user}


@app.get("/users")
def get_users():
    return {"data": users}
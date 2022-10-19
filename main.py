from fastapi import FastAPI, HTTPException
from models import *

app = FastAPI()

db: List[User] = [
    User(id= uuid4(), 
    name='John Doe', 
    email='doe@em.com', 
    gender=Gender.male, 
    roles=[Role.admin, Role.supervisor]),
    User(id= uuid4(), 
    name='Jane Doe', 
    email='doe@em.com', 
    gender=Gender.female, 
    roles=[Role.supervisor]),
    User(id= uuid4(), 
    name='Malika Doe', 
    email='mdoe@em.com', 
    gender=Gender.female, 
    roles=[Role.amateur]),

]

@app.get("/")
async def root():
    return {'Greetings': 'Habari yako, Karibu hapa'}


@app.get('/api/get-all-users')
async def get_all_users():
    return db;

@app.post('/api/add-user/')
async def add_user(user: User):
    db.append(user)
    return {'new_user_id': user.id}

@app.put('/api/update-user/{username}')
async def update_user(user_update: UpdateUser, username: str):
    for user in db:
        if user.name == username:
            user.email = user_update.email
            user.gender = user_update.gender
            user.roles = user_update.roles
            return user_update
        raise HTTPException(
            status_code=404,
            detail=f"User with name {username} does not exist"
        )


@app.delete('/api/delete-user/{username}')
async def delete_user(username: str):
    for user in db:
        if user.name == username:
            db.remove(user)
            return {'message': f'User {username} has been deleted'}
        raise HTTPException(
            status_code=404,
            detail=f"User with name {username} does not exist"
        )
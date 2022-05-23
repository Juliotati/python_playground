from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/{limit}")
def get_users(limit: int = 10):
    # Awaiting functionally from the db
    pass


@router.get("/{user_id}")
def get_user(user_id: int):
    print(f'could not find a user with the given id: {user_id}')


@router.put("/{user_id}")
def update_user(user_id: str):
    return {"message": f" Updated user{user_id}"}


@router.post("/")
def add_user():
    return {"message": f"Added new user"}


@router.delete("/{user_id}")
def delete_user(user_id: str):
    return {"message": f"Deleted user with id {user_id}"}

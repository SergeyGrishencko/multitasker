from fastapi import APIRouter, HTTPException, status, Response

from src.app.users.schemas import RegisterUserSchema, LoginUserSchema
from src.db.users.repository import UserRepository
from src.db.users.auth import UserAuth, authentificate_user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user_data: RegisterUserSchema):
    is_user = await UserRepository.get_one_or_none(email=user_data.email)
    if is_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = UserAuth.get_password_hash(user_data.password)
    await UserRepository.create_object(
        username=user_data.username, 
        email=user_data.email, 
        hashed_password=hashed_password
    )

@router.post("/login")
async def login_user(response: Response, user_data: LoginUserSchema):
    is_user = await authentificate_user(user_data.email, user_data.password)
    if not is_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = UserAuth.create_access_token({"sub": str(is_user.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("user_access_token")
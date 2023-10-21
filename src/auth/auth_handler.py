import time
from datetime import datetime, timedelta
from typing import Union

import jwt
from decouple import config

from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from src.auth.auth_model import Token, UserInDB, TokenData


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


users_db = {
    "issamb": {
        "username": "issamb",
        "hashed_password": "$2b$12$d7PF1B4vr.y8XdgyE1B5zuWiL2f/0Sri7e9BCoek4DAvQvKEAskq2",
        "role": "admin",
    },
    "marceldg": {
        "username" : "marceldg",
        "hashed_password": "$2b$12$03CDBSNyJ6KHNuN0..qwr.7ppwAJNCUISTPMJ3jwXSr7LuDGONc6G",
        "role": "admin",
    },
    "guest": {
        "username": "guest",
        "hashed_password": "$2b$12$kf4.6duEpMj6wbP77jeazu58shGS111p7QD56WYywulU6vSiCCgx2",
        "role": "user",
    },
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$Bt10sxMTRbwflfAVfhX1ser/4kTxGP7G8kLTgAbGWzFoU1QrqBZFu",
        "role": "admin",
    }
}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=600)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

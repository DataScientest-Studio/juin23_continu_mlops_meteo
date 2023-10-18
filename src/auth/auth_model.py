# Test

from pydantic import BaseModel, Field, EmailStr
from typing import Union


class User(BaseModel):
    """ Le format des champs constituant la classe User (informations nécessaires à l'autorisation, ici seul le username et role sont récupérés)
    """
    username: str = Field(...)
    role: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "identifiant": "issamb",
                "password": "weakpassword",
                "role" : "admin"
            }
        }


class UserLoginSchema(BaseModel):
    """ Le format des champs constituant la classe UserLoginSchema (informations nécessaires à l'authentification)
    """
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "issamb",
                "password": "weakpassword"
            }
        }


class UserInDB(User):
    """ Cette classe permet de récupérer le mot de passe crypté pour vérifier la présnece de l'utilisateur dans la BDD avant de le connecter
    """
    hashed_password: str


class Token(BaseModel):
    """ Classe permettant de récupérer les informations nécessaires à la gestion des Token de connexion
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

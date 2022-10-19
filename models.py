from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    supervisor = 'supervisor'
    amateur = 'amateur'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    email: str
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    email: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]
from pydantic import BaseModel
from typing import Dict


class Calling(BaseModel):
	prompt: str

class Type(BaseModel):
	type: str

class Definition(BaseModel):
	name: str
	description: str
	parameters: Dict[str, Type]
	returns : Type
from pydantic import BaseModel, ConfigDict
from typing import Dict


class Calling(BaseModel):
	model_config = ConfigDict(extra="forbid")
	prompt: str

class Type(BaseModel):
	model_config = ConfigDict(extra="forbid")
	type: str

class Definition(BaseModel):
	model_config = ConfigDict(extra="forbid")
	name: str
	description: str
	parameters: Dict[str, Type]
	returns : Type
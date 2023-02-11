import BaseModel


MAC = 'MacOS'
UBUNTU = 'Ubuntu'
WINDOWS = 'Windows'

# @todo: Define a range of records.

class OS(BaseModel):
    type: str

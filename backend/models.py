from pydantic import BaseModel


# fix inherit
class Item(BaseModel):
    name: str
    description: str


class User(BaseModel):
    username: str
    bio: str

    # You can raise your hands and give the answer to the chocolate question

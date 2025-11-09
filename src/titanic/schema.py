from pydantic import BaseModel, confloat, conint
from typing import Optional

class TitanicInput(BaseModel):
    Pclass: conint(ge=1, le=3)
    Sex: str
    Age: Optional[confloat(ge=0)]
    SibSp: conint(ge=0)
    Parch: conint(ge=0)
    Fare: Optional[confloat(ge=0)]
    Embarked: Optional[str]
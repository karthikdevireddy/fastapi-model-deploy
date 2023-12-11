from pydantic import BaseModel

# Define a Pydantic model for the input data
class Income(BaseModel):
    officearea: float
    comarea: float
    yearbuilt: int
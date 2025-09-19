import datetime
from typing import Literal, Union, Optional, Any, Callable

from pydantic import BaseModel

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: Optional[float] = None

class Prediction(BaseModel):
    value: Literal["virginica", "versicolor", "setosa"]
    dt: datetime.datetime

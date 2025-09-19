import io

import seaborn as sns
import matplotlib.pyplot as plt

from typing import Literal
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/data",
    tags=["Data"]
)

iris_df = sns.load_dataset("iris")

@router.get("/histogram")
def hist(
    column: Literal["sepal_width", "sepal_length", "petal_width", "petal_length"],
    species: Literal["virginica", "versicolor", "setosa"]
    ) -> StreamingResponse:

    fig = plt.figure()

    sns.histplot(iris_df[iris_df["species"] == species][column]) # type: ignore

    buffer = io.BytesIO()
    fig.savefig(buffer)

    buffer.seek(0)

    plt.close(fig)

    return StreamingResponse(content=buffer, media_type="image/png")
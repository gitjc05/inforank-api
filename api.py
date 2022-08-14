from fastapi import FastAPI
from pydantic import BaseModel
from main import ranker


app = FastAPI()

class RankerItem(BaseModel):
    text: str
    sentence_limit: str


@app.post('/')
async def scoring_endpoint(item:RankerItem):
    return item
    context = ranker(text=item.text, sentence_lim=item.sentence_limit)

    

    return context
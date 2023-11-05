from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from pydantic import BaseModel
from typing import Optional
import datetime
import asyncio

class Message(BaseModel):
    text: str
    sentBy: str
    sentAt: datetime.datetime
    isChatOwner: Optional[bool] = None

router = APIRouter(
    prefix="/api/execute",
    tags=["execute"],
    include_in_schema=False,
    responses={404: {"description": "Not found"}},
)

@router.post("/message", response_model=Message)
async def execute(message: Message) -> Message:
    # Your processing here
    await asyncio.sleep(3)
    dummy_message = Message(
        text="testing london breed",
        sentBy="London",
        sentAt=datetime.datetime.now(),
        isChatOwner=False,
    )
    reply_message = dummy_message
    return reply_message
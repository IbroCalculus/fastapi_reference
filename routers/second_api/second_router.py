from fastapi import APIRouter

router = APIRouter(prefix='/api/v2', tags=["second group"])


@router.get('/welcome')
async def welcome():
    return {"message": "Welcome to second router"}


@router.get('/getValues')
async def getValues():
    values = [x for x in range(5,9)]
    return {"values": values}

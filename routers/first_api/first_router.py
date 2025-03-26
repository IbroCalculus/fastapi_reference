from fastapi import APIRouter

router = APIRouter(prefix='/api/v1', tags=["first group"])


@router.get('/')
async def index():
    return {"message": "Hello, this is the first group endpoint"}


@router.get('/getValues')
async def getValues():
    values = [x for x in range(4)]
    return {"values": values}

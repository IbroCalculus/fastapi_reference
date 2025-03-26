from fastapi import FastAPI

app = FastAPI()

"""
# ========================= 1. ADD RETURN TYPE ============================

@app.get("/")
async def index() ->  dict:      // Return a dictionary of strings, Any datatype
    return {"message": "Hello World", "error": "Error message", "age": 30}

@app.get("/")
async def index() -> list[str]: // Return a list of strings
    return ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

# ===========================
    

"""

from fastapi import FastAPI, HTTPException, Path
from typing import Union

from starlette import status

app = FastAPI()


# ========= 1. Simple get request ==========
# http://127.0.0.1:8000/
@app.get("/", status_code=status.HTTP_200_OK, tags=["group 1"])
def root():
    return {"Hello": "World"}
    # return "It can simply be a string of text"


# ========= 2. Another example of a simple get request with a different endpoint ==========
# http://127.0.0.1:8000/fruits
@app.get("/fruits", tags=["group 1"])
def get_fruits():
    return {
        "fruit1": "Mango",
        "fruit2": "Banana",
        "fruit3": "Orange",
        "fruit4": "Paw paw",
        "fruit5": "Cashew",
        "fruit6": "Guava",
        "fruit7": "Plantain"
    }


# NB: There are 2 ways of passing parameters, either as; path parameters, or as query parameters

# ========= 3.  Get request with parameter E.g1 (Using path parameter)   ==========

# http://127.0.0.1:8000/message/IbrahimCalculus
@app.get("/message/{username}", tags=["group 2"], )
def get_message(username):
    return f'You are welcome aboard Mr {username}'


# ========= 4.  Get request with parameters E.g2 (Using path parameter)  ==========
inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "regular",
    },
    2: {
        "name": "Sugar",
        "price": "4.23",
        "brand": "condensed",
    }
}


# http://127.0.0.1:8000/get-item/1
@app.get("/get-item/{item_id}", tags=["group 2"])
def get_item(item_id: int):
    return inventory[item_id]


# ALTERNATIVELY, Same as above, but with error handling
# http://127.0.0.1:8000/get-item2/1
@app.get("/get-item2/{item_id}")
def get_item(item_id: int):
    try:
        item = inventory[item_id]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    return item


# ========= 5.  Get request with parameters E.g3 (Using path parameter) ==========
inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "regular",
    },
    2: {
        "name": "Sugar",
        "price": "4.23",
        "brand": "condensed",
    }
}


# http://127.0.0.1:8000/get-item/1/price
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str):
    item = inventory[item_id]
    value = item.get(name)
    return f'item name: {value}'


# ========= 6.  Get request with parameters, with PATH keyword E.g4 (Using path parameter) ==========
# The Path() method allows us to add more constraints to our path parameter, ie add a description of the parameter for user

inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "regular",
    },
    2: {
        "name": "Sugar",
        "price": "4.23",
        "brand": "condensed",
    }
}


# http://127.0.0.1:8000/get-item3/1
@app.get("/get-item3/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you would like to view", gt=0, lt=2)):      # gt=0 => must be greater than 0
    return inventory[item_id]

# NB: Path(None, description="The ID of the item you would like to view", gt=0, lt=2)): Where none is default, but for the above there can't be a default


# ========= 7.  Get request with multiple parameters ==========
# http://127.0.0.1:8000/adder/2,5
@app.get("/adder/{num1},{num2}")  # OR: @app.get("/adder/{num1}/{num2}") -> http://127.0.0.1:8000/adder/2/5
def add_both(num1, num2):
    sum_of_both = int(num1) + int(num2)
    return f'{num1} + {num2} = {sum_of_both}'




# ========= 8.  Get request with parameters E.g (Using query parameter) ==========
inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "regular",
    },
    2: {
        "name": "Sugar",
        "price": "4.23",
        "brand": "condensed",
    }
}


# http://127.0.0.1:8000/get-by-name?name=Milk
@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory.keys():
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}


# http://127.0.0.1:8000/get-by-name2?name=Milk&test=5    (NB: test=5 has no use here, just to depict passing multiple query parameters)
@app.get("/get-by-name2")
def get_item(*, name: str, test: int):
    for item_id in inventory.keys():
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}


# ========= 9.  Get request with parameters E.g (Using both path & query parameter) ==========

# http://127.0.0.1:8000/get-by-name3/1?name=Milk&test=5    # TODO: (Confusing, I have to look at it again)
@app.get("/get-by-name3/{item_id}")
def get_item(*, item_id: int, name: str, test: int):
    for item_id in inventory.keys():
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}
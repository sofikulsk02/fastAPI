# from fastapi import FastAPI


# app=FastAPI()

# BOOKS=[
#     {'title':"Title one","author":"Author one","category":"Science"},
#     {'title':"Title two","author":"Author two","category":"Fiction"},
#     {'title':"Title three","author":"Author three","category":"History"},
#     {'title':"Title four","author":"Author four","category":"Science"},
#     {'title':"Title five","author":"Author five","category":"Fiction"},
#     {'title':"Title six","author":"Author two","category":"History"},
# ]

# @app.get("/books")
# async def read_all_books():
#     return BOOKS

# @app.get("/books/my_book")
# async def read_all_books():
#     return {"title":"My favorite book"}

# @app.get("books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {"dynamic_param":dynamic_param}





from fastapi import FastAPI

app=FastAPI();

BOOKS=[
    {'title':"Title one","author":"Author one","category":"Science"},
    {'title':"Title two","author":"Author two","category":"Fiction"},
    {'title':"Title three","author":"Author three","category":"History"},
    {'title':"Title four","author":"Author four","category":"Science"},
    {'title':"Title five","author":"Author five","category":"Fiction"},
    {'title':"Title six","author":"Author two","category":"History"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS;


@app.get('/books/my_book')
async def read_all_books():
    return {"title":"my fav book"}

@app.get("/books/{dynamic_params}")
async def read_all_books(dynamic_params):
    return {"dynamic_params":dynamic_params}


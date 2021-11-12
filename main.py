from fastapi import FastAPI
# FastAPIは、APIのすべての機能を提供するPythonクラス

app = FastAPI()
# FastAPIのインスタンスを生成

@app.get("/")
# パスオペレーションデコレータ
# 直下の関数が下記のリクエストの処理を担当することをFastAPIに伝える
async def root():
    # パスオペレーション関数
    # asyncではなく通常の関数でもOK！
    return {"message": "Hello world"}
    # dict型、list型、str型、int型などを返すことができる

@app.get("/items/{item_id}")
# パスパラメータ item_idの値は引数item_idが渡される。(なんでもOK！)
async def read_item(item_id: int):
    # int型のitem_idを渡すようにする。int型のものが渡されている
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"/user_id": "the current user"}

@app.get("/users/{user_id}")
# パスパラメータuser_idの値は引数user_idが渡される。str型で定義されているので、str型のパスパラメータしか渡せない
# パスパラメーターmeともマッチする
async def read_user(user_id: str):
    return {"/user_id": user_id}
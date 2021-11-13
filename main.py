from enum import Enum

from fastapi import FastAPI
# FastAPIは、APIのすべての機能を提供するPythonクラス

class ModelName(str, Enum):
    # strとEnumを継承したサブクラス
    # 第一引数strを継承することで値が文字列でなければいけないようになり正確にレンダリングできるようになる。
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    # 固定値のクラス属性を作り、その値が使用可能な値となる。

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

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # ModelNameクラスではstr型を定義しているので値は文字列にならないといけない。
    if model_name == ModelName.alexnet:
        # クラス名 + .で取得(この場合はstr型)
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
from fastapi import APIRouter

router = APIRouter()

@router.get("/{id}")
def get_article(id: int):
    return {"id": id, "title": "测试文章"}

@router.post("/")
def create_article():
    return {"msg": "创建文章成功"}

from fastapi import FastAPI
from routers.article import router as article_router

app = FastAPI()

app.include_router(article_router, prefix="/api/article", tags=["文章接口"])

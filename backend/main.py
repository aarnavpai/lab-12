from fastapi import FastAPI
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router
from routes.users import router as users_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# fix cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(users_router, prefix="/users")
app.include_router(quiz_router, prefix="/quiz")


# why the hell did I write this function?
@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}

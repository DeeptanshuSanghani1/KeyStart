from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import gcp_upload_router


app = FastAPI()
app.title = "piano-project"


api = FastAPI(root_path="/api")
api.title = "piano-project api"
app.mount("/api", api, name="api")

api.include_router(gcp_upload_router.router, prefix="/upload")

# Allow Front-end Origin in local development
origins = ["http://localhost:3000",
           "http://192.168.2.72:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/healthcheck")
async def healthcheck():
    """
    Endpoint to verify that the service is up and running
    """
    return {"status": "backen is running"}




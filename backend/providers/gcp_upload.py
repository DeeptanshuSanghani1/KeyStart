from fastapi import HTTPException, UploadFile
from google.cloud import storage
from google.oauth2 import service_account
from backend.constants import settings



async def upload_file_to_bucket(file : UploadFile):
    credentials = service_account.Credentials.from_service_account_info(settings.google_cloud_credentials)
    client = storage.Client(credentials=credentials)
    if(file.content_type not in ['audio/midi', 'audio/x-midi', 'audio/mid']):
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Upload the file to Google Cloud Storage
    bucket = client.get_bucket("key_start_bucket")
    blob = bucket.blob(file.filename)
    try:
        blob.upload_from_file(file.file, content_type=file.content_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")


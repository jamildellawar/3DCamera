import os.path

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def uploadFile(filePath, fileName):	
	# If modifying these scopes, delete the file token.json.
	SCOPES = ["https://www.googleapis.com/auth/drive.file"]
	
	creds = None
	
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
	if os.path.exists("token.json"):
		creds = Credentials.from_authorized_user_file("token.json", SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				"credentials.json", SCOPES
			)
			creds = flow.run_local_server(port=0)
        
		# Save the credentials for the next run
		with open("token.json", "w") as token:
			token.write(creds.to_json())

	try:
		# create drive api client
		service = build("drive", "v3", credentials=creds)
		
		fileMetadata = {"name": f"{fileName}.mp4"}
		media = MediaFileUpload(filePath, mimetype="video/mp4")
		
		uploadedFile = service.files().create(body=fileMetadata, media_body=media, fields="id").execute()
		print(uploadedFile)
		
	except HttpError as error:
		print(f"An Error ocurred: {error}")
		uploadedFile = None
		
	return uploadedFile.get("id")
		
uploadFile("/home/jamilspi/Code/3DCamera/Videos/Video2.mp4", "3dcamera1")

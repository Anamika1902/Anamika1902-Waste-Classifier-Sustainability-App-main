from firebase_admin import credentials, initialize_app

def initialize_firebase():
    try:
        cred = credentials.Certificate("waste-classifier-be072-95e026b8db39.json")
        return initialize_app(cred)
    except ValueError:
        # Firebase app already exists, return None or handle the error as needed
        pass

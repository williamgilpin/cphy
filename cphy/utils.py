import os
import sys

from hashlib import sha256

def hash_string(s: str) -> str:
    """
    Hashes a string using SHA-256.

    Args:
        s (str): The string to hash.

    Returns:
        str: The SHA-256 hash of the string.
    """
    return sha256(s.encode()).hexdigest()

def fetch_userstring():
    """
    Fetches the user's email address if running in Google Colab, otherwise returns the local username.

    Returns:
        str: The user's email address if running in Google Colab, otherwise the local username.
            If there is an error fetching the user email, returns "no_user".

    """
    
    # Detect if running in Google Colab
    in_colab = "google.colab" in sys.modules
    
    if in_colab:

        print("Running in Google Colab." +
            "You will need to authenticate your Google account (prompted by the browser)" +
            "to use this function.", 
            flush=True
        )
        try:
            # In Colab: get Google account email
            from google.colab import auth
            auth.authenticate_user()
            
            import google.auth
            from google.auth.transport.requests import Request
            from googleapiclient.discovery import build
            
            creds, _ = google.auth.default()
            creds.refresh(Request())
            service = build('oauth2', 'v2', credentials=creds)
            user_info = service.userinfo().get().execute()
            return user_info['email']
        except Exception as e:
            print(f"Error fetching user email: {e}", flush=True)
            return "no_user"
    else:
        # Local: return username
        try:
            username = os.getlogin()
        except Exception:
            username = os.environ.get("USER") or os.environ.get("USERNAME")
        return username



    
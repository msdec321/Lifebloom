#!/usr/bin/env python3
"""
WarcraftLogs User Authentication (OAuth Authorization Code Flow)
Authenticates as a user to access subscription features like archived reports
"""

import os
import json
import time
import webbrowser
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OAuth Configuration
CLIENT_ID = os.getenv("WARCRAFTLOGS_CLIENT_ID")
CLIENT_SECRET = os.getenv("WARCRAFTLOGS_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8080/callback"
AUTH_URL = "https://www.warcraftlogs.com/oauth/authorize"
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
TOKEN_FILE = ".token.json"

# Request timeout and retry configuration
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries

# Global variable to store the authorization code
auth_code = None


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """HTTP request handler for OAuth callback"""

    def do_GET(self):
        """Handle GET request from OAuth redirect"""
        global auth_code

        # Parse the query parameters
        query_components = parse_qs(urlparse(self.path).query)

        if 'code' in query_components:
            auth_code = query_components['code'][0]

            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            success_html = """
            <html>
            <head><title>Authorization Successful</title></head>
            <body>
                <h1>Authorization Successful!</h1>
                <p>You have successfully authorized the application.</p>
                <p>You can close this window and return to the terminal.</p>
            </body>
            </html>
            """
            self.wfile.write(success_html.encode())
        else:
            # Send error response
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            error_html = """
            <html>
            <head><title>Authorization Failed</title></head>
            <body>
                <h1>Authorization Failed</h1>
                <p>There was an error during authorization.</p>
                <p>Please try again.</p>
            </body>
            </html>
            """
            self.wfile.write(error_html.encode())

    def log_message(self, format, *args):
        """Suppress default logging"""
        pass


def get_authorization_code():
    """
    Start the OAuth authorization flow.
    Opens a browser for user to authorize and starts a local server to receive the callback.
    Returns the authorization code.
    """
    global auth_code

    # Construct authorization URL
    auth_params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code'
    }

    auth_url_full = f"{AUTH_URL}?client_id={auth_params['client_id']}&redirect_uri={auth_params['redirect_uri']}&response_type={auth_params['response_type']}"

    print("Opening browser for authorization...")
    print(f"If the browser doesn't open automatically, visit this URL:")
    print(f"{auth_url_full}\n")

    # Open browser
    webbrowser.open(auth_url_full)

    # Start local server to receive callback
    print("Starting local server on http://localhost:8080 to receive callback...")
    server = HTTPServer(('localhost', 8080), OAuthCallbackHandler)

    # Handle one request (the callback)
    print("Waiting for authorization...")
    server.handle_request()
    server.server_close()

    if auth_code:
        print("✓ Authorization code received!\n")
        return auth_code
    else:
        raise Exception("Failed to receive authorization code")


def exchange_code_for_token(code):
    """
    Exchange authorization code for access token.
    Returns token data including access_token and refresh_token.
    """
    print("Exchanging authorization code for access token...")

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                TOKEN_URL,
                data={
                    'grant_type': 'authorization_code',
                    'code': code,
                    'redirect_uri': REDIRECT_URI
                },
                auth=(CLIENT_ID, CLIENT_SECRET),
                timeout=REQUEST_TIMEOUT
            )

            if response.status_code == 200:
                token_data = response.json()
                print("✓ Access token received!\n")
                return token_data
            else:
                error_msg = f"Failed to get access token: {response.status_code} - {response.text}"
                if attempt < MAX_RETRIES - 1:
                    print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {response.status_code}")
                    print(f"  Retrying in {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                else:
                    raise Exception(error_msg)

        except requests.exceptions.Timeout:
            if attempt < MAX_RETRIES - 1:
                print(f"  Attempt {attempt + 1}/{MAX_RETRIES} timed out after {REQUEST_TIMEOUT}s")
                print(f"  Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise Exception(f"Token exchange timed out after {MAX_RETRIES} attempts")

        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES - 1:
                print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
                print(f"  Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise Exception(f"Token exchange failed after {MAX_RETRIES} attempts: {e}")

    raise Exception("Failed to exchange code for token after all retries")


def save_token(token_data):
    """Save token data to file"""
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f, indent=2)
    print(f"✓ Token saved to {TOKEN_FILE}\n")


def load_token():
    """Load token data from file or environment variable"""
    # First, check for token in environment variable (for production deployments)
    env_token = os.getenv('WARCRAFTLOGS_TOKEN_JSON')
    if env_token:
        try:
            return json.loads(env_token)
        except json.JSONDecodeError:
            print("Warning: WARCRAFTLOGS_TOKEN_JSON environment variable is not valid JSON")

    # Fall back to file
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return json.load(f)
    return None


def refresh_access_token(refresh_token):
    """
    Refresh the access token using a refresh token.
    Returns new token data.
    """
    print("Refreshing access token...")

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                TOKEN_URL,
                data={
                    'grant_type': 'refresh_token',
                    'refresh_token': refresh_token
                },
                auth=(CLIENT_ID, CLIENT_SECRET),
                timeout=REQUEST_TIMEOUT
            )

            if response.status_code == 200:
                token_data = response.json()
                print("✓ Access token refreshed!\n")
                return token_data
            else:
                error_msg = f"Failed to refresh token: {response.status_code} - {response.text}"
                if attempt < MAX_RETRIES - 1:
                    print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {response.status_code}")
                    print(f"  Retrying in {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                else:
                    raise Exception(error_msg)

        except requests.exceptions.Timeout:
            if attempt < MAX_RETRIES - 1:
                print(f"  Attempt {attempt + 1}/{MAX_RETRIES} timed out after {REQUEST_TIMEOUT}s")
                print(f"  Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise Exception(f"Token refresh timed out after {MAX_RETRIES} attempts")

        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES - 1:
                print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
                print(f"  Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise Exception(f"Token refresh failed after {MAX_RETRIES} attempts: {e}")

    raise Exception("Failed to refresh token after all retries")


def get_user_access_token(force_reauth=False):
    """
    Get a valid user access token.
    Uses saved token if available, refreshes if needed, or performs full auth flow.

    Args:
        force_reauth: Force a new authentication flow even if token exists

    Returns:
        Access token string
    """
    # Check if running in production (Railway sets RAILWAY_ENVIRONMENT)
    is_production = os.getenv('RAILWAY_ENVIRONMENT') is not None or os.getenv('PRODUCTION') is not None

    # Check if token is from environment variable (don't refresh these - they're valid for 1 year)
    env_token = os.getenv('WARCRAFTLOGS_TOKEN_JSON')
    token_from_env = env_token is not None

    if not force_reauth:
        # Try to load existing token
        token_data = load_token()

        if token_data and 'access_token' in token_data:
            # If token is from environment variable, use it directly without refreshing
            # These tokens are valid for 1 year and refreshing would invalidate the env var token
            if token_from_env:
                print("Using access token from environment variable...")
                return token_data['access_token']

            # For file-based tokens, try to refresh to keep them fresh
            if 'refresh_token' in token_data:
                try:
                    # Try to refresh the token
                    new_token_data = refresh_access_token(token_data['refresh_token'])
                    save_token(new_token_data)
                    return new_token_data['access_token']
                except Exception as e:
                    print(f"Failed to refresh token: {e}")
                    # Fall back to existing token
                    print("Using existing access token...")
                    return token_data['access_token']
            else:
                # No refresh token, just use the access token
                print("Using existing access token from file...")
                return token_data['access_token']

    # In production, don't attempt interactive OAuth
    if is_production:
        raise Exception("Interactive authentication not available in production. Please authenticate locally first, then deploy with a valid .token.json file.")

    # Perform full OAuth flow
    print("=" * 70)
    print("USER AUTHENTICATION REQUIRED")
    print("=" * 70)
    print("You will be redirected to WarcraftLogs to authorize this application.")
    print("This is required to access archived reports with your subscription.\n")

    code = get_authorization_code()
    token_data = exchange_code_for_token(code)
    save_token(token_data)

    return token_data['access_token']


def main():
    """Main function for testing authentication"""
    print("WarcraftLogs User Authentication\n")

    try:
        access_token = get_user_access_token()
        print("=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print(f"Access token: {access_token[:20]}...")
        print("\nYou can now use this token to access archived reports and other")
        print("subscription features.")
        print("\nThe token has been saved and will be reused for future requests.")

    except Exception as e:
        print(f"\nError: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

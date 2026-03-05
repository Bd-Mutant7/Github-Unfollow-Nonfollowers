import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# GitHub configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', 'your_token_here')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'your_username_here')

# API configuration
API_BASE_URL = 'https://api.github.com'
REQUEST_TIMEOUT = 10  # seconds

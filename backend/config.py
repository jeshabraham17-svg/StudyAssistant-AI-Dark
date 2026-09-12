import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
MODEL_NAME = os.getenv('MODEL_NAME', 'mistral')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')

# Flask Configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)

# API Configuration
API_PORT = int(os.getenv('API_PORT', 5000))
API_HOST = os.getenv('API_HOST', '0.0.0.0')

# CORS Settings (for security)
ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5000',
]

# AI Behavior
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))  # 0.0-1.0, lower = more deterministic
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2000))
TOP_P = float(os.getenv('TOP_P', 0.9))

from fastapi.middleware.cors import CORSMiddleware

config = {
    "allow_origins": [
        "http://localhost",
        "http://localhost:8000",
    ],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "max_age": 600,
}
CORS_MIDDLEWARE = (CORSMiddleware, config)

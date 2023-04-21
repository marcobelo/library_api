from fastapi.middleware.trustedhost import TrustedHostMiddleware

config = {"allowed_hosts": ["*"]}
TRUSTED_HOST_MIDDLEWARE = (TrustedHostMiddleware, config)

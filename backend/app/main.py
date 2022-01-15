from starlite import Starlite, OpenAPIConfig, get

from app.api.router import router as api_router


@get(path="/")
def health_check() -> str:
    return "healthy"


app = Starlite(
    route_handlers=[health_check, api_router],
    openapi_config=OpenAPIConfig(title="API", version="1.0.0"),
)

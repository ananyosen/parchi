# from https://github.com/fastapi/fastapi/discussions/7618#discussioncomment-7937666

from starlette.responses import Response
from starlette.types import Scope

from starlette.staticfiles import StaticFiles

class CacheControlledStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        response = await super().get_response(path, scope)
        response.headers["Cache-Control"] = "public, max-age=31536000"
        return response
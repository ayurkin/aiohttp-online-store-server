from aiohttp import web
from .db import setup_mongo
from .views import routes
from .config import Config


def init(config: Config) -> web.Application:
    app = web.Application()
    app['config'] = config
    app.on_startup.append(setup_mongo)
    app.add_routes(routes)
    return app


if __name__ == '__main__':
    config = Config()
    app = init(config)
    web.run_app(app, port=config.PORT)

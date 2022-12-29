import asyncio
import datetime

from sanic import Sanic
from sanic.response import json
from sanic.log import logger


app = Sanic("MyHelloWorldApp")


class TimeManager:
    _started_at = datetime.datetime.now()

    async def update_time(self):
        logger.info("Initializing startup timer...")
        self._started_at = datetime.datetime.now()
        logger.info("Captured time of the server startup is %s", self.started_at.isoformat())

    @property
    def started_at(self):
        return self._started_at


@app.get("/info")
async def info_req_handler(request):
    started_at = app.ctx.timemanager.started_at
    uptime_timedelta = datetime.datetime.now() - started_at
    return json({
        "ip": request.ip,
        "uptime": str(uptime_timedelta),
        "started_at": started_at.isoformat(),
    })


async def init_timemanager(app, loop):
    timemanager = TimeManager()
    app.ctx.timemanager = timemanager
    asyncio.ensure_future(timemanager.update_time(), loop=loop)


@app.before_server_start
async def on_server_start(app, loop):
    logger.info("Pre-start hooks")
    await init_timemanager(app, loop)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

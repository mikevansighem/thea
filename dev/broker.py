import logging
import asyncio
import os
from hbmqtt.broker import Broker
import yaml

logger = logging.getLogger(__name__)

# TODO move to constant
stream = open("broker_config.yml", "r")
broker_config = yaml.load(stream)


@asyncio.coroutine
def broker_coro():
    broker = Broker(broker_config)
    yield from broker.start()


if __name__ == "__main__":

    # TODO: remove
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)

    broker = Broker(broker_config)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(broker.start())

    print("here")

    loop.run_forever()

    while True:
        pass

"""Module with classes used to communicate with hardware. """

import time
from multiprocessing import Queue, Process
import logging

from .base_itemstore import BaseItem, BaseStore
from .communicator_types import COMMUNICATOR_TYPES
from .exceptions import CommNotConnectedError

REMAINING_MESSAGES_TIMEOUT = 3  # seconds
COMM_STARTUP_TIME = 5  # seconds

logger = logging.getLogger(__name__)


class Communicator(BaseItem):
    """A communicator is a object that connects with hardware."""

    # Define attributes that should be changed when inheriting this class
    type_dict = COMMUNICATOR_TYPES

    def _additional_attributes(self, **kwargs) -> dict:
        """Handles setting attributes not defined in the BaseItem class"""

        # Set initial status
        self.message_queue = Queue(maxsize=20)

        # Create (MQTT) communicator daemon process
        self.comm_handler = self.type_dict[self.type_].comm_handler

        return kwargs

    def _additional_init(self):
        """Setup MQTT comm handler"""

        self.comm_handler = Process(
            target=self.comm_handler,
            args=(self.message_queue, self.properties),
            daemon=True,
        )

    @property
    def status(self):
        """Returns weather the comm handling process is running."""

        return self.comm_handler.is_alive()

    def send_message(self, adress, data):
        """Adds message to the message queue to be send by the daemon communicator process."""

        if self.status is False:
            raise CommNotConnectedError(f"{self} is not connected.")
        else:
            self.message_queue.put((adress, data))

    def connect(self):
        """Sets-up the connection in a daemon process."""

        if self.status is False:

            logger.info(f"Started connecting '{self}'")

            # Start daemon process
            self.comm_handler.start()

            # Some time for the process to start
            time.sleep(COMM_STARTUP_TIME)

            # Check if the communicator process is running
            if self.status is True:
                logger.info(f"Successfully connected '{self}'")
            else:
                raise CommNotConnectedError(f"Could not connect '{self}'")

        else:
            logger.warning(f"'{self}' has already been connected.")

    def disconnect(self):
        """Disconnect and shutdown the daemon process. While allowing
        some time for the message queue tom clear."""

        # TODO does this kill the broker?

        if self.status is True:

            disconnect_time = time.time()

            # Some time to clear the message queue
            while (self.message_queue.qsize() > 0) or (
                (time.time() - disconnect_time) > REMAINING_MESSAGES_TIMEOUT
            ):
                # small time delay to prevent a "racing loop"
                time.sleep(0.01)

            len_unsend_messages = self.message_queue.qsize()

            # Kill daemon process in a while loop to prevent this function
            # from exiting while the process is still shutting down
            while self.status is not False:
                self.comm_handler.terminate()

            # Flush the queue
            while not self.message_queue.empty():
                self.message_queue.get()

            logger.info(
                f"Disconnected {self} and deleted {len_unsend_messages} unsent messages."
            )

            # TODO refresh the process


class CommunicatorStore(BaseStore):

    item_to_create = Communicator

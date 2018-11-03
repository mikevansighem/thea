"""Module with classes used to communicate with hardware. """

from base_itemstore import BaseItem, BaseStore
from communicator_types import COMMUNICATOR_TYPES
from exceptions import CommNotConnectedError
from multiprocessing import Queue, Process
import logging_setup

logger = logging_setup.aux_logger()


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
            args=(self.message_queue, *self.properties),
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

            # Start daemon process
            self.comm_handler.start()

            # TODO: Wait for confirmation of connection
            # TODO: Status is retried from the thread

    def disconnect(self):
        """Disconnect and shutdown the daemon process."""

        if self.status is True:

            # TODO: add some time to clear the message queue

            no_unsend_messages = len(self.message_queue)

            # Kill daemon process
            self.comm_handler.terminate()

            # Flush the queue
            while not self.message_queue.empty():
                self.message_queue.get()

            logger.info(
                f"Disconnected {self} and deleted {no_unsend_messages} unsent messages."
            )


class CommunicatorStore(BaseStore):

    item_to_create = Communicator

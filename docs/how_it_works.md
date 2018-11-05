# 👓 How it works

## Definitions

Throughout the source-code for Theia we use a variety of terms the most
import of which are defined below:

-   Theia world: An object in which all other objects are stored. A world can be saved
    to a file.
-   Environment: simulated state by which things are surrounded.
-   Thing: object in the "World" that can be controlled such as a house or a streetlight.
-   Communicator: object to communicate with hardware modules.
-   MQTT hardware module: physical device with pins connected to MQTT network.
-   Topic: (sub-)address on the MQTT communication channel.
-   Functional endpoint: Object to control the behavior of one of multiple endpoints.
-   Endpoint: object to control the behavior of one or multiple pins.
-   Pin: physical output of a controller board such as the Raspberry Pi.

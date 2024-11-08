# The TCP IP stack and MAC addresses

## The TCP/IP protocol

- One of the most important protocols in stack use currently

- A set of networking protocols, consisting of four layers all working together

- Incoming and outgoing packets pass though the layers during communication on a network

## TCP/IP protocol layers

### Application

- A message is passed through the layers

- The application layer uses an appropriate protocol based on the application being used to transmit data

### Transport

- This uses the TCP part

- responsible for end to end connection

- Once connection established, data is split to be transmitted into packets

- Adds:
    - Packet number
    - Total number of packets
    - Port number the packets should use

### Network

- Adds a source and destination IP address to each packet

- All routers operate on this layer

- They use the IP address to know the destination the packet is going

- socket = IP + Port

- Socket tells you:
    - The device the packet is going to
    - What application on the device needs the packet

### Link

- Represents the physical connection between nodes

- Responsible for adding MAC address of the source device and of the destination device

- The MAC address is changed on each hop of the route

## MAC address

- 12 digit hex code, unique

- Hard coded during manufacturing to every single NIC

- Can identify a device with one

- IP addresses operate on layer 3, MAC addresses operate on layer 2
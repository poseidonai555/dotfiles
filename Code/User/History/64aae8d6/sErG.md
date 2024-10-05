# Packets and packet switching

## What are the components of a packet

- Packet sequence number 

- Source IP address

- Destination IP address

- Source MAC address

- Destination IP address

- Checksum 

- Data

## What does the packet sequence do?

- Breaks the data into multiple packets that are numbered and sent in a certain order

## What is packet switching

- The network interface card receives a message to send out data

- THE NIC splits the message into a number of equally sized packets and numbers them, a checksum is calculated for each packet and added to the end of it

- The packets are routed to the ISP and checked for errors

- The packets are routed to the next node my the router, depending on the bandwidth and connection, the packets may take different routes

- The packets arrive at the ISP of the destination computer

- TCP reorders the packets upon arrival, using the packet sequence numbers of the packets
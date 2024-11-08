# The structure of IP addresses

## IPv4

- 32 bits used

- Range from 000.000.000.000 — 255.255.255.255

- Around 4 billion possible IP addresses

- There are however some special revered |IP addresses:
    - 127.x.x.x :These are private, non-routable addresses used for diagnostics within LANs
    - X.x.x.0 : This address is reserved as a network identifier
    - x.x.x.225 :This address is reserved as a broadcast address on a subnet (sends message to all hosts)
    - x.x.x.1 - Typically used as the default address of a router

# Parts of an IPv4 address

- Network identifier, this is the first 3 bytes

- Host identifier, this is the last byte

- Historically a system of classes was used to define the network / host portions of IPv4 addresses

- This divided the network / host parts in a few fixed ways

- Class A = 1: Network identifier, 3: Host identifier
- Class B = 2: Network identifier, 2: Host identifier
- Class C = 3: Network identifier, 1: Host identifier


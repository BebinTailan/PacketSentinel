# PacketSentinel

[![ci](https://github.com/BebinTailan/PacketSentinel/actions/workflows/ci.yml/badge.svg)](https://github.com/BebinTailan/PacketSentinel/actions/workflows/ci.yml)

PacketSentinel reads network captures (PCAP) and flags suspicious behavior: port scans, ARP spoofing,
DNS tunneling and unusual outbound volumes. It is written in pure Python (standard library only), so
the packet decoders are implemented from the protocol specifications rather than wrapped from a library.

> **Status:** early development. See [docs/ROADMAP.md](docs/ROADMAP.md) for what is done and what is planned.

## Requirements

- Python 3.11+
- No third-party dependency

## Usage

```bash
python -m packetsentinel --version
```

More commands are added as features land (see the roadmap).

## Development

```bash
python -m unittest discover -s tests -v
```

## Scope

PacketSentinel is a defensive tool: it analyzes captures you are allowed to inspect (your own lab,
your own network, or public sample captures). It never sends traffic.

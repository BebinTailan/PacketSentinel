# Roadmap

Each feature is developed on its own branch (`feature/NN-slug`) and merged into `main` when complete.

## Milestone v0.2.0: read and decode

- [ ] **01 pcap-reader**: classic libpcap file reader (global header, both byte orders, micro/nanosecond timestamps, truncated-file handling)
- [ ] **02 link-and-ip-decoders**: Ethernet II, 802.1Q VLAN tag, ARP, IPv4 (options, fragments flag), IPv6 fixed header
- [ ] **03 transport-decoders**: TCP (flags, options length), UDP, ICMP/ICMPv6 types
- [ ] **04 dns-decoder**: DNS messages over UDP (header, questions, answers, name compression, common record types)

## Milestone v0.3.0: flows and detections

- [ ] **05 flow-table**: bidirectional 5-tuple flows with packet/byte counters, start/end times and TCP state hints
- [ ] **06 portscan-detector**: vertical and horizontal scan detection with configurable thresholds and time windows
- [ ] **07 arp-spoof-detector**: IP-to-MAC binding changes, gratuitous ARP bursts, duplicate MAC claims
- [ ] **08 dns-tunnel-detector**: long labels, high-entropy subdomains, TXT/NULL record volume per domain

## Milestone v1.0.0: reporting

- [ ] **09 exfil-detector**: per-host outbound volume baseline and rare-destination scoring
- [ ] **10 cli-and-reports**: `packetsentinel analyze <file>` with text, JSON and HTML reports, severity levels and exit codes

"""Command-line interface for PacketSentinel."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from packetsentinel import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level argument parser."""
    parser = argparse.ArgumentParser(prog="packetsentinel", description="Dependency-free PCAP analyzer that detects suspicious network behavior.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point. Returns a process exit code."""
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0

#!/usr/bin/env python3
"""Command-line interface for git-helper."""

import argparse
import sys
from . import __version__

def create_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="A CLI tool that simplifies common Git workflows"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"%(prog)s {__version__}"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Placeholder for subcommands - will be implemented in future versions
    pr_parser = subparsers.add_parser("pr", help="GitHub PR workflow helpers")
    pr_parser.add_argument(
        "action", 
        choices=["create", "list", "checkout"], 
        help="PR action to perform"
    )
    
    branch_parser = subparsers.add_parser("branch", help="Git branch workflow helpers")
    branch_parser.add_argument(
        "action", 
        choices=["cleanup", "list-current", "rename"], 
        help="Branch action to perform"
    )
    
    changelog_parser = subparsers.add_parser("changelog", help="Generate changelogs")
    changelog_parser.add_argument(
        "--format", 
        choices=["markdown", "json", "text"], 
        default="markdown",
        help="Output format for changelog"
    )
    
    return parser

def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Placeholder implementations - to be replaced with actual functionality
    if args.command == "pr":
        print(f"PR action: {args.action}")
        print("TODO: Implement PR workflow helpers")
        return 0
    elif args.command == "branch":
        print(f"Branch action: {args.action}")
        print("TODO: Implement branch workflow helpers")
        return 0
    elif args.command == "changelog":
        print(f"Generating changelog in {args.format} format")
        print("TODO: Implement changelog generation")
        return 0
    else:
        print(f"Unknown command: {args.command}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

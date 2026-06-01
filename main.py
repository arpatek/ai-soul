#!/usr/bin/env python3
import argparse
import logging
from core.agent import Agent


def main():
    parser = argparse.ArgumentParser(description="AI Agent — Claude-backed DevOps assistant")
    parser.add_argument("--prompt", metavar="TEXT", help="Single prompt (non-interactive)")
    parser.add_argument(
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        metavar="LEVEL",
    )
    parser.add_argument(
        "--no-confirm",
        action="store_true",
        help="Skip shell confirmation prompts",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(levelname)s %(name)s: %(message)s",
    )

    agent = Agent(no_confirm=args.no_confirm)

    if args.prompt:
        agent.run_once(args.prompt)
    else:
        agent.run()


if __name__ == "__main__":
    main()

import sys

from sephirothos.application import SephirothOS


def main() -> int:
    application = SephirothOS(sys.argv)
    return application.run()

if __name__ == "__main__":
    raise SystemExit(main())
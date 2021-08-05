from gendiff.scripts.cli import run
from gendiff import gendiff


def main():
    args = run()
    gendiff.output(args)


if __name__ == '__main__':
    main()
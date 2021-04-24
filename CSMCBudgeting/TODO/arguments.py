import argparse


def args_new_member():
    parser = argparse.ArgumentParser(description='A test program.')

    parser.add_argument("--name", help="Name of member.")
    parser.add_argument("--datejoined", help="Date joined - format YYYY-MM-DD")
    parser.add_argument("--dateleft", help="Date Left, leave blank if new member", nargs='?', default=None)
    return parser

import argparse
import sys
import logging

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.DEBUG

def main(number, other_number, output):
    logging.info(f'Dividing {number} and {other_number}')
    result = number / other_number
    print(f'the result is {result}', file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', type=int, help='the first number', default=1)
    parser.add_argument('-n2', type=int, help='the second number', default=1)
    parser.add_argument('-o', type=argparse.FileType('w'), help='the output file', default=sys.stdout)
    parser.add_argument('-l', dest='log', type=str, help='log file', default=None)
    args = parser.parse_args()
    if args.log:
        logging.basicConfig(filename=args.log, level=LOG_LEVEL, format=LOG_FORMAT)
    else:
        logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

    try:
        main(args.n1, args.n2, args.output)
    except Exception as exc:
        logging.exception("Error running task")
        exit(1)
#!/usr/bin/env python
import random
import string
import sys


def puts(val):
    sys.stdout.write(val)


def main(argv):

    if len(argv) < 2:
        command = 'string'
    else:
        command = argv[1]

    if command in ('string', 'letters'):
        if command == 'string':
            chars = string.letters + string.digits + string.punctuation
        else:
            chars = string.ascii_lowercase
        if len(argv) < 3:
            count = 40
        else:
            count = int(argv[2])
        puts(''.join(random.choice(chars) for i in xrange(count)))

    elif command == 'bool':
        puts(('no', 'yes')[random.getrandbits(1)])

    elif command == 'number':
        if len(argv) == 2:
            lower_bound = 10000
            upper_bound = 99999
        elif len(argv) == 3:
            lower_bound = 0
            upper_bound = int(argv[2])
        else:
            lower_bound = int(argv[2])
            upper_bound = int(argv[3])
        puts(str(random.randint(lower_bound, upper_bound)))

    else:
        sys.stderr.write('cannot generate random ' + command + '\n')
        exit(1)


if __name__ == '__main__':
    main(sys.argv)
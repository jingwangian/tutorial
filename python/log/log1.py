#!/usr/bin/env python3

import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)
logger = logging.getLogger('main')


def main():
    logger.info("main function")

    logger.info("main function %d", 100)

    logger.info("main function %s", 100)

    logger.warning("The input size [%d] is smaller than current size [%d]!", 100, 200)


if __name__ == '__main__':
    main()

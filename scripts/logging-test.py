import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    filename='logs/errors.log',
                    format = '%(asctime)s %(message)s')


def main():

    while True:
        try:
            1/0 #exception
            time.sleep(2)
        except Exception as e:
            logging.exception("error:")
            time.sleep(1)


if __name__ == "__main__":
    main()
from pyfirmata import Arduino, util
import time


def main():
    board = Arduino('/dev/tty.usbmodemFD121')
    #board = util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')

    iter8 = util.Iterator(board)
    iter8.start()

    LED = board.get_pin('a:0:o')

    print(LED.read())
    print(board.analog[0].read())

    board.pass_time(10)

    z=board.analog[0].read()
    print(z)

    board.exit()

if __name__ == "__main__":
    main()
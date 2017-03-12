if __name__ == "__main__":
    def a():
        try:
            12/0
        except Exception as er:
            print("smaller error")
            print(er)


    try:
        a()
    except Exception as er:
        print("big time error")
        print(er)
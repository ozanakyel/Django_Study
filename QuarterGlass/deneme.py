from threading import Thread
from time import sleep


class DenemeThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("başlatıldı")
        self.i = 0

    def result(self):
        print("def sayıcı çalıştırıldı")

        while self.i < 15:
            print(self.i)
            self.i += 1
            # if i == 999:
            #     print('basa dön'+ i + 'oldu')
            #     i = 0
            sleep(1)
            return self.i


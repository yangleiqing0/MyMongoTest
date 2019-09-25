from datetime import datetime


def get_num():
    num = 1
    while 1:
        if num < 10:
            n = '00{}'.format(num)
        elif num < 100:
            n = '0{}'.format(num)
        else:
            n = str(num)
        yield n
        num += 1


def get_number(num):

    timestr = datetime.now().strftime('%Y%m%d') + num
    print(timestr)
    return timestr


if __name__ == '__main__':
    get_number()
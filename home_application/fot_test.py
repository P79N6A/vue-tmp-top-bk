# -*- coding: utf-8 -*-


def func():
    a = 0
    b = False
    while a < 3 and not b:
        print a
        a += 1
        if a == 2:
            b = True


if __name__ == "__main__":
    func()

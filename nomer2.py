#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    first = set(str1)
    second = set(str2)

    a = first.intersection(second)
    print("Общие символы:", a)
#!/usr/bin/ env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "f", "i", "n", "o"}
    b = {"f", "g", "h", "l", "u"}
    c = {"i", "j", "u", "w"}
    d = {"e", "g", "l", "p", "q", "u", "v"}

    x = (a & c) | b
    print(f"x = {x}")

    bn = u.difference(b)
    y = (a.intersection(bn)).difference(c.difference(d))
    print(f"y = {y}")
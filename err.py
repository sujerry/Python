#!/usr/bin/env python3
#coding: utf-8

glo_list = []
glo_elem = None

for e in range(10):
    global glo_elem
    glo_elem = e
    glo_list.append(glo_elem)

print(glo_list)

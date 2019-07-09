# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:51:26 2018

@author: Yair
"""
import operator

def person_lister(f):
    def inner(people):
        return map(f,sorted(people,key=lambda p: int(p[2])))
    return inner


def wrapper(f):
    def fun(l):
        phones = ["+91" + p[1:]  if p.startswith("0") else p for p in l]
        phones = ["+91" + p  if len(p)<11 else p for p in phones]
        phones = [p.replace("91","+91",1)  if p.startswith("91") else p for p in phones]
        phones = map(lambda p : p[0:3] + " " + p[3:8]+ " " + p[8:], phones)
        f(phones)   
    return fun


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    people = [["Jake Jake 42 M"],
              ["Jake Kevin 57 M"],
              ["Jake Michael 91 M"],
              ["Kevin Jake 2 M"],
              ["Kevin Kevin 44 M"],
              ["Kevin Michael 100 M"],
              ["Michael Jake 4 M"],
              ["Michael Kevin 36 M"],
              ["Michael Michael 15 M"],
              ["Micheal Micheal 6 M]"]]
    people = [p[0].split() for p in people]
    l= ['07895462130', '919875641230', '9195969878']
    sort_phone(l) 
    print('\n')
    print(*name_format(people), sep='\n')
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def rtl(words):
    return words[::-1]

#regularity levels:
# 1 = check every week | very often
# 2 = check every 2-4 weeks | often
# 3 = check every 1-3 months | normal
# 4 = check every 3-6 months | rarely
# 5 = check every 6-12 months | very rarely

mainList = {
    rtl("אוכל"): {
        rtl("רגיל"): {},
        rtl("תבלינים"): {},
        rtl("פירות וירקות"): {},
        rtl("מותרות"): {},
        rtl("אביזרים"): {}
    },
    rtl("היגיינה"): {
        rtl("אישי"): {},
        rtl("בית"): {}
    },
    rtl("תינוק"): {
        rtl("כללי"): {}
    }
}

def updateListFromCode(cat, sub, item, reg = 3, note1 = None, note2 = None, note3 = None, label = None):
    mainList[cat][sub][len(mainList[cat][sub])+1] = ({"item": item, "regularity": reg, "note1": note1, "note2": note2, "note3": note3})

def updateListFromFileList():
    customFileR = open("./customList.txt", "r", encoding="UTF-8")

    index = 0
    cat = None
    sub = None
    item = None
    reg = None
    note1 = None
    note2 = None
    note3 = None
    for x in customFileR:
        if index == 0:
            cat = x[:-1]
        elif index == 1:
            sub = x[:-1]
        elif index == 2:
            item = rtl(x[:-1])
        elif index == 3:
            reg = rtl(x[:-1])
        elif index == 4:
            note1 = rtl(x[:-1])
        elif index == 5:
            note2 = rtl(x[:-1])
        elif index == 6:
            note3 = rtl(x[:-1])
            index = -1
        index += 1
        if cat != None and sub != None and item != None and reg != None and note1 != None and note2 != None and note3 != None:
            mainList[cat][sub][len(mainList[cat][sub])+1] = ({"item": item, "regularity": reg, "note1": note1, "note2": note2, "note3": note3})
            cat = None
            sub = None
            item = None
            reg = None
            note1 = None
            note2 = None
            note3 = None

    customFileR.close()

def resetFileList():
    customFileA = open("customList.txt", "w", encoding="UTF-8")
    customFileA.write("")

def addItemToFileList(item):
    customFileA = open("customList.txt", "a", encoding="UTF-8")
    customFileA.write(rtl(item) + "\n")
    customFileA.close()

def removeItemFromFileList(cat, sub, item):
    customFileR = open("customList.txt", "r", encoding="UTF-8")
    checkNum = 0
    while True:
        customFileR.seek(0,0)
        if len(customFileR.readlines())-1 <= checkNum:
            print("item doesn't exist!")
            customFileR.close()
            return
        customFileR.seek(0,0)
        if customFileR.readlines()[checkNum][:-1] == cat:
            customFileR.seek(0,0)
            if customFileR.readlines()[1+checkNum][:-1] == sub:
                customFileR.seek(0,0)
                if customFileR.readlines()[2+checkNum][:-1] == item:
                    print("item successfully removed!")
                    customFileR.seek(0,0)
                    tempList = customFileR.readlines()
                    customFileR.close()
                    tempList.pop(6+checkNum)
                    tempList.pop(5+checkNum)
                    tempList.pop(4+checkNum)
                    tempList.pop(3+checkNum)
                    tempList.pop(2+checkNum)
                    tempList.pop(1+checkNum)
                    tempList.pop(checkNum)
                    customFileW = open("customList.txt", "w", encoding="UTF-8")
                    for x in tempList:
                        customFileW.write(x)
                    customFileW.close()
                    return
        checkNum += 7

#updateListFromFileList()

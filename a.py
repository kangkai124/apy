#!/usr/bin/env python
#coding=utf-8

fristDict = {}
secondDict = {}

i= 0
with open("db_inac276_genom_1line.fasta") as secondFile:
  for line in secondFile:
    i += 1
    if (i % 2 == 0):
      continue
    lineList = line.split(' ')
    lastField = 'unmatched'
    key = lineList[0]
    if('plasmid' in lineList):
      index = lineList.index('plasmid') + 1
      lastField = lineList[index].replace(',', '').replace('\n', '')
    elif('plasmid:' in lineList):
      index = lineList.index('plasmid:') + 1
      lastField = lineList[index].replace(',', '').replace('\n', '')

    secondDict[key] = key + ' ' + lineList[1] + ' ' + lineList[2] + ' ' + lastField

j = 0
key = ''
with open("inac276_genom_repa.fasta") as firstFile:
  for line in firstFile:
    j += 1
    if (j % 2 == 0):
      fristDict[key] = line.replace('\r\n', '')
      continue
    key = line.replace('\r\n', '').replace('\n', '')

newFile = open('./output.log', 'w')

k = 0
with open("inac276_genom_repa.fasta") as file:
  for line in file:
    k += 1
    if (k % 2 == 0):
      continue
    key = line.replace('\r\n', '').replace('\n', '')
    print >> newFile, secondDict[key]
    print >> newFile, fristDict[key]

print ('转换完毕...')
newFile.close()
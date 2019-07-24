#!/usr/bin/env python
#coding=utf-8

dict = {}
dict2 = {}

lastKey = ''
i = 0
for line in open("db_inac276_genom_1line.fasta"):
  i= i + 1
  if (i % 2 == 0):
    continue

  x = line.split(' ')
  key = x[0]
  lastKey = key
  dict[key] = line

ii = 0
key = ''
for line in open("inac276_genom_repa.fasta"):
  ii = ii + 1
  if (ii % 2 == 0):
    if (ii != 0):
      dict2[key] = line.replace('\r\n', '')
    continue
  key = line.replace('\r\n', '').replace('\n', '')



newFile = open('./output.log', 'w+')

j = 0
for line in open("inac276_genom_repa.fasta"):
  j = j + 1
  if (j % 2 == 0):
    continue

  key = line.replace('\r\n', '').replace('\n', '')

  try:
    f = dict[key]
  except KeyError as e:
    continue
  
  fEle = f.split(' ')

  lastField = 'unmatched'

  if ('plasmid' in fEle):
    index = fEle.index('plasmid') + 1
    lastField = fEle[index].replace(',', '').replace('\n', '')
  
  if ('plasmid:' in fEle):
    index = fEle.index('plasmid:') + 1
    lastField = fEle[index].replace(',', '').replace('\n', '')

    
  newLine = key + ' ' + fEle[1] + ' ' + fEle[2] + ' ' + lastField
  print >> newFile, newLine
  print >> newFile, dict2[key]

print '转换完毕'
newFile.close()
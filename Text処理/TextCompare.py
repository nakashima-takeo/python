f_new = open('自払データ_2023年03月01日.txt', 'r', encoding='Shift_JIS')
f_old = open('jiharai.txt', 'r', encoding='Shift_JIS')
newData = f_new.readlines()
oldData = f_old.readlines()
f_new.close()
f_old.close()
fixData = ["ここからは名前が一致するが、金額が違うデータの一覧です。"]
for line in newData[:]:
  for line2 in oldData[:]:
    if line[43:80] == line2[43:80]:
      if line[80:90] == line2[80:90]:
        newData.remove(line)
        oldData.remove(line2)
        break
      else:
        fixData.append(line)
        fixData.append(line2)
        break
createF = open('diff.txt', 'w', encoding='Shift_JIS')
for line in newData:
  createF.write(line[:])
for line in oldData:
  createF.write(line[:])
for line in fixData:
  createF.write(line[:])
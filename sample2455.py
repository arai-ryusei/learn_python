#  例題ファイル：C:\pythonPG\sample2455.py

print()
set00 = {'s0', 's1', 's2'}
set11 = {'s0', 's3', 's4'}
print("初期　set00=", set00)
print("初期　set11=", set11);  print()

print("和=", set00|set11);  print()

print("積=", set00&set11);  print()

print("差set00-set11=", set00-set11);  print()

print("差set11-set00=", set11-set00);  print()

print("対称差=", set00 ^ set11);  print()

print("部分集合=", set00<=set11);  print()

print("部分集合{0,1,2},{0,1,2,3}=", {0,1,2}<={0,1,2,3})
print()


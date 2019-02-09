#  例題ファイル：C:\pythonPG\sample2425.py

print()
base_list = [ 11, 12, 13, 14, 15, 16, 17 ]
print("base_list=", base_list)
new_list = []
for element in base_list:
	if element % 2 == 0:
		new_element = element * 2
		new_list.append(new_element)
print("new_list1=", new_list)

print()
base_list = [ 11, 12, 13, 14, 15, 16, 17 ]
new_list = [element * 2  for  element in base_list  if  element % 2 == 0]
print("new_list2=", new_list)


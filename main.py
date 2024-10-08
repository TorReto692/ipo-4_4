strings = input("Введите список строк, разделенных пробелами: ").split() # ввод списка 
tripled_str = [s * 3 for s in strings] # цикл for
print(tripled_str) # вывод результата 
# 2. Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (пробелы важны!).
# Первая строка содержит следующее значение,
# а вторая строка содержит предыдущее значение введёного числа
# Please enter an integer number: 1234
#The next number for the number 1234 is 1235.
#The previous number for the number 1234 is 1233.
#or
# Please enter an integer number: 0
#The next number for the number 0 is 1.
#The previous number for the number 0 is -1.


num = input("Please enter an integer number: ")

print("the next number of the number " + num + " is " + str(int(num) + 1))
print("the previous number of the number " + num + " is " + str(int(num) - 1))


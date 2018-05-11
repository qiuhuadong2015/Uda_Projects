"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

# 用 set 记录电话
numbers = set()
for text in texts:
    incoming_number = text[0]
    answering_number = text[1]
    numbers.add(incoming_number)
    numbers.add(answering_number)
for call in calls:
    incoming_number = call[0]
    answering_number = call[1]
    numbers.add(incoming_number)
    numbers.add(answering_number)

numbers_count = "There are <count> different telephone numbers in the records."
numbers_count = numbers_count.replace("<count>", str(len(numbers)))
print(numbers_count)
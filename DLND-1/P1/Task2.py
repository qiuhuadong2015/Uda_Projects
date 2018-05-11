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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

'''
STEP 1：设计一个字典，key 是电话号码，value 是电话的通话总时长
STEP 2：遍历每条电话记录，将呼叫电话时长、被呼叫电话时长分别加入到字典对应电话的时长中
STEP 3：在字典中找出通话时长最长的电话和时长，并输出
'''

# STEP 1
during_count = dict()
# STEP 2
for call in calls:
    incoming_number = call[0]
    answering_number = call[1]
    during = int(call[3])
    if incoming_number not in during_count.keys():
        during_count[incoming_number] = during
    else:
        during_count[incoming_number] += during

    if answering_number not in during_count.keys():
        during_count[answering_number] = during
    else:
        during_count[answering_number] += during
# STEP 3
max_number = None
max_time = 0
for number in during_count.keys():
    time = int(during_count[number])
    if time > max_time:
        max_time = time
        max_number = number
max_description = "<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
max_description = max_description.replace("<telephone number>", str(max_number))
max_description = max_description.replace("<total time>", str(max_time))
print(max_description)
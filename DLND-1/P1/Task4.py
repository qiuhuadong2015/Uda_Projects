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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

'''
STEP 1：收集全部电话（不重复）
STEP 2：找非推销员，即发过短信或收过短信或收过来电的电话（不重复）
STEP 3：在全部电话中过滤非推销员，剩余的电话即可能推销员电话，进行输出
'''

# STEP 1
numbers = set()
for text in texts:
    numbers.add(text[0])
    numbers.add(text[1])
for call in calls:
    numbers.add(call[0])
    numbers.add(call[1])
# STEP 2
normal_numbers = set()
for text in texts:
    normal_numbers.add(text[0])
    normal_numbers.add(text[1])
for call in calls:
    normal_numbers.add(call[1])
# STEP 3
print("These numbers could be telemarketers: ")
telemarketer_numbers = list(filter(lambda item: item not in normal_numbers, numbers))
telemarketer_numbers.sort()
for telemarketer_number in telemarketer_numbers:
    print(telemarketer_number)
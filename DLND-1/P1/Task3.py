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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

'''
STEP 1：遍历每条电话记录，找到加罗尔地区呼出的记录
STEP 2：
 第一部分：收集被呼叫电话的区号或前缀
 第二部分：收集被呼叫电话和被呼叫电话为加罗尔地区的电话
STEP 3：
 第一部分：排序和输出
 第二部分：统计比例和输出
'''

# 用于第一部分
answering_codes = set()
# 用于第二部分
answering_numbers = set()
answering_080_numbers = set()

for call in calls:
    incoming_number = str(call[0])
    answering_number = str(call[1])
    # STEP 1
    if incoming_number.startswith("(080)"):
        # STEP 2
        # 第一部分
        if answering_number.startswith("140"):
            answering_codes.add("140")
        elif answering_number.startswith("(0"):
            end_index = answering_number.index(")") + 1
            answering_codes.add(answering_number[0:end_index])
        else:
            answering_codes.add(answering_number[0:4])
        # 第二部分
        answering_numbers.add(answering_number)
        if answering_number.startswith("(080)"):
                answering_080_numbers.add(answering_number)

# STEP 3
# 第一部分
answering_codes = list(answering_codes)
answering_codes.sort()
print("The numbers called by people in Bangalore have codes:")
for answering_code in answering_codes:
    print(answering_code)

# 第二部分
rate = len(answering_080_numbers) / len(answering_numbers)
rate_description = "<percentage> percent of calls from fixed lines in Bangalore are callsto other fixed lines in " \
                   "Bangalore. "
percentage = str(round(rate * 100, 2)) + "%"
rate_description = rate_description.replace("<percentage>", percentage)
print(rate_description)
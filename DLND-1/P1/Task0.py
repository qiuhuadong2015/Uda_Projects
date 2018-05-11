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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text_incoming_number = texts[0][0]
first_text_answering_number = texts[0][1]
first_text_time = texts[0][2]
first_text = "First record of texts, <incoming number> texts <answering number> at time <time>"
first_text = first_text.replace("<incoming number>", first_text_incoming_number)
first_text = first_text.replace("<answering number>", first_text_answering_number)
first_text = first_text.replace("<time>", first_text_time)
print(first_text)

last_call_incoming_number = calls[-1][0]
last_call_answering_number = calls[-1][1]
last_call_time = calls[-1][2]
last_call_during = calls[-1][3]
last_call = "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
last_call = last_call.replace("<incoming number>", last_call_incoming_number)
last_call = last_call.replace("<answering number>", last_call_answering_number)
last_call = last_call.replace("<time>", last_call_time)
last_call = last_call.replace("<during>", last_call_during)
print(last_call)
average_score = 0
student_number = 0
total_score = 0
highest_score = 0
lowest_score = 100
failed_number = 0
while True:
    str_score = input("请输入下一个学生的分数，回车表示输入结束>>>")
    if str_score == "":
        break
    int_score = int(str_score)
    student_number = student_number + 1
    total_score = total_score + int_score
    if int_score > highest_score:
        highest_score = int_score
    if int_score < lowest_score:
        lowest_score = int_score
    if int_score < 60:
        failed_number = failed_number + 1
average_score = total_score / student_number
print("平均分：%s" % average_score)
print("最高分：%s" % highest_score)
print("最低分：%s" % lowest_score)
print("不及格人数：%s" % failed_number)
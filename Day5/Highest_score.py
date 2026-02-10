student_scores =[150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum=0
for score in student_scores:
    sum+=score
print(sum)

max_number = max(student_scores) 
print(max_number)


max_scoreis =0
for score in student_scores:
    if score>max_scoreis:
        max_scoreis=score

print(max_scoreis)

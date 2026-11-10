# #===== STUDENT PERFORMANCE ANALYSIS SYSTEM =====

# import numpy as np

# marks=np.array([
#     [27,75,85,42,16],
#     [52,75,10,80,90],
#     [85,75,96,73,55],
#     [95,99,78,91,80],
#     [88,75,45,25,90],
#     [84,75,70,48,49],
#     [55,25,39,79,45],
#     [89,45,75,66,25],
#     [88,20,14,72,71],
#     [69,33,70,100,99]
# ])


# total_marks=np.sum(marks,axis=1)
# print("Total Marks of each students : ",total_marks)
# average_marks=np.mean(marks,axis=1)
# print("Average marks of each student : ",average_marks)

# average_subject=np.mean(marks,axis=0)
# print("Subject-wise average is : ",average_subject)

# topper=np.max(total_marks)
# print(f" The student with {topper} mark is the toppest among the students")

# low_mark=marks[marks<40]
# count=len(low_mark)
# print(f"{count} number of students have mark below 40 with marks {low_mark}")

# print("The class average is : ",np.mean(marks))
# print("The standard deviation is : ",np.std(marks))

# ranking=np.argsort(total_marks)
# rank=np.sort(total_marks)
# print(f"Ranking of students {ranking} based on their total marks {rank} ")

# passed_stds=np.where(np.all(marks>40,axis=1))[0]
# print("Students who passed all the subjects are : ",passed_stds+1)
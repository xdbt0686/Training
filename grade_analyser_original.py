'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
import csv

def calculate_classification(average_grade):
     if average_grade >= 70:
          return 1
     elif average_grade >= 60:
          return 2.1
     elif average_grade >= 50:
          return 2.2
     elif average_grade >= 40:
          return 3
     else:
          return "F"

def process_grade(filename):
     try:
          with open(filename,'r',newline='') as infile:
               reader = csv.reader(infile)
               student_data = list(reader)
          
          output_data = []
          for student in student_data:
               if not student:
                    continue
               student_id = student[0] 

               if not student_id.isdigit():
                    continue

               
               grades=[float(grade) for grade in student[1:] if grade.strip()]
               
               if not grades:
                    continue

               average_grade = sum(grades) / len(grades)

               classification = calculate_classification(average_grade)

               output_line = f"{student_id},{average_grade:.2f}_{classification}"
               output_data.append(output_line)
          output_filename = filename + "_out.csv"

          with open(output_filename,"w",newline='') as outfile:
               for line in output_data:
                    outfile.write(line+'\n')
          print(f"The file has been saved")
          return output_filename
     except FileNotFoundError:
          print("wrong")

def main():
     filename = input("\n please input the file's name").strip() 

     process_grade(filename)

if __name__ == "__main__":
     main()

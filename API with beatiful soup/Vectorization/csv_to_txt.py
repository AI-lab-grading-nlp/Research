import csv

csv_file = r'minerva_university_responses.csv'
txt_file = r'mu_responses_txt.txt'

with open(txt_file, "w", encoding="utf8") as my_output_file:
    with open(csv_file, "r", encoding="utf8") as my_input_file:
        [my_output_file.write(" ".join(row)+'\n') for row in csv.reader(x.replace('\0', '') for x in my_input_file)]
    my_output_file.close()

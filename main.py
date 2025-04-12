
import csv_to_gift

questions_csv_path = 'csv.csv'

raw_questions_list = csv_to_gift.read_csv(questions_csv_path, has_headers=False)

csv_to_gift.write_gift(raw_questions_list)
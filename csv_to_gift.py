
import csv

def read_csv(
    input_file_name:str, 
    has_headers:bool=True
    ) -> list:

    '''
    reads a given CSV file containing questions in the following format:
    question, answer_1, answer_2, answer_3, answer_4, answer_index[1-4]

    args:
        input_file_name(str)    : name for the input CSV
        has_headers(bool)       : if the CSV has headers

    returns:
        q_and_a_list(list)      : a list containing questions and answers
    
    '''

    # initializes a list that will be returned later including questions and answers
    q_and_a_list:list = None 
    
    # opens given csv, parses into a list then passes to q_and_a_list
    with open(input_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        q_and_a_list = list(reader)

    # returns list-ified csv - removes headers if present
    if has_headers is True:
        return q_and_a_list[1:]
    else:
        return q_and_a_list

def write_gift(
    q_and_a_list:list
    ):

    '''
    Writes questions in the GIFT format to a file for upload. Uses the
    question_formatter function to format questions before writting to
    the file.
    
    args:
        q_and_a_list(list): list of q's and a's to write to a gift file.

    '''
    
    # creates the file 'gift_output.gift'
    with open('gift_output.gift', 'w') as gift_output:
        for q_and_a in q_and_a_list:
            gift_output.write(question_formatter(q_and_a) + '\n')

def question_formatter(
    q_and_a:list
    ) -> str:
    
    '''
    Formats a list containing a question and answers. They MUST fit the 
    following format:

    question    : inxex 0
    answer 1    : index 1
    answer 2    : index 2
    answer 3    : index 3
    answer 4    : index 4
    correct ans : index 5

    args:
        q_and_a(list): list of answers and a question in the above format
    
    returns:
        as_gift(str): returns list passed in the args in the gift format

    '''
    
    # defines where to find the question and correct answer in the list
    QUESTION_INDEX  = 0
    ANSWER_INDEX    = 5

    # begins the return string in gift format - the question comes first
    as_gift:str = q_and_a[QUESTION_INDEX] + '{ '

    # appends answers to the above gift string. If the option index
    # matches the answer index, begins the option with '=', otherwise
    # it begins with '~'.

    for index, option in enumerate(q_and_a[1:-1]):
        
        if option != '':
            if index == int(q_and_a[ANSWER_INDEX])-1:
                as_gift += '=' + option + ' '
            else:
                as_gift += '~' + option + ' '
    
    # closes and returns the gift formatted string.
    return as_gift + '}'


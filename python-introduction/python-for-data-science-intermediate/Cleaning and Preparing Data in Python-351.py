## 1. Introducing Data Cleaning ##

# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows = len(moma)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
# str.replace(old, new)

age2 = age1.replace("one", "two")

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality
    gender = row[5]
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender

## 5. String Capitalization ##

for row in moma:
    # fix the capitalization and missing
    # values for the gender column
    gender = row[5]
    
    if not gender:
        gender = "Gender Unknown/Other"
    else:
        gender = gender.title()
        
    row[5] = gender

    # fix the capitalization and missing
    # values for the nationality column
    nationality = row[2]
    
    if not nationality:
        nationality = "Nationality Unknown"
    else:
        nationality = nationality.title()
        
    row[2] = nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begin_date = row[3]
    end_date = row[4]
    
    begin_date = clean_and_convert(begin_date)
    end_date = clean_and_convert(end_date)
    
    row[3] = begin_date
    row[4] = end_date
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    clean_string = string
    for bad_char in bad_chars:
        clean_string = clean_string.replace(bad_char, "")
    return clean_string

stripped_test_data = []

for date in test_data:
    clean_date = strip_characters(date)
    stripped_test_data.append(clean_date)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

# the date above
# some are a single year, some are ranges of years.
# When you encounter data like this, you need to make decisions on how you'll proceed.

def process_date(string):
    if "-" not in string:
        return int(string)
    else:
        date_split = string.split("-")
        date_one = int(date_split[0])
        date_two = int(date_split[1])
        date = round((date_one + date_two) / 2)
        return date  

processed_test_data = []

for data in stripped_test_data:
    processed_test_data.append(process_date(data))
    
for row in moma:
    date = row[6]
    date = process_date(strip_characters(date))
    row[6] = date
    
                               

                               
                              
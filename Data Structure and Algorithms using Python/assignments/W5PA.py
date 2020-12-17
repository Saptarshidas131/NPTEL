'''


For this assignment, you have to write a complete Python program.

    You may define additional auxiliary functions as needed.
    In all cases you may assume that the input to your program has the expected format, so your program does not have to check for malformed inputs.
    There are 2 public test cases and 6 (hidden) private test cases.
    "Compile and run" will evaluate your submission against the public test cases.
    "Submit" will evaluate your submission against the hidden private test cases and report a score on 100.
    Ignore warnings about "Presentation errors".

The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.

1.    Information about books
    Line format: Accession Number~Title

2.    Information about borrowers
    Line format: Username~Full Name

3.    Information about checkouts
    Line format: Username~Accession Number~Due Date
    Note: Due Date is in YYYY-MM-DD format.

You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one currently issued book in the following format:

Due Date~Full Name~Accession Number~Title

Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name. If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.

'''
# Dictionary to map accession number to title
books = {}
# Dictionary to map username to fullname
borrowers = {}
# List to store checkout data: accumulate, sort and print
checkouts = [] 

# Find the start of Books data
nextline = input().strip()
while nextline.find("Books") < 0:
    nextline = input().strip()

# Read upto start of Borrowers data
# Skip the line with "Books"
nextline = input().strip()
while nextline.find("Borrowers") < 0:
    (accession_number,title) = nextline.split('~')
    books[accession_number] = title
    nextline = input().strip()

# Read upto Checkout data
# Skip the line with "Borrowers"
nextline = input().strip()
while nextline.find("Checkouts") < 0:
    (username,fullname) = nextline.split('~')
    borrowers[username] = fullname
    nextline = input().strip()

# Process Checkouts
# Skip the line with "Checkouts"
nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    (username,accession_number,due_date) = nextline.split('~')
    checkoutline = due_date+"~"+borrowers[username]+"~"+accession_number+"~"+books[accession_number]
    checkouts.append(checkoutline)
    nextline = input().strip()

# Print the output from checkouts
for checkoutline in sorted(checkouts):
    print(checkoutline)



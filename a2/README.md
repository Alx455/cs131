This command allows the user to attach custom messages to
a given file or directory passed by command line parameters.
It stores the attached messages in a csv file, where the first
column is the file or directory name and the second column is
the attached message. When a the command is given a file which
already has an attached message, it prints out the message.

This is useful in the context of files or directories with 
undescriptive names(eg 0703). The user can attach messages to
these files or directories to help understand the purpose or
contents of it.

This command is simply used by running the command 'note' followed
by a file or directory name. The terminal then prompts the user to enter
the message to attach to that file. One entered, the file or directory
name is paired with the message in a csv file.

Example input:
./note test.txt
Enter note for test.txt:
This is a file that I created to test the note script
Note for test.txt has been added
[alejandrosu24@sjsu a2]$ ./note test.txt
Note for test.txt
This is a file that I created to test the note script
Would you like to overwrite the note for test.txt?
(y/n):
n

[alejandrosu24@sjsu a2]$ ./note 0703
Enter note for 0703:
Hello
Note for 0703 has been added
[alejandrosu24@sjsu a2]$ ./note 0703
Note for 0703
Hello
Would you like to overwrite the note for 0703?
(y/n):
y
Enter new note for 0703:
This is a directory for cs131 lecture of July 3, 2024. Today we presented out A2 projects
Note for 0703 has been updated
[alejandrosu24@sjsu a2]$ ./note 0703
Note for 0703
"This is a directory for cs131 lecture of July 3
Would you like to overwrite the note for 0703?
(y/n):
n


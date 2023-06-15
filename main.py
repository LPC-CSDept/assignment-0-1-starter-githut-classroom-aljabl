def main():
        print('Hello World')
        print('CS 7: Introduction to Computer Science')

    ##############################
    # make your code below
    # print('Hello World')
    ##############################


if __name__ == '__main__':
        main()

'''
ESSAY 

1. For this assignment I cloned the classroom repository, and completed the main.py by adding two print functions and defining the main() function. 
Lastly I tested the program using pytest and pytest -rP before executing stage/commit/set.

2. I learned how to stage/commit/push through terminal:

    STAGE: git add . (or name-of-file/doc instead of .)
    COMMIT: git commit -m “msg”
    PUSH: git push -u origin main

3.
    def main():
        #defines the function main(). running main() runs the two print functions.

        print('Hello World')
        print('CS 7: Introduction to Computer Science')
            #the print functions display the argument/data written in the quotes.

    if __name__ == '__main__':
        # __name__ is a special variable set by the python interpreter.
        # The __name__ variable is set to __main__ when file/module that's being run is the main program.
        # Otherwise, (if the file is being imported from a different file) __name__ is set to the file's name.
        # (EX. if the program in file-A imports file-B, __name__ will be set to __main__ for file-A and "file-B" for file-B)
        # In this context the __name__ variable is set to __main__ for the file main.py.

        main()
            #if the file being run is main.py, call the main() function.

4. I experienced an indentation error when I pushed my program to the GitHub Classroom repository, this was fixed by indenting "main()" under the "if"
 statement. I also experienced the credential issue mentioned on the slides.
 
 '''
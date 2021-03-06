# Computer_Assisted_Instruction

From: Java How to Program, Early Objects (10th Edition), Paul J. Deitel and Harvey Deitel, Pearson, 2015.

6.35. (Computer-Assisted Instruction) The use of computers in education is referred to as
computer-assisted instruction (CAI). Write a program that will help an elementary school
student learn multiplication. Use a SecureRandom object to produce two positive one-digit
integers. The program should then prompt the user with a question, such as
How much is 6 times 7?
The student then inputs the answer. Next, the program checks the student’s answer. If it’s
correct, display the message "Very good!" and ask another multiplication question. If the
answer is wrong, display the message "No. Please try again." and let the student try the same
question repeatedly until the student finally gets it right. A separate method should be used to
generate each new question. This method should be called once when the application begins
execution and each time the user answers the question correctly. (ComputerAssistedInstruction_1.py)

6.36. (Computer-Assisted Instruction: Reducing Student Fatigue) One problem in CAI
environments is student fatigue. This can be reduced by varying the computer’s responses to
hold the student’s attention. Modify the program of Exercise 6.35 so that various comments
are displayed for each answer as follows:
Possible responses to a correct answer:
Very good!
Excellent!
Nice work!
Keep up the good work!
Possible responses to an incorrect answer:
No. Please try again.
Wrong. Try once more.
Don't give up!
No. Keep trying.
Use random-number generation to choose a number from 1 to 4 that will be used to select one
of the four appropriate responses to each correct or incorrect answer. Use a switch statement
to issue the responses. (ComputerAssistedInstruction_2.py)

6.37. (Computer-Assisted Instruction: Monitoring Student Performance) More
sophisticated computer-assisted instruction systems monitor the student’s performance over a
period of time. The decision to begin a new topic is often based on the student’s success with
previous topics. Modify the program of Exercise 6.36 to count the number of correct and
incorrect responses typed by the student. After the student types 10 answers, your program
should calculate the percentage that are correct. If the percentage is lower than 75%, display
"Please ask your teacher for extra help.", then reset the program so another student can try it.
If the percentage is 75% or higher, display "Congratulations, you are ready to go to the next
level!", then reset the program so another student can try it. (ComputerAssistedInstruction_3.py)

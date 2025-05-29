# Practical Exercises about Abstract Data Types (ADTs)

Below are practical exercises to help you understand how to define Abstract Data Types can be used to model real-world data for processing by a program. For each exercise, think about how to represent the data and provide an implementation of this representation. In many cases it is valuable to think about alternative representations and when it is more convenient to use certain representation.

**VERY IMPORTANT**: Make sure your ADT implementations are *well-structured*, *encapsulated*, and provide *clear interfaces* for interaction. Use Python classes to implement the ADTs.


## ADT for a Book

**Task**:
Define an ADT for a Book that stores the title, author, and year of publication.

Implement the ADT using a Python class.
Define and implement accessor and mutator methods for each field.
Write a function to print a book’s details.

## ADT for a Bank Account

**Task**:
Define an ADT for a BankAccount with operations: deposit, withdraw, get_balance, and transfer_to(other_account, amount).

Implement the ADT.
Write a test program that creates two accounts and performs several operations.

## ADT for a Polynomial

**Task**:
Design an ADT for a mathematical polynomial (e.g., $3x² + 2x + 1$).

Implement the ADT so it can add, subtract, and evaluate polynomials.
Consider different internal representations (list of coefficients, list of terms, etc.) and discuss their pros and cons.

Implement *unit tests* to make sure the polynomial operations work correctly.
Implement [Ruffini’s Rule](https://algebrica.org/ruffinis-rule/) for synthetic division of polynomials.

## ADT for Doctor Appointments

**Task**:
Create an ADT for a DoctorAppoinment that includes the the patient (a Person ADT), the starting and ending times of the appointment, and the doctor (another Person ADT).

Implement accessor and mutator methods for each field.
Implement a method to check if the appointment overlaps with another appointment.
Write a function to print a daily schedule given a list of appointments.

## Extension

For each exercise:

- Write a short explanation of why their design is a good abstraction.
- Discuss alternative representations and when they might be preferable.

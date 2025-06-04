# Practical Exercises about Abstract Data Types (ADTs)

Below are practical exercises to help you understand how to define Abstract Data Types (ADTs) to model real-world data for processing by a program. These exercises do not include collections like Queues, Stacks, or Bags, but focus on ADTs representing entities and concepts.

**VERY IMPORTANT**: Make sure your ADT implementations are *well-structured*, *encapsulated*, and provide *clear interfaces* for interaction. Use Python classes to implement the ADTs.

## ADT for a Book

**Task**:
Define an ADT for a Book that stores the title, author, and year of publication.

- Implement the ADT using a Python class.
- Define and implement accessor and mutator methods for each field.
- Write a function to print a book’s details.

## ADT for a Bank Account

**Task**:
Define an ADT for a BankAccount with operations: deposit, withdraw, get_balance, and transfer_to(other_account, amount).

- Implement the ADT.
- Write a test program that creates two accounts and performs several operations.

## ADT for a Polynomial

**Task**:
Design an ADT for a mathematical polynomial (e.g., $3x^2 + 2x + 1$).

- Implement the ADT so it can add, subtract, and evaluate polynomials.
- Consider different internal representations (list of coefficients, list of terms, etc.) and discuss their pros and cons.
- Implement *unit tests* to make sure the polynomial operations work correctly.
- Implement [Ruffini’s Rule](https://algebrica.org/ruffinis-rule/) for synthetic division of polynomials.

## ADT for Doctor Appointments

**Task**:
Create an ADT for a DoctorAppointment that includes the patient (a Person ADT), the starting and ending times of the appointment, and the doctor (another Person ADT).

- Implement accessor and mutator methods for each field.
- Implement a method to check if the appointment overlaps with another appointment.
- Write a function to print a daily schedule given a list of appointments.

## Extension

For each exercise:

- Write a short explanation of why the design is a good abstraction.
- Discuss alternative representations and when they might be preferable.

## Exercises on Designing APIs

These exercises require you to think carefully about the API design of the ADT. The API is not given; you must decide what methods and operations make sense.

### ADT for a Library Catalog

**Task**:
Design an ADT for a LibraryCatalog that manages a collection of books.

- Decide what operations the catalog should support (e.g., add_book, etc.).
- Consider how to handle multiple copies of the same book.
- Think about how to represent the catalog internally.
- Implement the ADT with your chosen API.
- Write example usage demonstrating your API.

### ADT for a Social Network User

**Task**:
Design an ADT for a SocialNetworkUser.

- Consider what attributes and operations are needed (e.g., add_friend, etc.).
- Think about privacy settings and how they might affect the API.
- Implement the ADT with your chosen API.
- Write tests or example code showing how your API works.

### ADT for a Task Scheduler

**Task**:
Design an ADT for a TaskScheduler that manages tasks with priorities and deadlines.

- Decide on the operations (e.g., add_task, remove_task, get_next_task).
- Consider how to handle task priorities and deadlines in the API.
- Implement the ADT.
- Provide example usage.

### ADT for a Shopping Cart

**Task**:
Design an ADT for a ShoppingCart.

- Decide what operations are needed (e.g., add_item, get_total_price, etc.).
- Consider how to handle quantities and discounts.
- Implement the ADT.
- Write example usage demonstrating your API.

For these exercises, focus on designing clear, intuitive, and useful APIs that encapsulate the data and operations well.

## Adding Simple Unit Tests

For each exercise above, add a simple set of unit tests in the `if __name__ == "__main__":` block of your program. These tests should:

- Create instances of your ADT.
- Call the main operations with sample data.
- Use assertions to verify correctness.

This will help ensure your ADT operations work as expected and provide example usage for others.

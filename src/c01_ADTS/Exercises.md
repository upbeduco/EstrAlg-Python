# Practical Exercises about Abstract Data Types (ADTs)

Below are practical exercises to help you understand how to define Abstract Data Types (ADTs) to model real-world data for processing by a program. These exercises do not include collections like Queues, Stacks, or Bags, but focus on ADTs representing entities and concepts.

**VERY IMPORTANT**: Make sure your ADT implementations are *well-structured*, *encapsulated*, and provide *clear interfaces* for interaction. Use Python classes to implement the ADTs.
Additionally, for most ADTs, it is good practice to implement:
-   `__str__`: To provide a user-friendly string representation of the object.
-   `__eq__`: To define what it means for two instances of the ADT to be considered equal.

## ADT for a Book

**Task**:
Define an ADT for a Book that stores the title, author, and year of publication.

-   Implement the ADT using a Python class.
-   Define and implement accessor and mutator methods for each field.
-   Implement `__str__` to provide a user-friendly string representation (e.g., "Title by Author (Year)").
-   Implement `__eq__` to compare two Book instances based on their title and author.
-   Write a function to print a book’s details.

## ADT for a Bank Account

**Task**:
Define an ADT for a BankAccount with operations: deposit, withdraw, get_balance, and transfer_to(other_account, amount).

-   Implement the ADT.
-   Ensure `withdraw` and `transfer_to` methods handle cases of insufficient funds gracefully (e.g., by raising an error or returning `False`).
-   Implement `__str__` to show account details (e.g., "Account #XXXXX, Balance: $Y.YY").
-   Write a test program that creates two accounts and performs several operations.

## ADT for a Polynomial

**Task**:
Design an ADT for a mathematical polynomial (e.g., $3x^2 + 2x + 1$).

-   Implement the ADT so it can add, subtract, and evaluate polynomials.
-   Consider different internal representations (list of coefficients, list of terms, etc.) and discuss their pros and cons.
-   Implement `__str__` to represent the polynomial in a readable format.
-   Implement `__eq__` to compare two polynomial instances.
-   Implement *unit tests* to make sure the polynomial operations work correctly.
-   Implement [Ruffini’s Rule](https://algebrica.org/ruffinis-rule/) for synthetic division of polynomials.

## ADT for Doctor Appointments

**Task**:
Create an ADT for a DoctorAppointment that includes the patient (a Person ADT), the starting and ending times of the appointment, and the doctor (another Person ADT).

-   Implement accessor and mutator methods for each field.
-   Implement a method to check if the appointment overlaps with another appointment.
-   Implement `__str__` for a clear representation of the appointment.
-   Implement `__eq__` to compare two appointments.
-   Write a function to print a daily schedule given a list of appointments.

## Extension

For each exercise:

-   Write a short explanation of why the design is a good abstraction.
-   Discuss alternative representations and when they might be preferable.

## Exercises on Designing APIs

These exercises require you to think carefully about the API design of the ADT. The API is not given; you must decide what methods and operations make sense.

### ADT for a Library Catalog

**Task**:
Design an ADT for a LibraryCatalog that manages a collection of books.

-   Decide what operations the catalog should support (e.g., add_book, remove_book, find_book_by_title, list_all_books, etc.).
-   Consider how to handle multiple copies of the same book.
-   Think about how to represent the catalog internally.
-   Implement the ADT with your chosen API.
-   Write example usage demonstrating your API.

### ADT for a Social Network User

**Task**:
Design an ADT for a SocialNetworkUser.

-   Consider what attributes and operations are needed (e.g., add_friend, remove_friend, post_message, get_friends_list, etc.).
-   Think about privacy settings and how they might affect the API.
-   Implement the ADT with your chosen API.
-   Write tests or example code showing how your API works.

### ADT for a Task Scheduler

**Task**:
Design an ADT for a TaskScheduler that manages tasks with priorities and deadlines.

-   Decide on the operations (e.g., add_task, remove_task, get_next_task, mark_task_complete).
-   Consider how to handle task priorities and deadlines in the API.
-   Implement the ADT.
-   Provide example usage.

### ADT for a Shopping Cart

**Task**:
Design an ADT for a ShoppingCart.

-   Decide what operations are needed (e.g., add_item, remove_item, update_quantity, get_total_price, apply_discount, checkout).
-   Consider how to handle quantities and discounts.
-   Implement the ADT.
-   Write example usage demonstrating your API.

For these exercises, focus on designing clear, intuitive, and useful APIs that encapsulate the data and operations well.

## Adding Simple Unit Tests

For each exercise above, add a simple set of unit tests in the `if __name__ == "__main__":` block of your program. These tests should:

-   Create instances of your ADT.
-   Call the main operations with sample data.
-   Use assertions to verify correctness.

This will help ensure your ADT operations work as expected and provide example usage for others.

## Further Exploration of ADT Design

### ADT for a Playing Card

**Task**:
Define an ADT for a standard playing card (e.g., "Ace of Spades").

-   Implement the ADT using a Python class.
-   Implement `__str__` for a clear representation (e.g., "King of Hearts").
-   Implement `__eq__` to compare two cards (e.g., same rank and suit).
-   Implement rich comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`) to allow sorting cards (e.g., by rank, then by suit).
-   Discuss if this ADT should be mutable or immutable and justify your choice.

### ADT for a Geometric Vector (2D or 3D)

**Task**:
Define an ADT for a 2D or 3D vector.

-   Implement vector addition (`__add__`), subtraction (`__sub__`), and scalar multiplication (`__mul__`).
-   Implement methods for calculating the magnitude (`__abs__`) and the dot product.
-   Implement `__str__` for a readable vector representation (e.g., "<3, 4>").
-   Implement `__eq__` to compare two vectors.
-   Discuss the choice of internal representation (e.g., list, tuple, separate attributes) and its implications.

### Immutability vs. Mutability

**Discussion Point**:
Explain the concepts of immutable and mutable ADTs. Discuss when it is appropriate to design an ADT as immutable (its state cannot change after creation) versus mutable (its state can be modified).

**Task**:
Identify which of the previously implemented ADTs are naturally immutable (e.g., Book, Playing Card, Point) and which are mutable (e.g., BankAccount, ShoppingCart). Discuss the implications of this choice on their design and usage.

### Data Validation and Robustness

**Discussion Point**:
Emphasize the importance of validating input data in constructors and methods to maintain ADT integrity and prevent invalid states.

**Task**:
Review one of your implemented ADTs (e.g., `Date` or `Fecha` from `src/c01_ADTS/fecha.py` or `src/c01_ADTS/FechaDataclass.py`) and add robust validation for all input parameters (e.g., year within a reasonable range, month between 1-12, day valid for the given month and year, handling leap years). Ensure that invalid inputs raise appropriate exceptions (e.g., `ValueError`).

### Hashing (`__hash__`)

**Discussion Point**:
Briefly explain when and why the `__hash__` method is needed in Python (e.g., for using ADT instances as keys in dictionaries or elements in sets). Explain the relationship between `__eq__` and `__hash__`.

**Task**:
For an immutable ADT you have implemented (e.g., `Book` or `Playing Card`), implement the `__hash__` method so that instances of your ADT can be used in hash-based collections like `dict` and `set`. Write a small test to demonstrate this functionality.

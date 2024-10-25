# IS601 MIDTERM - ADVANCED PYTHON CALCULATOR
An advanced python calculator has been developed in this project which satifies all the requirements like advanced design patterns, maintainable code, logging,  dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Video Presentation link [click here]

## Follow these steps for the succesful execution of the code:

## Step 1: Clone this repository

Clone this particular repository by using the following command:
git clone https://github.com/rithika955/Midterm

## Step 2: Install all the required libraries in the requirements.txt file by using the following command:

pip install -r requirements.txt

## Step 3: In the .env file in the repository(which is empty), add the following environment variable and it's value:

CALC_FILE_PATH='./data/calculator_history.csv'

## Step 4: Start the application:

To start the application, type the following command in the terminal:
python3 main.py

## Step 5: Give data and check the running of application:

You can choose any of the options displayed and give data accordingly for a particular operation and see the results getting displayed and also stored in the csv file in the data folder.

The menu functions has all the options or functionalities the app has to offer,[Click here](https://github.com/rithika955/Midterm/tree/master/app/plugins)

You can use the following commands within the REPL command interface:

1. Add: to add two numbers
2. Subtract: to subtract two numbers
3. Multiply: to multiply two numbers
4. Divide: to divide one number by another
5. Load: shows history of the actions performed
6. Clear: Clears the history
7. Delete: deletes a particular record when it's ID is given
8. Menu: options are displayed
9. Exit: Exit the application

To check the codes for all these plugins, [click here](https://github.com/rithika955/Midterm/tree/master/app/plugins)

## Arithmetic Operations:

### 1.Add: for addition 
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/add/__init__.py)

### 2. Subtract: for subtraction
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/subtract/__init__.py)

### 3. Multiply: for multiplication
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/multiply/__init__.py)

### 4. Divide: for division
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/divide/__init__.py)

## Managing History:

### 1. Load: loads the history of the calculator
It displays complete history of the operations performed which are stored in the calculation_history.csv file.
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/load/__init__.py)

History looks like this:

ID,action,arg1,arg2
1,divide,3.0,4.0
2,subtract,6.0,4.0
3,add,4.0,5.0
4,subtract,6.0,5.0
5,add,3.0,4.0
6,subtract,7.0,6.0
7,multiply,10.0,76.0
8,divide,9.0,6.0

### 2. Delete: deletes a particular record when the Id is given
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/delete/__init__.py)

For example, let us delete the record with ID=4
Now, the history looks like this:

ID,action,arg1,arg2
1,divide,3.0,4.0
2,subtract,6.0,4.0
3,add,4.0,5.0
4,add,3.0,4.0
5,subtract,7.0,6.0
6,multiply,10.0,76.0
7,divide,9.0,6.0

### 3. clear: this command clears the entire history stoed in the calculator_history.csv file
[Click here] (https://github.com/rithika955/Midterm/tree/master/app/plugins/clear/__init__.py)

## Design of the application:
1. 'Command pattern': The command pattern is best illustrated by the `execute` method in the command handling code. Every command, including `add`, `subtract`, and so on, is represented as an object that contains the action that needs to be performed. By encouraging decoupling between the executor (such as calculating logic) and the invoker (such as user input), this design improves modularity and flexibility. [Click here] (https://github.com/rithika955/Midterm/blob/master/app/commands/__init__.py)
2. 'Facade pattern': With the help of pandas, the `History` class serves as a platform, providing a simplified method for managing CSV data. With features like `writing_the_data`, `get_as_list`, `get_as_dataframe`, and `clear`, it offers an easy-to-use interface that protects users from the complexities of file management and pandas. By removing the complexity of data management, this abstraction enables users to manipulate CSV data with ease. [Click here] (https://github.com/rithika955/Midterm/tree/master/app/history/__init__.py)
3. 'Singleton pattern': As a singleton instance, the `MenuCommand` class makes sure that only one instance is made for the course of the application's lifecycle. The 'MenuCommand' class implementation in the "app.plugins.menu" module exemplifies the singleton approach. This guarantees consistent behavior throughout the program and encourages resource efficiency. [Click here] (https://github.com/rithika955/Midterm/tree/master/app/__init__.py)

## Logging: 

To provide thorough monitoring and efficient troubleshooting, the program uses Python's logging module to implement a strong logging mechanism:

1. **Configuration and Initialization**:

At the beginning of the application, typically in the main module or entry point, the logging setup is coordinated. This configuration includes setting up settings such as the output destination (e.g., file, console), format, and logging level. To improve maintainability and flexibility, configuration settings are centralized and streamlined using a special logging configuration file (`logging.conf`).
(https://github.com/rithika955/Midterm/tree/master/logging.conf) [click here]

2. **Categorization of Use and Messages**:

Logging is carefully incorporated into the application's codebase to record a variety of messages, such as warning, error, and informational messages. In order to facilitate effective triaging and prioritizing during troubleshooting efforts, each log message is meticulously categorized according to its severity and significance.

Example of logging:

2024-10-24 23:11:31,727 - root - INFO - Logging configured.
2024-10-24 23:11:31,766 - root - INFO - Environment variables loaded.
2024-10-24 23:11:50,000 - root - INFO - Command 'add' from plugin 'add' registered.
2024-10-24 23:11:50,012 - root - INFO - Command 'clear' from plugin 'clear' registered.
2024-10-24 23:11:50,014 - root - INFO - Command 'delete' from plugin 'delete' registered.
2024-10-24 23:11:50,018 - root - INFO - Command 'divide' from plugin 'divide' registered.
2024-10-24 23:11:50,021 - root - INFO - Command 'load' from plugin 'load' registered.
2024-10-24 23:11:50,022 - root - INFO - Command 'menu' from plugin 'menu' registered.
2024-10-24 23:11:50,026 - root - INFO - Command 'multiply' from plugin 'multiply' registered.
2024-10-24 23:11:50,034 - root - INFO - Command 'subtract' from plugin 'subtract' registered.
2024-10-24 23:11:50,034 - root - INFO - Application started. Type 'exit' to exit.
2024-10-24 23:12:37,109 - root - INFO - addition of 3.0 and 4.0 = 7.0
2024-10-24 23:12:37,143 - root - INFO - The Addition operation was performed successfully
2024-10-24 23:12:46,877 - root - INFO - Subtraction of 7.0 and 6.0 = 1.0
2024-10-24 23:12:46,877 - root - INFO - The Subtract operation was performed successfully
2024-10-24 23:12:56,012 - root - INFO - Multiplication of 10.0 and 76.0 = 760.0
2024-10-24 23:12:56,014 - root - INFO - The Multiplication operation was performed successfully
2024-10-24 23:13:09,398 - root - INFO - division of 9.0 and 6.0 = 1.5
2024-10-24 23:13:09,399 - root - INFO - The Division operation was performed successfully
2024-10-24 23:15:01,470 - root - INFO - History of the record with ID 4 has been deleted.

3. **Reporting errors and handling exceptions**:
Strong error-handling techniques, exemplified by try/except blocks, are thoughtfully incorporated into important codebase parts such as file operations and computing activities. In order to provide thorough error coverage, these procedures are regularly used in modules like subtract, add, multiply, and divide. In the event of an occurrence, thorough error messages are recorded to give developers context-specific information about the fault's context and underlying cause, enabling quick problem identification and fixing.
[Click here](https://github.com/rithika955/Midterm/tree/master/app/plugins/subtract/__init__.py)

By using this logging technique, the application strengthens its dependability and maintainability in a variety of operational circumstances by guaranteeing transparency, traceability, and resilience throughout its operational lifecycle.

## EAFP (Easier to Ask for Forgiveness than Permission)

**Achievement**: Explore the implementation of the `divide` plugin, where possible 'ZeroDivisionError' exceptions are handled gently via the try/except method. This method promotes readability and clarity in the code while guaranteeing strong error management, which is in line with Pythonic principles.

(https://github.com/rithika955/Midterm/tree/master/app/plugins/divide/__init__.py) [click here]

In addition to improving the application's dependability, this unique approach to design patterns, logging plans, and error-handling procedures raises the bar for the user experience as a whole.













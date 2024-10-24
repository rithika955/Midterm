import logging
from app.commands import Command
from app.history import History

class SubtractCommand(Command):
    def execute(self):
        try:
            hist_inst = History()
            input1 = float(input("Enter the first number: "))
            input2 = float(input("Enter the second number: "))
            result = input1 - input2
            print('The result of the operations is', result)
            logging.info(f'Subtraction of {input1} and {input2} = {input1 - input2}')
            logging.info('The Subtract operation was performed successfully')
            data = ['subtract', input1, input2]
            existing_data = hist_inst.get_as_list()
            existing_data.append(data)
            hist_inst.writing_the_data(existing_data)

        except ValueError as e:
                print("Please enter a valid number!")
                logging.info('The Subtraction operation failed')
         
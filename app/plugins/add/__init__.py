import logging
from app.commands import Command
from app.history import History


class AddCommand(Command):
    def execute(self):
        try:
            #hist_inst = History()
            input1 = float(input("Please enter the first number: "))
            input2 = float(input("Please enter the second number: "))
            result = input1 + input2
            print('The result of the operations is', result)
            logging.info(f'addition of {input1} and {input2} = {input1 + input2}')
            logging.info('Addition operation successfully performed')
            data = ['add', input1, input2]
            #existing_data = hist_inst.get_as_list()
            #existing_data.append(data)
            #hist_inst.writing_the_data(existing_data)

        except ValueError:
                print("Please enter a valid number!")
                logging.info('The Addition operation failed')

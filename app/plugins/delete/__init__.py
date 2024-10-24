import sys
from app.commands import Command
from app.history import History
import logging


class DeleteCommand(Command):
    def execute(self):
        hist_inst = History()
        existing_data = hist_inst.get_as_data_frame()
        record_id = int(input('Enter the ID of the record to delete: '))
        updated_data = existing_data[existing_data['ID'] != record_id]
        logging.info(f'History of the record with ID {record_id} has been deleted.')
        hist_inst.writing_the_data(updated_data.values.tolist())
        print('Data history of calculator after deletion:\n', hist_inst.get_as_data_frame().to_string(index=False))

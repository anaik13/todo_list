import pandas as pd

def load_notes(self):
    df = pd.read_csv(self.dir + 'notes.csv', index_col=0)
    return df

def ask_about_note_update():
    updated_note = dict()
    updated_note['updated_note'] = input('Write updated note:')
    updated_note['updated_note_date'] = input('Write updated note date:')
    updated_note['updated_note_importance'] = input('Write updated note importance:')
    updated_note['updated_note_status'] = input('Write updated note status:')
    updated_note['updated_note_place'] = None
    return updated_note
    logger.info('Log fro, auxiliary_functions.py')


def which_note(self):
    df = self.load_notes()
    print(df)
    idx_to_update = int(input('Specify which note (look at idx column):'))
    return idx_to_update


def which_col_to_update():
    col_to_update = input('Specify which column to update (Options: status, importance):')
    return col_to_update


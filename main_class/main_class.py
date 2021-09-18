import pandas as pd
import datetime
from main_class import auxiliary_functions as af
from main_class import auxiliary_functions_event as afe
from logs import logs as l


class Action():

    def __init__(self):
        dir = r'C:\Users\anaik\Desktop\Praca_2021\BitPeak\practise_python_1\todo_list\\'
        self.dir = dir

    @l.add_action_status
    def write_notes(self, df):
        df.to_csv(self.dir + 'notes.csv')


    @l.add_action_status
    def show_all_notes(self):
        df = self.load_notes()
        print(df)


    def create_new_note(self):
        new_note = input('Write new note:')
        new_note_date = input('Write date of new note:')
        new_note_importance = input('Write importance of new note:')
        new_note_df = pd.DataFrame([[new_note, new_note_date, new_note_importance]], columns=['note', 'date', 'importance'])
        new_note_df['added_date'] = datetime.datetime.now()
        new_note_df['date'] = new_note_date if new_note_date != '' else None
        new_note_df['status'] = 'To do'
        new_note_df['place'] = None
        new_note_df = new_note_df[['added_date', 'date', 'note', 'importance', 'status', 'place']]
        return new_note_df


    @l.add_action_status
    def save_new_note(self):
        df = self.load_notes()
        new_note_df = self.create_new_note()
        df = df.append(new_note_df)
        df['idx'] = range(1, len(df)+1)
        df = df.set_index('idx')
        self.write_notes(df)
        print('------- New note saved. -------')


    @l.add_action_status
    def delete_note(self):
        df = self.load_notes()
        print(df)
        idx_to_delete = int(input('Specify which note to delete (look at idx column):'))
        df = df.drop(index=idx_to_delete)
        self.write_notes(df)
        print('------- Specified note was removed. -------')


    @l.add_action_status
    def delete_all_notes(self):
        self.write_notes(pd.DataFrame(columns=['added_date', 'date', 'note', 'importance', 'status', 'place']))
        print('------- There are NO saved notes. -------')


    @l.add_action_status
    def update_note(self):

        idx_to_update = self.which_note()
        updated_note = self.ask_about_note_update()

        df = self.load_notes()
        df.loc[idx_to_update, :] = [df.loc[idx_to_update, 'added_date'],
                             updated_note['updated_note_date'] if updated_note['updated_note_date']
                                                                else df.loc[idx_to_update, 'date'],
                             updated_note['updated_note'] if updated_note['updated_note']
                                                            else df.loc[idx_to_update, 'note'],
                             updated_note['updated_note_importance'] if updated_note['updated_note_importance']
                                                                        else df.loc[idx_to_update, 'importance'],
                             updated_note['updated_note_status'] if updated_note['updated_note_status']
                                                                    else df.loc[idx_to_update, 'status'],
                             updated_note['updated_note_place'] if updated_note['updated_note_place']
                                                                    else df.loc[idx_to_update, 'place']
                            ]
        self.write_notes(df)


    @l.add_action_status
    def update_field(self):

        idx_to_update = self.which_note()
        col_to_update = self.which_col_to_update()

        df = self.load_notes()

        val_to_update = input('For what {}:'.format(col_to_update))
        df.loc[idx_to_update, col_to_update] = val_to_update
        self.write_notes(df)


    # Auxiliary functions


    def load_notes(self):
        return af.load_notes(self)


    def ask_about_note_update(self):
        return af.ask_about_note_update()


    def which_note(self):
        return af.which_note(self)


    def which_col_to_update(self):
        return af.which_col_to_update()



class Event(Action):

    def create_new_note(self):
        new_note_df = super().create_new_note()
        new_note_place = input('Write place of new note:')
        new_note_df['place'] = new_note_place
        return new_note_df


    # Auxiliary functions

    def ask_about_note_update(self):
        return afe.ask_about_note_update()


    def which_col_to_update(self):
        return afe.which_col_to_update()


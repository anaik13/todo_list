def ask_about_note_update():
    updated_note = dict()
    updated_note['updated_note'] = input('Write updated note:')
    updated_note['updated_note_date'] = input('Write updated note date:')
    updated_note['updated_note_importance'] = input('Write updated note importance:')
    updated_note['updated_note_status'] = input('Write updated note status:')
    updated_note['updated_note_place'] = input('Write updated note place:')
    return updated_note

def which_col_to_update():
    col_to_update = input('Specify which column to update (Options: status, importance, place):')
    return col_to_update
from main_class import main_class as mc


note = mc.Action()
event = mc.Event()




while True:

    next_action = input('What do you want to do [Options: list, add, remove, remove all, update, update all fields] :')

    if next_action == 'l':
        note.show_all_notes()

    elif next_action == 'a':
        action_kind = input('What kind of action do you want to add [Options: event, others]?')
        if action_kind == 'e':
            event.save_new_note(action_kind)
        elif action_kind == 'o':
            note.save_new_note(action_kind)

    elif next_action == 'r':
        note.delete_note()

    elif next_action == 'ra':
        note.delete_all_notes()

    elif next_action == 'u':
        action_kind = input('What kind of action do you want to update [Options: event, others]?')
        if action_kind == 'e':
            event.update_field(action_kind)
        elif action_kind == 'o':
            note.update_field(action_kind)
        else:
            print('You specified uncorrect kind of action.')


    elif next_action == 'ua':
        action_kind = input('What kind of action do you want to update [Options: event, others]?')
        if action_kind == 'e':
            event.update_note(action_kind)
        elif action_kind == 'o':
            note.update_note(action_kind)
        else:
            print('You specified uncorrect kind of action.')

    if_continue = input('Do you want to continue [Options: y, n]:')
    if not if_continue == 'y':
        break




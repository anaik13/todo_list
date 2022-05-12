from main_class import main_class as mc


note = mc.Action()
event = mc.Event()

while True:

    next_action = input('What do you want to do [Options: list (l), add (a), remove (r), remove all (ra), update (u), update all fields (ua)] :')

    if next_action == 'l':
        note.show_all_notes()

    elif next_action == 'a':
        action_kind = input('What kind of action do you want to add [Options: event (e), others (o)]?')
        if action_kind == 'e':
            event.save_new_note(action_kind)
        elif action_kind == 'o':
            note.save_new_note(action_kind)

    elif next_action == 'r':
        note.delete_note()

    elif next_action == 'ra':
        note.delete_all_notes()

    elif next_action == 'u':
        action_kind = input('What kind of action do you want to update [Options: event (e), others (o)]?')
        if action_kind == 'e':
            event.update_field(action_kind)
        elif action_kind == 'o':
            note.update_field(action_kind)
        else:
            print('You specified incorrect kind of action.')

    elif next_action == 'ua':
        action_kind = input('What kind of action do you want to update [Options: event (e), others (o)]?')
        if action_kind == 'e':
            event.update_note(action_kind)
        elif action_kind == 'o':
            note.update_note(action_kind)
        else:
            print('You specified incorrect kind of action.')

    while True:
        if_continue = input('Do you want to continue [Options: y, n]:')
        if if_continue == 'y':
            break
        elif if_continue == 'n':
            exit()
        else:
            print('You specified incorrect kind of action.')

define a = Character("Admin")

label start:
    $ DEBUG = False
    if DEBUG:
        # Debug mode
        # Jump to debug this label
        jump end_story

    # Production mode
    jump play_or_learn

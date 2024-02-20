define a = Character("Admin")

label start:
    $ DEBUG = True
    if DEBUG:
        # Debug mode
        # Jump to debug this label
        jump play_or_learn

    # Production mode
    jump play_or_learn

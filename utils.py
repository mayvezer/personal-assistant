import difflib

def get_suggestion(user_input, commands):
    matches = difflib.get_close_matches(user_input, commands, n=1, cutoff=0.4)
    return matches[0] if matches else None
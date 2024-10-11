def mood_response(mood):
    if mood.lower() == "happy":
        print("Terrific! I hope the day is a good one.")
    elif mood.lower() == "sad":
        print("That's too bad. I hope the day improves and you feel better.")
    elif mood.lower() == "tired":
        print("I hope you can rest well tonight.")
    elif mood.lower() == "excited":
        print("I can't wait to see what happens today.")
    else:
        return "Tomorrow is another day"
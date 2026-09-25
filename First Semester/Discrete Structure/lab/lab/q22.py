def finite_automata(string):
    state = "q0"

    for symbol in string:
        if state == "q0":
            if symbol == "a":
                state = "q1"
            else:
                state = "dead"

        elif state == "q1":
            if symbol == "b":
                state = "q2"
            else:
                state = "dead"

        elif state == "q2":
            if symbol == "b":
                state = "q3"
            else:
                state = "dead"

        elif state == "q3":
            state = "dead"

        else:
            state = "dead"

    if state == "q2" or state == "q3":
        return True
    else:
        return False


string = input("Enter a string: ")

if finite_automata(string):
    print("Accepted")
else:
    print("Rejected")
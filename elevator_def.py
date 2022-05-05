def elevator_call(elevator_state, call_floor):
    counter = elevator_state
    while counter <= call_floor and customers > 0:
        print("floor number_", counter)
        counter += 1
    elevator_state = counter
    return selevator_state
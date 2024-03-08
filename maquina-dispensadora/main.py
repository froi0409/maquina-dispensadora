from entities.VendingMachine import VendingMachine

vending_machine = VendingMachine()

while True:
    # if vending_machine.state != "served-c1":
    print("Ingresar percepción: ")
    perception = input()

    vending_machine.state = vending_machine.update_state(vending_machine.state, vending_machine.action, perception)
    rule = vending_machine.rules[vending_machine.state]
    vending_machine.action = rule
    actionText = vending_machine.actions[vending_machine.action]

    print(actionText)


def on_button_pressed_a():
    global sender_id
    sender_id += -1
    if sender_id < 0:
        sender_id = 5
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global sender_id
    sender_id += 1
    if sender_id > 5:
        sender_id = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

sender_id = 0
radio.set_group(42)
sender_id = 5
radio.send_number(sender_id)
basic.show_number(sender_id)

def on_forever():
    radio.send_number(sender_id)
    basic.show_number(sender_id)
basic.forever(on_forever)

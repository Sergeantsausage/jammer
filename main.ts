input.onButtonPressed(Button.A, function () {
    sender_id += -1
    if (sender_id < 0) {
        sender_id = 5
    }
})
input.onButtonPressed(Button.B, function () {
    sender_id += 1
    if (sender_id > 5) {
        sender_id = 0
    }
})
let sender_id = 0
radio.setGroup(42)
sender_id = 5
basic.forever(function () {
    radio.sendNumber(sender_id)
    basic.showNumber(sender_id)
})

/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Michael Bruneau
 * Created on: Nov 2023
 * This program changes 
*/

// variables
const servoNumber1 = robotbit.Servos.S1


// setup
basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function () {
  robotbit.Servo(servoNumber1, 0)
  basic.showString('0')
  basic.showLeds(`
# # # . .
# . # . .
# # # . .
. . . . .
. . . . .
`)
  basic.pause(1000)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})

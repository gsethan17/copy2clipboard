from BMI import get_BMI
from BMI_derivative import get_derivatives_BMI

import tensorflow as tf

x1 = tf.Variable(65.)
x2 = tf.Variable(1.7)

with tf.GradientTape() as tape:
    tape.watch(x1)
    tape.watch(x2)

    y = get_BMI(x1, x2)

dy_dx = tape.gradient(y, (x1, x2))
print(dy_dx)

x1 = tf.constant(65.)
x2 = tf.constant(1.7)

dy_dx_derivative = get_derivatives_BMI(x1, x2)
print(dy_dx_derivative)
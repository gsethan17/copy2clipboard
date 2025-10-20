from BMI import get_BMI
from BMI_derivative import get_derivatives_BMI

import torch
x1 = torch.tensor(65., requires_grad=True)
x2 = torch.tensor(1.7, requires_grad=True)

y = get_BMI(x1, x2)

from torch import autograd
dy_dx = autograd.grad(
    outputs=y,
    inputs=(x1, x2),
    grad_outputs=torch.ones_like(y),
    retain_graph=True,
    create_graph=True,
)
print(dy_dx)

x1 = torch.tensor(65., requires_grad=False)
x2 = torch.tensor(1.7, requires_grad=False)

dy_dx_derivative = get_derivatives_BMI(x1, x2)
print(dy_dx_derivative)
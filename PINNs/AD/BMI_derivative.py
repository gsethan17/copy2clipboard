def get_derivatives_BMI(weight:float, height:float) -> tuple[float, float]:
    """Calculated the partial derivatives of the BMI (Body Mass Index)
        - BMI = weight / (height ** 2)
        - dBMI / dWeight = 1 / (height ** 2)
        - dBMI / dHeight = -2 * (weight / (height ** 3))
    params:
        weight (float): Body weight in kilograms.
        height (float): Height in meters.
    return:
        tuple[float, float]:
            - dBMI/dWeight (float): Partial derivatives of BMI with respect to weight
            - dBMI/dHeight (float): Partial derivatives of BMI with respect to height
    """
    
    x1 = weight
    x2 = height
    
    dy_dx1 = 1 / (x2 ** 2)
    dy_dx2 = -2 * (x1 / (x2 ** 3))
    
    return (dy_dx1, dy_dx2)


    
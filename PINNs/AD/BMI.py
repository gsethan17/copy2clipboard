def get_BMI(weight:float, height:float) -> float:
    """Calculate the BMI (Body, Mass Index)
    BMI = weight / (height ** 2)
    params:
        weight (float): Body weight in kilograms.
        height (float): Height in meters.
    return:
        BMI (float): The calculated BMI.
    """
    
    x1 = weight
    x2 = height
    
    y = x1 / (x2 ** 2)
    
    return y

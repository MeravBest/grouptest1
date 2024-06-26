from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0
    expression = ""

    for i in range(n):
        term = y_data[i]
        expression_term = str(y_data[i])
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
                expression_term += " * ( (x - " + str(x_data[j]) + ")  / (" + str(x_data[i]) + " - " + str(x_data[j]) + ") )"
        result += term
        if i == 0:
            expression +=" (" +expression_term
        else:
            expression += ") +( " + expression_term

    expression += ")"
    print(bcolors.OKGREEN, "\nInterpolating polynomial P(x) =", expression, bcolors.ENDC)

    return result, expression

if __name__ == '__main__':
    f = [(1.2, 1.2), (1.3, 2.3), (1.4, -0.5), (1.5, -0.89), (1.6, -1.37)]
    x_data = [1, 2, 5]
    y_data = [1, 0, 2]
    x_interpolate = 3  # The x-value where you want to interpolate
    y_interpolate, p = lagrange_interpolation(x_data, y_data, x_interpolate)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate, "is y =", y_interpolate, bcolors.ENDC)

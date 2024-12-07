import numpy as np

def tent_map(size, x0=0.5):
    result = []
    x = x0
    for _ in range(size):
        x = 2 * x if x < 0.5 else 2 * (1 - x)
        result.append(int(x * 255))  # Normalize to 0-255
    return result

def logistic_map(size, r=3.9, x0=0.5):
    result = []
    x = x0
    for _ in range(size):
        x = r * x * (1 - x)
        result.append(int(x * 255))  # Normalize to 0-255
    return result

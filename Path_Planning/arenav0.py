import numpy as np

def info():
    data = np.array([[0]*14]*14)
    for j in range(14):
        for k in range(14):
            if ((j//2) in (1,3,5)) and ((k//2) in (1,3,5)):
                data[j][k] = -1
    return data

if __name__ == '__main__':
    data = info()
    print(data)
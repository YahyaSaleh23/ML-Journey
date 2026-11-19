import numpy as np

x_train = np.array([1,2,3,4,5])
y_train = np.array([50,80,120,350,210])

def compute_cost_vectorized(x, y, w, b):
        m = x.shape[0]
        cost_array = ((w* x + b) - y) ** 2
        J_wb = (np.sum(cost_array)) / (2 *m)

        return J_wb

b = float(input("Enter the value of b: "))
w = float(input("Enter the value of w: "))

J_wb = compute_cost_vectorized(x_train,y_train,w,b)

print(f"the cost function with w ={w} b={b} is {J_wb}")
import numpy as np
import matplotlib.pyplot as plt
studying_hours = np.array([1,2,3,4])
results = np.array([50,65,70,90])

x = studying_hours.shape
ndim = studying_hours.shape[0]
print(f"shape: {x} \nndim: {ndim}")

def compute_model_output(x,w,b):
        m = x.shape[0]
        f_wb = np.zeros(m)

        for place in range(m):
                f_wb[place] = w * x[place] + b
        return f_wb


predictions = compute_model_output(studying_hours,13,35)

plt.scatter(studying_hours,results, c='r',marker='o', label="studing curve")
plt.plot(studying_hours,predictions, c='g', label='Our Prediction')
plt.title("students results")
plt.ylabel("Exam Score")
plt.xlabel("Hours Studied")
plt.legend()
plt.savefig('studying_curve.png')
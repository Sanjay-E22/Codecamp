import numpy as np
#create a function name calculator
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    data = np.reshape(np.array(numbers),(3,3))
    calc = {}
    calc['mean'] = [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data.flatten()).tolist()]
    calc['variance'] = [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data.flatten()).tolist()]
    calc['standard deviation'] = [np.std(data, axis=0).tolist(), np.std(data, axis=1).tolist(), np.std(data.flatten()).tolist()]
    calc['max'] = [np.max(data, axis=0).tolist(), np.max(data, axis=1).tolist(), np.max(data.flatten()).tolist()]
    calc['min'] = [np.min(data, axis=0).tolist(), np.min(data, axis=1).tolist(), np.min(data.flatten()).tolist()]
    calc['sum'] = [np.sum(data, axis=0).tolist(), np.sum(data, axis=1).tolist(), np.sum(data.flatten()).tolist()]
    return calc

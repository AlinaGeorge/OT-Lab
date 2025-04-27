from scipy.optimize import linprog

c = [-5, -3]
A = [
    [2, 1],
    [1, 1], 
]

b = [500, 400]

x_bounds = (100, None)  
y_bounds = (50, None)  

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

optimal_values = result.x
max_revenue = -result.fun 

print(f"Optimal number of chocolate cakes (x): {optimal_values[0]:.2f}")
print(f"Optimal number of vanilla cakes (y): {optimal_values[1]:.2f}")
print(f"Maximum revenue: ${max_revenue:.2f}")

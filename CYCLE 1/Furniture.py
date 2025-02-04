from scipy.optimize import linprog

c = [-20, -30]
A = [
    [1, 5],        
    [3, 1],      
]

b = [125, 80]

x_bounds = (0, None)  
y_bounds = (0, None) 

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

optimal_values = result.x
max_profit = -result.fun  

print(f"Optimal number of chairs (x): {optimal_values[0]:.2f}")
print(f"Optimal number of tables (y): {optimal_values[1]:.2f}")
print(f"Maximum profit: ${max_profit:.2f}")

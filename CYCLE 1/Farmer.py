from scipy.optimize import linprog

c = [-200, -150]  
A = [
    [1, 1],      
    [20, 10],      
    [10, 15],     
]


b = [60, 1200, 600]


x_bounds = (20, None) 
y_bounds = (10, None)  


result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')


if result.success:
    x_opt = result.x[0] 
    y_opt = result.x[1]  
    max_profit = -result.fun  
    
    print(f"Optimal number of acres of wheat: {x_opt:.2f}")
    print(f"Optimal number of acres of barley: {y_opt:.2f}")
    print(f"Maximum profit: ${max_profit:.2f}")
else:
    print("No solution found.")
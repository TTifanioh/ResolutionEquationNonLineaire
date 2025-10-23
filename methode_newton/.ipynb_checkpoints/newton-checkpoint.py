def method_newton(f,df,x0,tol=1e-10,max_iter=100):
    x_vals = [x0]
    for i in range (max_iter):
        x = x_vals[-1]
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            break
        	
        
        x_new = x - fx/dfx
        x_vals.append(x_new)
        
        print(f"Etape {i+1} : x = {x_new:.6f}. f(x) = {f(x_new):.6f}")
        
        if abs(x_new - x) < tol :
        	break
        
    return x_vals
def point_fixe(f,x0,tol=1e-8,max_iter=50):
    x_vals = [x0]
    for i in range(max_iter):
        x = x_vals[-1]
        x_news = f(x)
        x_vals.append(x_news)
        if abs(x_news - x) < tol:
            break
        print(f"Etape : {i+1}, x : {x_news:.6f}, f(x) : {f(x_news):.6f}")
    return x_news, i+1

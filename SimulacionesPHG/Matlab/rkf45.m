function [tout,yout]=rkf45(ode_function,tspan,y0,tolerance)
a=[0 1/4 3/8 12/13 1 1/2];
b=[0            0           0           0           0
   1/4          0           0           0           0
   3/32         9/32        0           0           0
   1932/2197    -7200/2197  7296/2197   0           0
   439/216      -8          3680/513    -845/4104   0
   -8/27        2           -3544/2565  1859/4104   -11/40];
c4=[25/216  0   1408/2565   2197/4104   -1/5    0];
c5=[16/135  0   6656/12825  28561/56430 -9/50   2/55];

if nargin < 4
    tol=1.e-8;
else
    tol=tolerance;
end

t0=tspan(1);
tf=tspan(2);
t=t0;
y=y0;
tout=t;
yout=y';
h=(tf-t0)/100;

while t < tf
    hmin=16*eps(t);
    ti=t;
    yi=y;
    for i=1:6
        t_inner= ti + a(i)*h;
        y_inner= yi;
        for j=1:i-1
            y_inner= y_inner + h*b(i,j)*f(:,j);
        end
        f(:,i)=feval(ode_function, t_inner, y_inner);        
    end
    
    te= h*f*(c4'-c5');
    te_max= max(abs(te));
    
    ymax=max(abs(y));
    te_allowed= tol*max(ymax,1.0);
    
    delta = (te_allowed/(te_max +  eps))^(1/5);
    
    if te_max <= te_allowed
        h = min(h,tf-t);
        t = t+h;
        y = yi + h*f*c5';
        tout = [tout;t];
        yout = [yout;y'];
    end
    h=min(delta*h, 4*h);
    if h < hmin
        fprint(['\n\nPrecaucion: valores (%g) en el tiempo %g.\n\n'],hmin,t)
        return
    end
end

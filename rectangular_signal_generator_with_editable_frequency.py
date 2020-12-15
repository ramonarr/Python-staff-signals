# Generating a rectangular periodic signal with editable frequency in python

t = arange(0,2,0.001)

f = 5         # Frequency [Hz]

x = 0         # The initial value of x

k = 1         # Multiplication factor

N = 1001      # Harmonics number

while k <= N:
        x = x + (4/pi)*(1/k)*sin(2*k*f*pi*t)
        k = k+2

figure(figsize=(9,6))
plot(t,x)
title(r'Rectangular signal with editable frequency in Python: $x(t)$ ')
xlabel(r't')
ylabel(r'$x(t)$')
grid()
 
        

# Generating a triangular periodic signal with editable frequency in Python

t = arange(0,2,0.001)

f = 5         # Frequency [Hz]

x = 0         # The initial value of x

i = 0         # Multiplication factor

N = 1001      # Harmonics number

while i < 1001:
        x = x + 8/pow(pi,2)*pow(-1,i)*pow(2*i+1,-2)*sin(2*f*pi*(2*i+1)*t)
        i = i+1

figure(figsize=(9,6))
plot(t,x)
title(r'Triangular signal with editable frequency in Python: $x(t)$ ')
xlabel(r't')
ylabel(r'$x(t)$')
grid()

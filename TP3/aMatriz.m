
function [delay30i,delay30f30l,delay50l,delay50f] = aMatriz(a,b,c,d)
%matriz = zeros(11,11);
for i=1:121
    delay30f30l(a(i,1)*10+1,a(i,2)*10+1) = a(i,4);
end

for i=1:121
    delay30i(b(i,1)*10+1,b(i,2)*10+1) = b(i,4);
end

for i=1:121
    delay50f(c(i,1)*10+1,c(i,2)*10+1) = c(i,4);
end

for i=1:121
    delay50l(d(i,1)*10+1,d(i,2)*10+1) = d(i,4);
end
end

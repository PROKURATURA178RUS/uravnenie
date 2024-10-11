input_data = open('input.txt','r')
data = input_data.read ()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
output_data = open('output.txt','a')
for x in range(-100, 100):
    if ((a * (x**3) + b * (x**2) + c * x + d  ) == 0):
        
        output_data.write(str(x) + ' ' )

input_data.close()
output_data.close()        
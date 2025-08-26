tall = 13

# Tallet 13 er 00001101 binært.
print(f'Tallet {tall} er {tall} binært.')          
# fill=0, width=8 og type=b

# Tallet 13 er 0d i heksadesimalt.
print(f'Tallet {tall} er {tall} heksadesimalt.') 
# fill=0, width=2 og type=x

verdier =[1.1, 22.22, 333.333]
#      1.10
#     22.22
#    333.33
for verdi in verdier:
    print(f'{verdi}') 
# align=>, width=10 og type=f, precision=2 og type=f

tall = 1/3
print(tall) # Bruk round() 0.33
print(f'{tall}') # 0.333
print(f'{tall}') # 3.3e-01 (standard form)
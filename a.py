import math

#input values i,N,r,L,permeability (u),

i=float(input("enter current: "))
N=1088 #N=float(input("enter number of turns: "))
r=0.00275 #meter #r=float(input("enter radius of torquer rod:  "))
L=0.086 #L=float(input("enter length: "))
u=6000#u=float(input("enter permeabiliy of material used: "))

#Nd =demagnetization factor , Nnd= numerator of Nd ,Ndd= dinominator of Nd

Nnd=4*(math.log(L/r)-1)
Ndd=((L/r)*(L/r))-4*math.log(L/r)
Nd= Nnd/Ndd
print("Demagnetization factor Nd= ",Nd)


# B = Magnetic field , Bn= numerator of B, Bd= denominator of B

u0 = 0.000001256

Bn= u0*N*i
Bd= L*((1-Nd)/u +Nd)
B= Bn/Bd

print("Magnetic field B=",B)


#M = dipole moment, W resistance per unit length of wire ,V= input voltage

W= float(input("enter Resistance per unit length : "))
R=float(input("enter Resistance of wire: "))
V =float(input("enter input voltage: "))

x=(u-1)/(1+(u-1)*Nd)

M=((r*V)/(2*W))*(1+x)

print("dipole moment=",M)

#M = dipole moment

x=(u-1)/(1+(u-1)*Nd)
M=(math.pi)*r*r*N*i*(1+x)
print(x)
print("dipole moment=",M)



#dipole moment practically

r0= float(input("Enter the distance of magnectometer from coil="))
b=float(input("ENTER MAGNECTIC FIELD "))
m=(b*r0*r0*r0*10e7)/2
print("dipole moment practically=",m)

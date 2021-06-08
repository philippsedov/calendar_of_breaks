Date = '18/05/2021'
z = 12.5 # zenith
s = 100; ss = 5*s/60 # sleep cycle 90-100 minutes
t = 8+(s/60) # labor + sleep
t81 = 8+(s/60)+40.1/60 # labor + sleep and rounding to 8 hours
t = t81

# short break
b1 = 5; b1n = 25
# long break
b2 = 30; b2n = 60*2

# cycles
bb1 = b1n + b1
bb2 = b2n + b2
bb = bb1 + bb2

# total
tb = ( (( z*60 - t/2*60 ) // bb) * (b1+b2) )*2
ta = ( t*60 - tb)

print (
'active  ',round((z-t/2)//1),':',round((z-t/2)%1*60),'–',
         round((z+t/2)//1),':',round((z+t/2)%1*60),' ',round(t//1),':',round(t%1*60),'\n'
 'sleep  ',round((z-s/60/2)//1),':',round((z-s/60/2)%1*60),'–',
         round((z+s/60/2)//1),':',round((z+s/60/2)%1*60),'  ',round(100//60),':',round(100%60),'\n' 
 'sleep0 ',round((z-12+24-ss/2) // 1),':',round((z-12+24-ss/2)%1*60),'– ',
         round((z-12+ss/2)//1),':',round((z-12+ss/2)%1*60),'  ',round(ss//1),':',round(ss%1*60),'\n')

print ('work   ', round(ta),'min   ', round(ta/60//1),':',round(ta/60%1*60),'   ', round(ta/(tb+ta)*100),'%')
print ('relax  ', round(tb),'min   ', round(tb/60//1),':',round(tb/60%1*60),'  ', round(tb/(tb+ta)*100),'%')
print ('every  ',b1n,'for',b1,'\n','\n')


print ('Subject	Start Date	Start Time	End Date	End Time')

print ('Sleep 2	',Date,'\t',round((z-s/60/2)//1),':',round((z-s/60/2)%1*60),'\t',Date,'\t',
         round((z+s/60/2)//1),':',round((z+s/60/2)%1*60))
print ('Sleep 1	',Date,'\t',round((z-12+24-ss/2) // 1),':',round((z-12+24-ss/2)%1*60),'\t','=D2+1','\t',
         round((z-12+ss/2)//1),':',round((z-12+ss/2)%1*60))


for i in range(round((z-t/2)*60)+b1n,round((z+t/2)*60)+b1n,bb1):
    print ('Break	',Date,'\t',int(i/60//1),':',int(i%60),'\t',Date,'\t',int((i+b1)/60//1),':',int((i+b1)%60))

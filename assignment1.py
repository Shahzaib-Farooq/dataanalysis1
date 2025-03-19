'''
print("*********Welcome to Cars Store***********")
ran=int(input("Dear customer please enter amount: "))
mod=int(input("Please select your desired car model, for eg:(2024,2023...): "))
col=input("Please enter your favourite color for eg:(silver, metallic, black, white: )")
cc=int(input("Please enter no of cc's, for eg:(2200,2000,1600,1400)"))
door=int(input("Enter num of doors you want for eg: 5 or 6: "))
if ran>=100000:
   
    if mod==2024 and col=="metallic" and cc==2200 and door==6:
        print("You can buy lamborghini")
    elif mod==2023 and col in ["black","white","silver"] and cc==2000 and door in[5,6]:
        print("You can buy lamborghini with 2000 cc's")
    elif mod==2022 and col in ["black","white","silver"] and cc==1600 and door in[5,6]:
        print("You can buy Land cruiser")
    if mod==2021 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("You can buy land cruise with 1400cc")
    elif mod==2020 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("You can corolla")
    elif mod==2019 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("You can buy corolla with 1400cc")
    if mod==2018 and col in ["black","white"] and cc==1400 and door==5:
        print("You can buy Civic")
    elif mod==2017 and col in ["black","white","black"] and cc==1400 and door==5:
        print("You can buy civic with 2017 model")
    elif mod==2016 and col in ["black","white","black"] and cc==1400 and door==5:
        print("You can buy civic with 2016 model")
    if mod==2015 and col in ["black","white"] and cc==1400 and door==5:
        print("You can buy suzuki")
    elif mod==2014 and col in ["black","white","black"] and cc==1400 and door==5:
        print("You can buy suzuki with 2014 model")
    elif mod==2013 and col in ["black","white","black"] and cc==1400 and door==5:
        print("You can buy suzuki with 2013 model")
    else:
        print("you can buy mehran")
elif 50000<=ran<100000:
    if mod==2012 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy suzuki in this range")
    elif mod==2011 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy suzuki of 2011 model")
    elif mod==2010 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy suzuki of 2010 model")
    if mod==2009 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy toyota in this range")
    elif mod==2008 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy toyota of 2008 model")
    elif mod==2007 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy toyota of 2007 model")
    if mod==2006 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW in this range")
    elif mod==2005 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW of 2005 model")
    elif mod==2004 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW of 2004 model")
    if mod==2003 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW in this range")
    elif mod==2002 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW of 2002 model")
    elif mod==2001 and col in ["black","white","silver"] and cc==1400 and door==5:
        print("you can buy BMW of 2001 model")
    else:
        print("you can buy mehran ")
else:
    print("Dear customer your budget is low no car is available")
'''
print("********Welcome to the Mobile Store********")
bud=int(input("Dear customer please enter your budget: "))
ram=int(input("Please enter how much RAM you want, for eg:(2GB, 4Gb...16GB) "))
rom=int(input("Please enter how much ROM you want, for eg:(16GB, 32GB,...256GB)"))
f_cam=int(input("Please enter camera specification for front camera, for eg:(8mpx,16mpx...32mpx)"))
b_cam=int(input("Please enter camera specification for back camera, for eg:(16mpx,32mpx...48mpx)"))
bat=int(input("Please enter battery specification, for eg:(300mah,5000mah....)"))
col=input("Enter colour you want, for eg:(black,white,...gray)")
if bud>=100000:
    if ram in [128,256] and rom in [628,912] and f_cam in [32,48] and b_cam in [128,256]:
        print("you can buy Iphone  in this range")
    elif ram in [64,128] and rom in [314,628] and f_cam in [16,32] and b_cam in [64,128]:
        print("You can buy samsung in this range")
    elif ram in [32,64] and rom in [157,314] and f_cam in [8,16] and b_cam in [32,64]:
        print("You can buy RealmeC35 in this range")
    if ram in [16,32] and rom in [75,156] and f_cam in [4,8] and b_cam in [16,32]:
        print("you can buy google(pixels)  in this range")
    elif ram in [8,16] and rom in [35,70] and f_cam in [2,4] and b_cam in [8,16]:
        print("You can buy Tecno in this range")
    elif ram in [4,8] and rom in [14,35] and f_cam in [2,6] and b_cam in [4,8]:
        print("You can buy Oneplus in this range")
    if ram in [2,4] and rom in [16,32] and f_cam in [6,8] and b_cam in [6,8]:
        print("you can buy Asus ROG Phone 9 Pro Edition  in this range")
    elif ram in [2,16] and rom in [8,16] and f_cam in [8,12] and b_cam in [4,12]:
        print("You can buy Honor Magic 6 RSR  in this range")
    elif ram in [4,8] and rom in [4,8] and f_cam in [4,16] and b_cam in [32,14]:
        print("You can buy Samsung Galaxy S25 Ultra in this range")
    if ram in [3,4] and rom in [2,4] and f_cam in [16,32] and b_cam in [16,32]:
        print("you can buy Google Pixel 9 Pro  in this range")
    elif ram in [2,8,] and rom in [3,6] and f_cam in [16,8] and b_cam in [16,8]:
        print("You can buy OnePlus 13 in this range")
    elif ram in [4,8] and rom in [2,4] and f_cam in [8,16] and b_cam in [8,16]:
        print("You can buy RealmeC35 in this range")
    else:
        print("You can buy infinix in this range")
elif 50000<=bud<100000:
    if ram in [50,64] and rom in [128,256] and f_cam in [48,32] and b_cam in [64,128]:
        print("you can buy Xiaomi 14 Ultra in this range")
    elif ram in [24,16] and rom in [16,24] and f_cam in [32,16] and b_cam in [32,64]:
        print("You can buy Vivo X100 Pro+ in this range")
    elif ram in [32,16] and rom in [64,32] and f_cam in [8,16] and b_cam in [16,32]:
        print("You can buy Realme GT5 Pro in this range")
    if ram in [8,16] and rom in [16,32] and f_cam in [8,32] and b_cam in [8,16]:
        print("you can buy  Nubia RedMagic 9 Pro (Gaming Phone)  in this range")
    elif ram in [8,32] and rom in [64,128] and f_cam in [16,12] and b_cam in [16,12]:
        print("You can buy Samsung Galaxy Z Fold 5 in this range")
    elif ram in [16,4] and rom in [32,64] and f_cam in [8,12] and b_cam in [32,12]:
        print("You can buy Sony Xperia 1 V in this range")
    if ram in [28,16] and rom in [16,8] and f_cam in [16,30] and b_cam in [12,18]:
        print("you can buy  Motorola Edge 50 Ultra in this range")
    elif ram in [32,8] and rom in [8,4] and f_cam in [8,32] and b_cam in [32,16]:
        print("You can buy Asus Zenfone 10 in this range")
    elif ram in [8,4] and rom in [4,16] and f_cam in [4,16] and b_cam in [8,16]:
        print("You can buy Huawei P60 Pro in this range")
    if ram in [2,4] and rom in [16,8] and f_cam in [4,8] and b_cam in [16,8]:
        print("you can buy infinix smart 5 in this range")
    elif ram in [3,16] and rom in [4,16] and f_cam in [8,16] and b_cam in [2,12]:
        print("You can buy tecno camon in this range")
    elif ram in [4,32] and rom in [8,16] and f_cam in [2,4] and b_cam in [32,16]:
        print("You can buy G Five in this range")
else:
        print("Dear customer your budget is low no phone available")
    
        
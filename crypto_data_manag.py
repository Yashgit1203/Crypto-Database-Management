# CRYPTOCURRENCY - DATA MANAGEMENT

print("\n*** WELCOME ****")

# Program using list to display crypto coins purchased



number_list = []


print("\n*** Available Cryptos **\n")
print("~ 1. Bitcoin")
print("~ 2. Ethereum")
print("~ 3. Polygon")
print("~ 4. Dogecoin\n")


# Program BY Using Tuple

print("** Levels of Crypto ***")
print("> High")
print("> Moderate")
print("> Average")
print("> Low")


#Initializing Variables in tuple
tuple=("Bitcoin","Ethereum","Polygon","Dogecoin")

(High,Moderate,Average,Low)=tuple


# Getting input from User

x=str(input("Enter level of crypto you wan't to purchase : "))


#Applying Control Structures

if(x=='High'):
  print("You can purchase:",High," and much more accordingly by your choice \n")
elif(x=='Moderate'):
  print("You can purchase:",Moderate," and much more accordingly by your choice \n")
elif(x=='Average'):
  print("You can purchase:",Average," and much more accordingly by  your choice \n")
elif(x=='Low'):
  print("You can purchase:",Low," and much more accordingly by your choice \n")
else:
  print("Please,Enter Correct Information\n")



# Final step to display output
print("\n****Crypto Price status are as follows**\n")
print("**************************")

print("Day        Bitcoin\tEthereum\tPolygon\t\tDogecoin\n")
print("**************************")
print("Monday    :20134 $\t1194 $\t\t0.456 $\t\t0.324 $\n")
print("Tuesday   :20246 $\t1218 $\t\t0.232 $\t\t0.159 $\n")
print("Wednesday :20221 $\t1232 $\t\t0.434 $\t\t0.246 $\n")
print("Thursday  :20322 $\t1159 $\t\t0.218 $\t\t0.243 $\n")
print("Friday    :20218 $\t1246 $\t\t0.243 $\t\t0.232 $\n")
print("Saturday  :20233 $\t1221 $\t\t0.159 $\t\t0.434 $\n")
print("Sunday    :20120 $\t1243 $\t\t0.456 $\t\t0.246 $\n")

print("**************************")
mm=str(input("Did You want to invest in Crypto(Yes,No) :   "))
if(mm=='Yes'):

  q=str(input("Enter the day at which Crypto Purchase : "))
  n = int(input("\nEnter number of crypto you have to purchase : "))

  # for loop to display 
  for i in range(1,n+1):
    print("Enter  coin", i,":" )
  # Getting input as string by User
    item = str(input())
  # We use Append to add item
    number_list.append(item)
  print("Coins in your wishlist are : ", number_list,"\n")

  bitcoin=int(input("\nHow many Bitcoin you want to purchase ?\n "))
  ethereum=int(input("How many Ethereum you want to purchase ?\n "))
  polygon=int(input("How many Polygon you want to purchase ?\n "))
  dogecoin=int(input("How many Dogecoin you want to purchase ?\n "))

  if(q=='Monday'):
    b=20134*bitcoin
    e=1194*ethereum
    p=0.456*polygon
    d=0.324*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",b,"$")
    print("You purchased ",ethereum, "Ethereum at",e,"$")
    print("You purchased ",polygon,"Polygon at ",p,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",d,"$\n")
    print("Your total price is ",b+e+p+d,"$")
  elif(q=='Tuesday'):
    bb=20246*bitcoin
    ee=1218*ethereum
    ppp=0.232*polygon
    dd=0.159*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",bb,"$")
    print("You purchased ",ethereum, "Ethereum at",ee,"$")
    print("You purchased ",polygon,"Polygon at ",ppp,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",dd,"$\n")
    print("Your total price is ",bb+ee+ppp+dd,"$")
  elif(q=='Wednesday'):
    bbb=20221*bitcoin
    eee=1232*ethereum
    pp_p=0.434*polygon
    ddd=0.246*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",bbb,"$")
    print("You purchased ",ethereum, "Ethereum at",eee,"$")
    print("You purchased ",polygon,"Polygon at ",pp_p,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",ddd,"$\n")
    print("Your total price is ",bbb+eee+pp_p+ddd,"$")
  elif(q=='Thursday'):
     bb_b=20322*bitcoin
     ee_e=1159*ethereum
     p_pp=0.218*polygon
     dd_d=0.243*dogecoin

     print("\nYou purchased ",bitcoin,"Bitcoin at",bb_b,"$")
     print("You purchased ",ethereum, "Ethereum at",ee_e,"$")
     print("You purchased ",polygon,"Polygon at ",p_pp,"$")
     print("You purchased ",dogecoin, "Dogecoin at ",dd_d,"$\n")
     print("Your total price is ",bb_b+ee_e+p_pp+dd_d,"$")
  elif(q=='Friday'):
    gg=20218*bitcoin
    hh=1246*ethereum
    ii=0.243*polygon
    jj=0.232*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",gg,"$")
    print("You purchased ",ethereum, "Ethereum at",hh,"$")
    print("You purchased ",polygon,"Polygon at ",ii,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",jj,"$\n")
    print("Your total price is ",gg+hh+ii+jj,"$")
  elif(q=='Saturday'):
    ggg=20233*bitcoin
    hhh=1221*ethereum
    iii=0.159*polygon
    jjj=0.434*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",ggg,"$")
    print("You purchased ",ethereum, "Ethereum at",hhh,"$")
    print("You purchased ",polygon,"Polygon at ",iii,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",jjj,"$\n")
    print("Your total price is ",ggg+hhh+iii+jjj,"$")
  else:
    gg_g=20120*bitcoin
    hh_h=1243*ethereum
    ii_i=0.456*polygon
    jj_j=0.246*dogecoin

    print("\nYou purchased ",bitcoin,"Bitcoin at",gg_g,"$")
    print("You purchased ",ethereum, "Ethereum at",hh_h,"$")
    print("You purchased ",polygon,"Polygon at ",ii_i,"$")
    print("You purchased ",dogecoin, "Dogecoin at ",jj_j,"$\n")
    print("Your total price is ",gg_g+hh_h+ii_i+jj_j,"$")

  
  # Using control structures

  print("**************************")
  uuu=str(input("Do you want to Sell Cryptos or not ? (Sell/Not) ?"))
  if(uuu=='Sell'):
    print("=====To Know Profit and Loss Of Crypto=====")
    nn=str(input("Enter the day at which you want to sell :"))
    nun=int(input("Enter how many types of coins you want to Sell : "))
    it=str(input("\nAre you confirm to sell ? (Yes/No) ?"))
    
    if(it=='Yes'):
      if(nn=='Monday'):
        bm=20134*bitcoin
        em=1194*ethereum
        pm=0.456*polygon
        dm=0.324*dogecoin
        if(q=='Tuesday'):
          if(nun==1):
            mp=str(input("Enter the coin name which you want to Sell:"))
            bm=20134*bitcoin
            em=1194*ethereum
            pm=0.456*polygon
            dm=0.324*dogecoin
            if(mp=='Bitcoin'):
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
            elif(mp=='Ethereum'):
              if(em>ee):
                  print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                  print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                  print("You are in Loss in Ethereum of : -",ee-em,"$")
            elif(mp=='Polygon'):
              if(pm>ppp):
                  print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                  print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                  print("You are in Loss in Polygon of : -",ppp-pm,"$")
            else:
              if(dm>dd):
                  print("You got profit in Dogecoin of : +",dm-dd,"$")
              elif(dm==dd):
                  print("Their is No profit and loss in Dogecoin : ",dd,"$")
              else:
                  print("You are in Loss in Dogecoin of : -",dd-dm,"$")
#####################################################################################################################
          elif(nun==2):
            mq=str(input("Enter the coin name which you want to Sell:"))
            mn=str(input("Enter the coin name which you want to Sell:"))
            if((mq=='Bitcoin')and(mn=='Ethereum')):
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
  
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
            elif((mq=='Ethereum')and(mn=='Bitcoin')):
  
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$") 
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
            elif((mq=='Bitcoin')and(mn=='Polygon')):
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
            elif((mq=='Polygon')and(mn=='Bitcoin')):
              
              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")    
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
            elif((mq=='Ethereum')and(mn=='Polygon')):
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")

              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
            elif((mq=='Polygon')and(mn=='Ethereum')):

              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
            elif((mq=='Ethereum')and(mn=='Dogecoin')):
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
              if(dm>dd):
                print("You got profit in Dogecoin of : +",dm-dd,"$")
              elif(dm==dd):
                print("Their is No profit and loss in Dogecoin : ",dd,"$")
              else:
                print("You are in Loss in Dogecoin of : -",dd-dm,"$")
            elif((mq=='Dogecoin')and(mn=='Ethereum')):
             
              if(dm>dd):
                print("You got profit in Dogecoin of : +",dm-dd,"$")
              elif(dm==dd):
                print("Their is No profit and loss in Dogecoin : ",dd,"$")
              else:
                print("You are in Loss in Dogecoin of : -",dd-dm,"$")
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
            elif((mq=='Polygon')and(mn=='Dogecoin')):
              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
  
              if(dm>dd):
                print("You got profit in Dogecoin of : +",dm-dd,"$")
              elif(dm==dd):
                print("Their is No profit and loss in Dogecoin : ",dd,"$")
              else:
                print("You are in Loss in Dogecoin of : -",dd-dm,"$")
            else:
  
              if(dm>dd):
                print("You got profit in Dogecoin of : +",dm-dd,"$")
              elif(dm==dd):
                print("Their is No profit and loss in Dogecoin : ",dd,"$")
              else:
                print("You are in Loss in Dogecoin of : -",dd-dm,"$")
              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
  ###############################################################################################################################
          elif(nun==3):
            mq=str(input("Enter the coin name which you want to Sell:"))
            mz=str(input("Enter the coin name which you want to Sell:"))
            mo=str(input("Enter the coin name which you want to Sell:"))
            if((mq=='Bitcoin')and(mz=='Ethereum')and(mo=='Polygon')):
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
  
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")

              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
            elif((mq=='Ethereum')and(mz=='Bitcoin')and(mo=='Polygon')):
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")  
            else:
              if(bm>bb):
                print("You got profit in Bitcoin of : +",bm-bb,"$")
              elif(bm==bb):
                print("Their is No profit and loss in Bitcoin : ",bb,"$")
              else:
                print("You are in Loss in Bitcoin of : -",bb-bm,"$")
  

              if(pm>ppp):
                print("You got profit in Polygon of : +",pm-ppp,"$")
              elif(pm==ppp):
                print("Their is No profit and loss in Polygon : ",ppp,"$")
              else:
                print("You are in Loss in Polygon of : -",ppp-pm,"$")
              if(em>ee):
                print("You got profit in Ethereum of : +",em-ee,"$")
              elif(em==ee):
                print("Their is NO profit and loss in Ethereum : ",ee,"$")
              else:
                print("You are in Loss in Ethereum of : -",ee-em,"$")
          else:
             mq=str(input("Enter the coin name which you want to Sell:"))
             mz=str(input("Enter the coin name which you want to Sell:"))
             my=str(input("Enter the coin name which you want to Sell:"))
             mr=str(input("Enter the coin name which you want to Sell:"))
              # Applying conditional statement
             if((mq=='Bitcoin')and(mz=='Ethereum')and(my=='Polygon')and(mr=='Dogecoin')):
                if(bm>bb):
                  print("You got profit in Bitcoin of : +",bm-bb,"$")
                elif(bm==bb):
                  print("Their is No profit and loss in Bitcoin : ",bb,"$")
                else:
                  print("You are in Loss in Bitcoin of : -",bb-bm,"$")
  
                if(em>ee):
                  print("You got profit in Ethereum of : +",em-ee,"$")
                elif(em==ee):
                  print("Their is NO profit and loss in Ethereum : ",ee,"$")
                else:
                  print("You are in Loss in Ethereum of : -",ee-em,"$")

                if(pm>ppp):
                  print("You got profit in Polygon of : +",pm-ppp,"$")
                elif(pm==ppp):
                  print("Their is No profit and loss in Polygon : ",ppp,"$")
                else:
                  print("You are in Loss in Polygon of : -",ppp-pm,"$")
  
                if(dm>dd):
                  print("You got profit in Dogecoin of : +",dm-dd,"$")
                elif(dm==dd):
                  print("Their is No profit and loss in Dogecoin : ",dd,"$")
                else:
                  print("You are in Loss in Dogecoin of : -",dd-dm,"$")
  

    else:
      print("OK")
  else:
    print("\nThanks For purchasing")
else:
  print("Have a Nice Day!")
  # Applying function in Crypto

def my_function(crypto):

  # Adding 'Thanks' with variable assigned in above function 'crypto'

   print("Thanks" + crypto)
   
  # Calling function

print("\n**********************\n\n")
my_function(" For Purchasing Crypto")
my_function(" For Visiting Our Website")
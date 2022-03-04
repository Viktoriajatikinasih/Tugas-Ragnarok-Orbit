#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("Nomor 1")


# In[2]:


a = False
b = True
c = False

(b and c)


# In[3]:


b or c


# In[4]:


not a and b


# In[5]:


(a and b) or not c


# In[6]:


not b and not (a or c)


# In[7]:


print ("Nomor 2")


# In[8]:


print (Hello!)
something == input ('Enter something: )
print ('You entered:' something)


# In[9]:


something = input ("Enter something:")
print ("Hello!")
print ("You entered :", something)


# In[10]:


print ("Nomor 3")


# In[11]:


print('Hello!')
something = input("Enter something: ")
if something = 'hello':
    print("Hello for you too!")

elif something = 'hi'
    print('Hi there!')
else:
    print("I don't know what," something,"means.")


# In[12]:


print('Hello!')
something = input("Enter something: ")
if something == 'hello':
    print("Hello for you too!")

elif something == 'hi':
    print("Hi there!")

else:
    print("I don't know what", something, "means.")


# In[15]:


print ("Nomor 4")


# In[13]:


for x in range(100):
    print("halo hai")


# In[14]:


i = 1
while i <= 100:
  print("halo hai")
  i += 1


# In[17]:


print ("Nomor 5 a")


# # Table

# |Pemain 1||Pemain 2||Pemenang|
# |--------||--------||--------|
# |Batu||Gunting||Pemain 1|
# |Gunting||Gunting||Seri|
# |Batu||Batu||Seri|
# |Kertas||Kertas||Seri|
# |Batu||Kertas||Pemain 2|
# |Kertas||Batu||Pemain 1|
# |Kertas||Gunting||Pemain 2|
# |Gunting||Batu||Pemain 2|
# |Gunting||Kertas||Pemain 1|

# In[18]:


print ("Nomor 5 b")


# In[20]:


print("Game Suit!")
Player1 = input("Masukkan Player 1: ")
Player2 = input("Masukkan Player 2: ")
if (Player1 == 'batu') and (Player2 == 'batu'):
    print("Seri!")

elif (Player1 == 'batu') and (Player2 == 'kertas'):
    print("Player 2 Wins!")
    
elif (Player1 == 'batu') and (Player2 == 'gunting'):
    print("Player 1 Wins!")
    
elif (Player1 == 'gunting') and (Player2 == 'gunting'):
    print("Seri!")
    
elif (Player1 == 'gunting') and (Player2 == 'batu'):
    print("Player 2 Wins!")
    
elif (Player1 == 'gunting') and (Player2 == 'kertas'):
    print("Player 1 Wins!")
    
elif (Player1 == 'kertas') and (Player2 == 'kertas'):
    print("Seri!")
    
elif (Player1 == 'kertas') and (Player2 == 'batu'):
    print("Player 1 Wins!")
    
elif (Player1 == 'kertas') and (Player2 == 'gunting'):
    print("Player 2 Wins!")
else:
    print("Input tidak valid!. Gunakan “batu”, “ gunting” dan “kertas” tanpa tanda kutip!")


# In[22]:


print ("Nomor 6")


# In[21]:


while True:
    kata = input('Masukkan kata: ')
    if kata == 'berhenti':
        break
print('Perulangan Berakhir')


# In[23]:


print ("Nomor 7")


# In[27]:


while True :
    print ("------Selamat Berbelanja------")
    print ("------------------------------")
    print ("---------MENU CEMILAN---------")
    print (" 1. |Corn Dog - Rp. 10.000,-| ")
    print (" 2. |Kebab    - Rp. 12.000,-| ")
    print (" 3. |Hottang  - Rp. 15.000,-| ")
    print ("------------------------------")
    pilihMenu = input("Masukkan Menu : ")
    if pilihMenu == '1':
        print("Kamu memesan Corn Dog dengan harga Rp. 10.000,-, terima kasih sudah berbelanja!")
    elif pilihMenu == '2':
        print("Kamu memesan Kebab dengan harga Rp. 12.000,-, terima kasih sudah berbelanja!")
    elif pilihMenu == '3' :
        print("Kamu memesan Hottang dengan harga Rp. 15.000,-, terima kasih sudah berbelanja!")
    else:
        print("Menu tidak tersedia")
    
    tambahan = input ("Adakah Tambahan : ")
    if tambahan == 'cukup':
            break
print("Terima kasih sudah berbelanja cemilan dari kami!")


# In[28]:


print("Nomor 8")


# In[1]:


while True :
    print ("------Selamat Berbelanja------")
    print ("------------------------------")
    print ("---------MENU CEMILAN---------")
    print (" 1. |Corn Dog - Rp. 10.000,-| ")
    print (" 2. |Kebab    - Rp. 12.000,-| ")
    print (" 3. |Hottang  - Rp. 15.000,-| ")
    print ("------------------------------")
    
    pilihMenu = input("Masukkan Menu : ")
    
    if pilihMenu == '1':
        print("Kamu memesan Corn Dog dengan harga per satuan Rp. 10.000,-.")
        corndog = int(input("Berapa banyak Corn Dog yang dipesan? "))
        hargaCorndog = 10000
        total = (hargaCorndog*corndog)
        print ("Total Bayar = Rp.", total)
        bayar = int(input("Uang Bayar = Rp. "))
        print ("Kembalian = Rp.", bayar-total)
        print ("------------------------------")
        
    elif pilihMenu == '2':
        print("Kamu memesan Kebab dengan harga per satuan Rp. 12.000,-.")
        kebab = int(input("Berapa banyak Kebab yang dipesan? "))
        hargaKebab = 12000
        total = (hargaKebab*kebab)
        print ("Total Bayar = Rp.", total)
        bayar = int(input("Uang Bayar = Rp. "))
        print ("Kembalian = Rp.", bayar-total)
        print ("------------------------------")
        
    elif pilihMenu == '3' :
        print("Kamu memesan Hottang dengan harga per satuan Rp. 15.000,-.")
        hottang = int(input("Berapa banyak Hottang yang dipesan? "))
        hargaHottang = 10000
        total = (hargaHottang*hottang)
        print ("Total Bayar = Rp.", total)
        bayar = int(input("Uang Bayar = Rp. "))
        print ("Kembalian = Rp.", bayar-total)
        print ("------------------------------")
        
    else:
        print("Menu tidak tersedia")
    
    tambahan = input ("Masukkan Tambahan : ")
    if tambahan == 'cukup':
            break
            
print("Terima kasih sudah berbelanja cemilan dari kami!")


# In[ ]:





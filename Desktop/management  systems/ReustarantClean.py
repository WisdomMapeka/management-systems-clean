from tkinter import*
import random
import time

root = Tk()
root.geometry('1500x1500+0+0')
root.title('Mutakunanzva Management System')
#=======================================frames====================================================================
f0 = Frame(root, width = 1500, height = 150, relief = SUNKEN)
f0.pack(side=TOP)

f1 = Frame(root, width = 800,height = 800, relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 600,height = 800, relief = SUNKEN)
f2.pack(side=RIGHT)



#===================reastaurant managemet sytem display=========================================================
lbinfo = Label(f0, font=('arial',30,'bold'),text='Mutakunanzva Management System',fg='#000000',bd=5,anchor='w')
lbinfo.grid(row=0, column=0)
#===============================time=============================================================================
localtime = time.asctime(time.localtime(time.time()))
mytime = Label(f0, font=('arial',20,'bold'),text=localtime,fg='#000000',bd=5, anchor='w')
mytime.grid(row=1, column=0)

lbinfo = Label(f0, font=('arial',20,'bold'),text='WELCOME',fg='#000000',bd=5,anchor='w')
lbinfo.grid(row=3, column=0)


#==============================================far left widgets==================================================
OrderNo = StringVar()
PotatoChips = StringVar()
SadzaNbeef = StringVar()
SadzaNemazondo = StringVar()
SadzaNehuku = StringVar()
SadzaNederere = StringVar()
SadzaRezviyo = StringVar()
SadzaRemhunga = StringVar()
Burger = StringVar()
RiceNchicken = StringVar()
RiceNbeef = StringVar()
Cheese = StringVar()
#------------------------------------------------------------------------------------------------------------
SadzaNfish = StringVar()
Coffe = StringVar()
SadzaNmufushwa = StringVar()
SadzaNmubora = StringVar()
SadzaNnzungu = StringVar()
SadzaNbakayawo = StringVar()
Scud = StringVar()
Ngoda = StringVar()
Super = StringVar()
Lager = StringVar()
Eagle = StringVar()
Whiskey = StringVar()
#-------------------------------------------------------------------------------------------------------------------
Brandy  = StringVar()
Coke = StringVar()
Fanta = StringVar()
Sprite = StringVar()
twoKeys = StringVar()
JackDaniels = StringVar()
Maheu = StringVar()
Vodka = StringVar()
Royalty = StringVar()
JonnyWalker = StringVar()
RussianBeer = StringVar()
Chateu = StringVar()
Cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()
#----------------------------------------------------------------------------------------



lblOrderNo = Label(f1,font=('arial',15,'bold'), text='OrderNo', bd=5, anchor='w')              #[1]
lblOrderNo.grid(row=0,column=0)
txtOrderNo = Entry(f1,font=('arial',10,'bold'), textvariable=OrderNo, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtOrderNo.grid(row=0,column=1)

lblPotatoChips = Label(f1,font=('arial',15,'bold'), text='Potato Chips', bd=5, anchor='w')                 #[2]
lblPotatoChips.grid(row=1,column=0)
txtPotatoChips = Entry(f1,font=('arial',10,'bold'), textvariable=PotatoChips, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtPotatoChips.grid(row=1,column=1)

lblSadzaNbeef = Label(f1,font=('arial',15,'bold'), text='Sadza Ne beef', bd=5, anchor='w')
lblSadzaNbeef.grid(row=2,column=0)
txtSadzaNbeef = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNbeef, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNbeef.grid(row=2,column=1)

lblSadzaNemazondo = Label(f1,font=('arial',15,'bold'), text='Sadza Ne mazondo', bd=5, anchor='w')
lblSadzaNemazondo.grid(row=3,column=0)
txtSadzaNemazondo = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNemazondo, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNemazondo.grid(row=3,column=1)

lblSadzaNehuku = Label(f1,font=('arial',15,'bold'), text='Sadza Ne huku', bd=5, anchor='w')              #[1]
lblSadzaNehuku.grid(row=4,column=0)
txtSadzaNehuku = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNehuku, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNehuku.grid(row=4,column=1)

lblSadzaNederere = Label(f1,font=('arial',15,'bold'), text='Sadza Ne derere', bd=5, anchor='w')                 #[2]
lblSadzaNederere.grid(row=5,column=0)
txtSadzaNederere = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNederere, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNederere.grid(row=5,column=1)
#-----------------------------------------far left widgets additions---------------------------------------------------------
lblSadzaRezviyo = Label(f1,font=('arial',15,'bold'), text='Sadza Re zviyo', bd=5, anchor='w')              #[1]
lblSadzaRezviyo.grid(row=6,column=0)
txtSadzaRezviyo = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaRezviyo, bd=5, insertwidth=23,
                     bg='powder blue',justify = 'right')
txtSadzaRezviyo.grid(row=6,column=1)

lblSadzaRemhunga = Label(f1,font=('arial',15,'bold'), text='Sadza Re mhunga', bd=5, anchor='w')                 #[2]
lblSadzaRemhunga.grid(row=7,column=0)
txtSadzaRemhunga = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaRemhunga, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaRemhunga.grid(row=7,column=1)

lblBurger = Label(f1,font=('arial',15,'bold'), text='Burger', bd=5, anchor='w')
lblBurger.grid(row=8,column=0)
txtBurger = Entry(f1,font=('arial',10,'bold'), textvariable=Burger, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtBurger.grid(row=8,column=1)

lblRiceNchicken = Label(f1,font=('arial',15,'bold'), text='Rice and chicken', bd=5, anchor='w')
lblRiceNchicken.grid(row=9,column=0)
txtRiceNchicken = Entry(f1,font=('arial',10,'bold'), textvariable=RiceNchicken, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtRiceNchicken.grid(row=9,column=1)

lblRiceNbeef = Label(f1,font=('arial',15,'bold'), text='Rice and beef', bd=5, anchor='w')              #[1]
lblRiceNbeef.grid(row=15,column=0)
txtRiceNbeef = Entry(f1,font=('arial',10,'bold'), textvariable=RiceNbeef, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtRiceNbeef.grid(row=15,column=1)

lblCheese = Label(f1,font=('arial',15,'bold'), text='Cheese', bd=5, anchor='w')                 #[2]
lblCheese.grid(row=11,column=0)
txtCheese = Entry(f1,font=('arial',10,'bold'), textvariable=Cheese, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtCheese.grid(row=11,column=1)
#-----------------------------------------far left widgets additions two---------------------------------------------------------
lblSadzaNfish = Label(f1,font=('arial',15,'bold'), text='Sadza Ne fish', bd=5, anchor='w')              #[1]
lblSadzaNfish.grid(row=12,column=0)
txtSadzaNfish = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNfish, bd=5, insertwidth=23,
                     bg='powder blue',justify = 'right')
txtSadzaNfish.grid(row=12,column=1)

lblCoffe = Label(f1,font=('arial',15,'bold'), text='Coffe', bd=5, anchor='w')                 #[2]
lblCoffe.grid(row=13,column=0)
txtCoffe = Entry(f1,font=('arial',10,'bold'), textvariable=Coffe, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtCoffe.grid(row=13,column=1)

lblSadzaNmufushwa = Label(f1,font=('arial',15,'bold'), text='Sadza and mufushwa', bd=5, anchor='w')
lblSadzaNmufushwa.grid(row=14,column=0)
txtSadzaNmufushwa = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNmufushwa, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNmufushwa.grid(row=14,column=1)

lblSadzaNmubora = Label(f1,font=('arial',15,'bold'), text='Sadza and mubora ', bd=5, anchor='w')
lblSadzaNmubora .grid(row=15,column=0)
txtSadzaNmubora  = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNmubora, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNmubora .grid(row=15,column=1)

lblSadzaNnzungu = Label(f1,font=('arial',15,'bold'), text='Sadza Ne nzungu', bd=5, anchor='w')              #[1]
lblSadzaNnzungu.grid(row=16,column=0)
txtSadzaNnzungu = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNnzungu, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNnzungu.grid(row=16,column=1)

lblSadzaNbakayawo = Label(f1,font=('arial',15,'bold'), text='Sadza Ne bakayawo', bd=5, anchor='w')                 #[2]
lblSadzaNbakayawo.grid(row=17,column=0)
txtSadzaNbakayawo = Entry(f1,font=('arial',10,'bold'), textvariable=SadzaNbakayawo, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSadzaNbakayawo.grid(row=17,column=1)

#=================================middle widgets================================================================

lblScud = Label(f1,font=('arial',15,'bold'), text='Scud', bd=5, anchor='w')              #[1]
lblScud.grid(row=0,column=2)
txtScud = Entry(f1,font=('arial',10,'bold'), textvariable=Scud, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtScud.grid(row=0,column=3)

lblNgoda = Label(f1,font=('arial',15,'bold'), text='Ngoda', bd=5, anchor='w')                 #[2]
lblNgoda.grid(row=1,column=2)
txtNgoda = Entry(f1,font=('arial',10,'bold'), textvariable=Ngoda, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtNgoda.grid(row=1,column=3)

lblSuper = Label(f1,font=('arial',15,'bold'), text='Super', bd=5, anchor='w')
lblSuper.grid(row=2,column=2)
txtSuper = Entry(f1,font=('arial',10,'bold'), textvariable=Super, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSuper.grid(row=2,column=3)

lblLager = Label(f1,font=('arial',15,'bold'), text='Lager', bd=5, anchor='w')
lblLager.grid(row=3,column=2)
txtLager = Entry(f1,font=('arial',10,'bold'), textvariable=Lager, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtLager.grid(row=3,column=3)

lblEagle = Label(f1,font=('arial',15,'bold'), text='Eagle', bd=5, anchor='w')              #[1]
lblEagle.grid(row=4,column=2)
txtEagle = Entry(f1,font=('arial',10,'bold'), textvariable=Eagle, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtEagle.grid(row=4,column=3)

lblWhiskey = Label(f1,font=('arial',15,'bold'), text='Whiskey', bd=5, anchor='w')                 #[2]
lblWhiskey.grid(row=5,column=2)
txtWhiskey = Entry(f1,font=('arial',10,'bold'), textvariable=Whiskey, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtWhiskey.grid(row=5,column=3)
#-----------------------------------------middle widgets additions---------------------------------------------------------
lblBrandy = Label(f1,font=('arial',15,'bold'), text='Brandy', bd=5, anchor='w')              #[1]
lblBrandy.grid(row=6,column=2)
txtBrandy = Entry(f1,font=('arial',10,'bold'), textvariable=Brandy, bd=5, insertwidth=23,
                     bg='powder blue',justify = 'right')
txtBrandy.grid(row=6,column=3)

lblCoke = Label(f1,font=('arial',15,'bold'), text='Coke', bd=5, anchor='w')                 #[2]
lblCoke.grid(row=7,column=2)
txtCoke = Entry(f1,font=('arial',10,'bold'), textvariable=Coke, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtCoke.grid(row=7,column=3)

lblFanta = Label(f1,font=('arial',15,'bold'), text='Fanta', bd=5, anchor='w')
lblFanta.grid(row=8,column=2)
txtFanta = Entry(f1,font=('arial',10,'bold'), textvariable=Fanta, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtFanta.grid(row=8,column=3)

lblSprite = Label(f1,font=('arial',15,'bold'), text='Sprite', bd=5, anchor='w')
lblSprite.grid(row=9,column=2)
txtSprite = Entry(f1,font=('arial',10,'bold'), textvariable=Sprite, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtSprite.grid(row=9,column=3)

lbltwoKeys = Label(f1,font=('arial',15,'bold'), text='2Keys', bd=5, anchor='w')              #[1]
lbltwoKeys.grid(row=15,column=2)
txttwoKeys = Entry(f1,font=('arial',10,'bold'), textvariable=twoKeys, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txttwoKeys.grid(row=15,column=3)

lblJackDaniels = Label(f1,font=('arial',15,'bold'), text='JackDaniels', bd=5, anchor='w')                 #[2]
lblJackDaniels.grid(row=11,column=2)
txtJackDaniels = Entry(f1,font=('arial',10,'bold'), textvariable=JackDaniels, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtJackDaniels.grid(row=11,column=3)
#-----------------------------------------middle widgets additions two---------------------------------------------------------
lblMaheu = Label(f1,font=('arial',15,'bold'), text='Maheu', bd=5, anchor='w')              #[1]
lblMaheu.grid(row=12,column=2)
txtMaheu = Entry(f1,font=('arial',10,'bold'), textvariable=Maheu, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtMaheu.grid(row=12,column=3)

lblVodka = Label(f1,font=('arial',15,'bold'), text='Vodka', bd=5, anchor='w')                 #[2]
lblVodka.grid(row=13,column=2)
txtVodka = Entry(f1,font=('arial',10,'bold'), textvariable=Vodka, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtVodka.grid(row=13,column=3)

lblRoyalty = Label(f1,font=('arial',15,'bold'), text='Royalty', bd=5, anchor='w')
lblRoyalty.grid(row=14,column=2)
txtRoyalty = Entry(f1,font=('arial',10,'bold'), textvariable=Royalty, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtRoyalty.grid(row=14,column=3)

lblJonnyWalker = Label(f1,font=('arial',15,'bold'), text='Jonny Walker', bd=5, anchor='w')
lblJonnyWalker.grid(row=15,column=2)
txtJonnyWalker = Entry(f1,font=('arial',10,'bold'), textvariable=JonnyWalker, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtJonnyWalker.grid(row=15,column=3)

lblRussianBeer = Label(f1,font=('arial',15,'bold'), text='Russian Beer', bd=5, anchor='w')              #[1]
lblRussianBeer.grid(row=16,column=2)
txtRussianBeer = Entry(f1,font=('arial',10,'bold'), textvariable=RussianBeer, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtRussianBeer.grid(row=16,column=3)

lblChateu = Label(f1,font=('arial',15,'bold'), text='Chateu', bd=5, anchor='w')                 #[2]
lblChateu.grid(row=17,column=2)
txtChateu = Entry(f1,font=('arial',10,'bold'), textvariable=Chateu, bd=5, insertwidth=4,
                     bg='powder blue',justify = 'right')
txtChateu.grid(row=17,column=3)

#==========================far right widgets============================================================
lblCost = Label(f2,font=('arial',16,'bold'), text='Cost of Meal', bd=16, anchor='w')                 #[2]
lblCost.grid(row=1,column=2)
txtCost = Entry(f2,font=('arial',16,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                     bg='#ffffff',justify = 'left')
txtCost.grid(row=1,column=3)

lblService = Label(f2,font=('arial',16,'bold'), text='Service Charge', bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService = Entry(f2,font=('arial',16,'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                     bg='#ffffff',justify = 'left')
txtService.grid(row=2,column=3)

lblStateTax = Label(f2,font=('arial',16,'bold'), text='VAT', bd=16, anchor='w')
lblStateTax .grid(row=3,column=2)
txtStateTax  = Entry(f2,font=('arial',16,'bold'), textvariable=Tax, bd=10, insertwidth=4,
                     bg='#ffffff',justify = 'left')
txtStateTax .grid(row=3,column=3)

lblSubtotal = Label(f2,font=('arial',16,'bold'), text='Sub total', bd=16, anchor='w')              #[1]
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f2,font=('arial',16,'bold'), textvariable=Subtotal, bd=10, insertwidth=4,
                     bg='#ffffff',justify = 'left')
txtSubtotal.grid(row=4,column=3)

lblTotalCost = Label(f2,font=('arial',16,'bold'), text='Total Cost', bd=16, anchor='w')                 #[2]
lblTotalCost.grid(row=5,column=2)
txtTotalCost = Entry(f2,font=('arial',16,'bold'), textvariable=Total, bd=10, insertwidth=4,
                     bg='#ffffff',justify = 'left')
txtTotalCost.grid(row=5,column=3)

#============================================buttons===========================================================
def Ref():
    x = random.randint(100,500)
    randomRef = str(x)
    OrderNo.set(randomRef)

    CoChips =float(PotatoChips.get())
    CoSadzaNbeef =float(SadzaNbeef.get())
    CoSadzaNemazondo =float(SadzaNemazondo.get())
    CoSadzaNehuku =float(SadzaNehuku.get())
    CoSadzaNederere =float(SadzaNederere.get())
    CoSadzaRezviyo =float(SadzaRezviyo.get())
    CoSadzaRemhunga =float(SadzaRemhunga.get())
    CoBurger =float(Burger.get())
    CoRiceNchicken =float(RiceNchicken.get())
    CoRiceNbeef =float(RiceNbeef.get())
    CoCheese =float(Cheese.get())
    #-------------------
    CoSadzaNfish =float(SadzaNfish.get())
    CoCoffe =float(Coffe.get())
    CoSadzaNmufushwa =float(SadzaNmufushwa.get())
    CoSadzaNmubora =float(SadzaNmubora.get())
    CoSadzaNnzungu =float(SadzaNnzungu.get())
    CoSadzaNbakayawo =float(SadzaNbakayawo.get())
    CoScud  =float(Scud.get())
    CoNgoda =float(Ngoda.get())
    CoSuper =float(Super.get())
    CoLager =float(Lager.get())
    CoEagle =float(Eagle.get())
    CoWhiskey =float(Whiskey.get())

    CoBrandy =float(Brandy.get())
    CoCoke =float(Coke.get())
    CoFanta =float(Fanta.get())
    CoSprite =float(Sprite.get())
    CotwoKeys =float(twoKeys.get())
    CoJackDaniels =float(JackDaniels.get())
    CoMaheu  =float(Maheu.get())
    CoVodka =float(Vodka.get())
    CoRoyalty =float(Royalty.get())
    CoJonnyWalker =float(JonnyWalker.get())
    CoRussianBeer =float(RussianBeer.get())
    CoChateu =float(Chateu.get())
   

    CostofCoChips = CoChips * 1.0
    CostofCoSadzaNbeef = CoSadzaNbeef * 1.00
    CostofCoSadzaNemazondo = CoSadzaNemazondo * 1.00
    CostofCoSadzaNehuku = CoSadzaNehuku * 1.00
    CostofCoSadzaNederere = CoSadzaNederere * 1.00
    CostofCoSadzaRezviyo = CoSadzaRezviyo * 1.0
    CostofCoSadzaRemhunga = CoSadzaRemhunga * 1.00
    CostofCoBurger = CoBurger * 1.00
    CostofCoRiceNchicken = CoRiceNchicken * 1.00
    CostofCoRiceNbeef = CoRiceNbeef * 1.00
    CostofCoCheese = CoCheese * 1.00
#=====================================================
    CostofCoSadzaNfish = CoSadzaNfish * 1.0
    CostofCoCoffe = CoCoffe * 1.00
    CostofCoSadzaNmufushwa = CoSadzaNmufushwa * 1.00
    CostofCoSadzaNmubora = CoSadzaNmubora * 1.00
    CostofCoSadzaNnzungu = CoSadzaNnzungu * 1.00
    CostofCoSadzaNbakayawo = CoSadzaNbakayawo * 1.0
    CostofCoScud = CoScud * 1.00
    CostofCoNgoda = CoNgoda * 1.00
    CostofCoSuper = CoSuper * 1.00
    CostofCoLager = CoLager * 1.00
    CostofCoEagle = CoEagle * 1.00
    CostofCoWhiskey = CoWhiskey * 10.00
#========================================================
    CostofCoBrandy = CoBrandy * 10.0
    CostofCoCoke = CoCoke * 1.00
    CostofCoFanta = CoFanta * 1.00
    CostofCoSprite = CoSprite * 1.00
    CostofCotwoKeys = CotwoKeys * 15.00
    CostofCoJackDaniels = CoJackDaniels * 25.0
    CostofCoMaheu = CoMaheu * 1.00
    CostofCoVodka = CoVodka * 15.00
    CostofCoRoyalty = CoRoyalty * 15.00
    CostofCoJonnyWalker = CoJonnyWalker * 20.00
    CostofCoRussianBeer = CoEagle * 15.00
    CostofCoChateu = CoChateu * 10.00

    

    CostofMeal = '$', str('%.2f' % (CostofCoChips +  CostofCoSadzaNbeef + CostofCoSadzaNemazondo +
                           CostofCoSadzaNehuku + CostofCoSadzaNederere +CostofCoSadzaRezviyo +
                           CostofCoSadzaRemhunga + CostofCoBurger+ CostofCoRiceNchicken +
                           CostofCoRiceNbeef + CostofCoCheese + CostofCoSadzaNfish +CostofCoCoffe +
                           CostofCoSadzaNmufushwa +CostofCoSadzaNmubora + CostofCoSadzaNnzungu +
                           CostofCoSadzaNbakayawo + CostofCoScud +CostofCoNgoda + CostofCoSuper +
                           CostofCoLager + CostofCoEagle + CostofCoWhiskey + CostofCoBrandy +
                           CostofCoCoke + CostofCoFanta + CostofCoSprite + CostofCotwoKeys +
                           CostofCoJackDaniels + CostofCoMaheu + CostofCoVodka + CostofCoRoyalty +
                           CostofCoJonnyWalker + CostofCoRussianBeer + CostofCoChateu ))

    PayTax = ((CostofCoChips +  CostofCoSadzaNbeef + CostofCoSadzaNemazondo +
                           CostofCoSadzaNehuku + CostofCoSadzaNederere +CostofCoSadzaRezviyo +
                           CostofCoSadzaRemhunga + CostofCoBurger+ CostofCoRiceNchicken +
                           CostofCoRiceNbeef + CostofCoCheese + CostofCoSadzaNfish +CostofCoCoffe +
                           CostofCoSadzaNmufushwa +CostofCoSadzaNmubora + CostofCoSadzaNnzungu +
                           CostofCoSadzaNbakayawo + CostofCoScud +CostofCoNgoda + CostofCoSuper +
                           CostofCoLager + CostofCoEagle + CostofCoWhiskey + CostofCoBrandy +
                           CostofCoCoke + CostofCoFanta + CostofCoSprite + CostofCotwoKeys +
                           CostofCoJackDaniels + CostofCoMaheu + CostofCoVodka + CostofCoRoyalty +
                           CostofCoJonnyWalker + CostofCoRussianBeer + CostofCoChateu ) * 0.15)

    TotalCost = (CostofCoChips +  CostofCoSadzaNbeef + CostofCoSadzaNemazondo +
                           CostofCoSadzaNehuku + CostofCoSadzaNederere +CostofCoSadzaRezviyo +
                           CostofCoSadzaRemhunga + CostofCoBurger+ CostofCoRiceNchicken +
                           CostofCoRiceNbeef + CostofCoCheese + CostofCoSadzaNfish +CostofCoCoffe +
                           CostofCoSadzaNmufushwa +CostofCoSadzaNmubora + CostofCoSadzaNnzungu +
                           CostofCoSadzaNbakayawo + CostofCoScud +CostofCoNgoda + CostofCoSuper +
                           CostofCoLager + CostofCoEagle + CostofCoWhiskey + CostofCoBrandy +
                           CostofCoCoke + CostofCoFanta + CostofCoSprite + CostofCotwoKeys +
                           CostofCoJackDaniels + CostofCoMaheu + CostofCoVodka + CostofCoRoyalty +
                           CostofCoJonnyWalker + CostofCoRussianBeer + CostofCoChateu )

    Ser_Charge = ((CostofCoChips +  CostofCoSadzaNbeef + CostofCoSadzaNemazondo +
                           CostofCoSadzaNehuku + CostofCoSadzaNederere +CostofCoSadzaRezviyo +
                           CostofCoSadzaRemhunga + CostofCoBurger+ CostofCoRiceNchicken +
                           CostofCoRiceNbeef + CostofCoCheese + CostofCoSadzaNfish +CostofCoCoffe +
                           CostofCoSadzaNmufushwa +CostofCoSadzaNmubora + CostofCoSadzaNnzungu +
                           CostofCoSadzaNbakayawo + CostofCoScud +CostofCoNgoda + CostofCoSuper +
                           CostofCoLager + CostofCoEagle + CostofCoWhiskey + CostofCoBrandy +
                           CostofCoCoke + CostofCoFanta + CostofCoSprite + CostofCotwoKeys +
                           CostofCoJackDaniels + CostofCoMaheu + CostofCoVodka + CostofCoRoyalty +
                           CostofCoJonnyWalker + CostofCoRussianBeer + CostofCoChateu )/99)

    Service = '$', str('%.2f' % Ser_Charge)

    overAllCost = '$', str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = '$', str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(overAllCost)
    

def qExit():
    root.destroy()

def Reset():
    OrderNo.set('')
    PotatoChips.set('0')
    SadzaNbeef.set('0')
    SadzaNemazondo.set('0')
    SadzaNehuku.set('0')
    SadzaNederere.set('0')
    SadzaRezviyo.set('0')
    SadzaRemhunga.set('0')
    Burger.set('0')
    RiceNchicken.set('0')
    RiceNbeef.set('0')
    Cheese.set('0')
    #------------------------------------------------------------------------------------------------------------
    SadzaNfish.set('0')
    Coffe.set('0')
    SadzaNmufushwa.set('0')
    SadzaNmubora.set('0')
    SadzaNnzungu.set('0')
    SadzaNbakayawo.set('0')
    Scud.set('0')
    Ngoda.set('0')
    Super.set('0')
    Lager.set('0')
    Eagle.set('0')
    Whiskey.set('0')
    #-------------------------------------------------------------------------------------------------------------------
    Brandy.set('0')
    Coke.set('0')
    Fanta.set('0')
    Sprite.set('0')
    twoKeys.set('0')
    JackDaniels.set('0')
    Maheu.set('0')
    Vodka.set('0')
    Royalty.set('0')
    JonnyWalker.set('0')
    RussianBeer.set('0')
    Chateu.set('0')
    Cost.set('')
    Service_Charge.set('')
    Tax.set('')
    Subtotal.set('')
    Total.set('')
   





btnTotal=Button(f2,padx=16,pady=8, bd=16, fg='black',font=('arial',16,'bold'), width=10,
                text='Total', bg='powder blue',command = Ref ).grid(row=7,column=2)

btnReset=Button(f2,padx=16,pady=8, bd=16, fg='black',font=('arial',16,'bold'), width=10,
                text='Reset', bg='powder blue',command = Reset ).grid(row=8,column=2)

btnExit=Button(f2,padx=16,pady=8, bd=16, fg='black',font=('arial',16,'bold'), width=10,
                text='Exit', bg='powder blue',command = qExit ).grid(row=9,column=2)

root.mainloop()




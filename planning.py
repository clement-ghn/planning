from random import *


cuisinemidi1 = randint(1,9)
cuisinemidi2 = randint(1,9)

vaissellemidi1 = randint(1,9)
vaissellemidi2 = randint(1,9)

cuisinesoir1 = randint(1,9)
cuisinesoir2 = randint(1,9)

vaissellesoir1 = randint(1,9)
vaissellesoir2 = randint(1,9)


if cuisinemidi1 == cuisinemidi2:
    test = randint(1,8)
    cuisinemidi2 = test


if vaissellemidi1 == vaissellemidi2:
    test = randint(1,8)
    vaissellemidi2 = test

if cuisinesoir1 == cuisinesoir2:
    test = randint(1,8)
    cuisinesoir1 = test

if vaissellesoir1 == vaissellesoir2:
    test = randint(1,8)
    vaissellesoir2 = test


if cuisinemidi1 == 1 and cuisinemidi2 == 2 or cuisinemidi2 == 3:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 2 and cuisinemidi2 == 1 or cuisinemidi2 == 3:
    test = randint(1,8)
    cuisinemidi2 = test
if cuisinemidi1 == 3 and cuisinemidi2 == 2 or cuisinemidi2 == 1:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 4 and cuisinemidi2 == 5 or cuisinemidi2 == 6:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 5 and cuisinemidi2 == 4 or cuisinemidi2 == 6:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 6 and cuisinemidi2 == 5 or cuisinemidi2 == 4:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 7 and cuisinemidi2 == 8:
    test = randint(1,8)
    cuisinemidi2 = test

if cuisinemidi1 == 8 and cuisinemidi2 == 7:
    test = randint(1,8)
    cuisinemidi2 = test




if cuisinemidi1 == vaissellemidi1 or cuisinemidi2 == vaissellemidi1:
    test = randint(1,8)
    vaissellemidi1 = test

if cuisinemidi1 == vaissellemidi2 or cuisinemidi2 == vaissellemidi2:
    test = randint(1,)
    vaissellemidi2 = test

if cuisinemidi1 == cuisinesoir1 or cuisinemidi2 == cuisinesoir1 or vaissellemidi1 == cuisinesoir1 or vaissellemidi2 == cuisinesoir1:
    test = randint(1,9)
    cuisinesoir1 = test

if cuisinemidi1 == cuisinesoir2 or cuisinemidi2 == cuisinesoir2 or vaissellemidi1 == cuisinesoir2 or vaissellemidi2 == cuisinesoir2:
    test = randint(1,9)
    cuisinesoir2 = test

if cuisinemidi1 == vaissellesoir1 or cuisinemidi2 == vaissellesoir1 or vaissellemidi1 == vaissellesoir1 or vaissellemidi2 == vaissellesoir1 or cuisinesoir1 == vaissellesoir1 or cuisinesoir2 == vaissellesoir1 :
    test = randint(1,9)
    vaissellesoir1 = test

if cuisinemidi1 == vaissellesoir2 or cuisinemidi2 == vaissellesoir2 or vaissellemidi1 == vaissellesoir2 or vaissellemidi2 == vaissellesoir2 or cuisinesoir1 == vaissellesoir2 or cuisinesoir2 == vaissellesoir2 :
    test = randint(1,9)
    vaissellesoir2 = test






print (" \n cuisine midi")
if cuisinemidi1 == 1:
    print ("clement")

elif  cuisinemidi1 == 2:
    print ("lucas")

elif  cuisinemidi1 == 3:
    print ("romane")

elif  cuisinemidi1 == 4:
    print ("joaquin")

elif  cuisinemidi1 == 5:
    print ("paul")

elif  cuisinemidi1 == 6:
    print ("laurianne")

elif  cuisinemidi1 == 7:
    print ("julien")

elif  cuisinemidi1 == 8:
    print ("adrien")


if cuisinemidi2 == 1:
    print ("clement")

elif  cuisinemidi2 == 2:
    print ("lucas")

elif  cuisinemidi2 == 3:
    print ("romane")

elif  cuisinemidi2 == 4:
    print ("joaquin")

elif  cuisinemidi2 == 5:
    print ("paul")

elif  cuisinemidi2 == 6:
    print ("laurianne")

elif  cuisinemidi2 == 7:
    print ("julien")

elif  cuisinemidi2 == 8:
    print ("adrien")







print (" \n vaiselle midi")
if vaissellemidi1 == 1:
    print ("clement")

elif  vaissellemidi1 == 2:
    print ("lucas")

elif  vaissellemidi1 == 3:
    print ("romane")

elif  vaissellemidi1 == 4:
    print ("joaquin")

elif  vaissellemidi1 == 5:
    print ("paul")

elif  vaissellemidi1 == 6:
    print ("laurianne")

elif  vaissellemidi1 == 7:
    print ("julien")

elif  vaissellemidi1 == 8:
    print ("adrien")


if vaissellemidi2 == 1:
    print ("clement")

elif  vaissellemidi2 == 2:
    print ("lucas")

elif  vaissellemidi2 == 3:
    print ("romane")

elif  vaissellemidi2 == 4:
    print ("joaquin")

elif  vaissellemidi2 == 5:
    print ("paul")

elif  vaissellemidi2 == 6:
    print ("laurianne")

elif  vaissellemidi2 == 7:
    print ("julien")

elif  vaissellemidi2 == 8:
    print ("adrien")



print ("\n cuisine soir")

if cuisinesoir1 == 1:
    print ("clement")

elif  cuisinesoir1 == 2:
    print ("lucas")

elif  cuisinesoir1 == 3:
    print ("romane")

elif  cuisinesoir1 == 4:
    print ("joaquin")

elif  cuisinesoir1 == 5:
    print ("paul")

elif  cuisinesoir1 == 6:
    print ("laurianne")

elif  cuisinesoir1 == 7:
    print ("julien")

elif  cuisinesoir1 == 8:
    print ("adrien")


if cuisinesoir2 == 1:
    print ("clement")

elif  cuisinesoir2 == 2:
    print ("lucas")

elif  cuisinesoir2 == 3:
    print ("romane")

elif  cuisinesoir2 == 4:
    print ("joaquin")

elif  cuisinesoir2 == 5:
    print ("paul")

elif  cuisinesoir2 == 6:
    print ("laurianne")

elif  cuisinesoir2 == 7:
    print ("julien")

elif  cuisinesoir2 == 8:
    print ("adrien")



print ("\n vaiselle soir")


if vaissellesoir1 == 1:
    print ("clement")

elif  vaissellesoir1 == 2:
    print ("lucas")

elif  vaissellesoir1== 3:
    print ("romane")

elif  vaissellesoir1 == 4:
    print ("joaquin")

elif  vaissellesoir1 == 5:
    print ("paul")

elif  vaissellesoir1 == 6:
    print ("laurianne")

elif  vaissellesoir1 == 7:
    print ("julien")

elif  vaissellesoir1 == 8:
    print ("adrien")


if vaissellesoir2 == 1:
    print ("clement")

elif  vaissellesoir2 == 2:
    print ("lucas")

elif  vaissellesoir2 == 3:
    print ("romane")

elif  vaissellesoir2 == 4:
    print ("joaquin")

elif  vaissellesoir2 == 5:
    print ("paul")

elif  vaissellesoir2 == 6:
    print ("laurianne")

elif  vaissellesoir2 == 7:
    print ("julien")

elif  vaissellesoir2 == 8:
    print ("adrien")


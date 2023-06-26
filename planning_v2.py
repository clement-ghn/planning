from random import sample

liste = ["paul", "laurianne", "lucas", "clement", "adrien", "julien", "romane", "jaquin"]

for i in range (7):
    while True:
        tirage = sample(liste, 8)
        if tirage[0] != "paul" and tirage[1] != "laurianne" or tirage[1] != "paul" and tirage[0] != "laurianne" or tirage[1] != "paul" and tirage[0] != "jaquin" or tirage[0] != "paul" and tirage[1] != "jaquin" or tirage[0] != "julien" and tirage[1] != "adrien" or tirage[1] != "julien" and tirage[0] != "adrien" or tirage[0] != "laurianne" and tirage[1] != "jaquin" or tirage[1] != "laurianne" and tirage[0] != "jaquin" or tirage[0] != "clement" and tirage[1] != "lucas" or tirage[1] != "clement" and tirage[2] != "lucas" or tirage[0] != "clement" and tirage[1] != "romane" or tirage[1] != "clement" and tirage[0] != "romane" or tirage[0] != "lucas" and tirage[1] != "romane" or tirage[1] != "lucas" and tirage[0] != "romane":
            break

    print ("\ncuisine midi :")
    print(tirage[0], tirage[1])
    print ("\nvaisselle midi :")
    print(tirage[2], tirage[3])
    print ("\ncuisine soir :")
    print(tirage[4], tirage[5])
    print ("\nvaisselle soir :")
    print(tirage[6], tirage[7])
    print("\n\n\n\n")
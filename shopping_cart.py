class Shopping_cart :
    Leather_wallet = 1100*5/100
    Umbrella = 900*5/100
    cigarette = 200*3
    honey = 100*2

    GLeather = Leather_wallet * 18/100
    GUmnrella = Umbrella * 12/100
    GCigarette = cigarette * 28/100
    GHoney = honey

    GSTlist = []
    GSTLeather = Leather_wallet - GLeather
    GSTUmbrella = Umbrella - GUmnrella
    GSTCigarette = cigarette - GCigarette

    totLeather = Leather_wallet + GLeather
    totUmbrella = Umbrella + GUmnrella
    totCigarette = cigarette + GCigarette
    tothoney = honey

    total_amount = totLeather + totCigarette + tothoney + totUmbrella


    GSTlist.append(GSTCigarette)
    GSTlist.append(GSTUmbrella)
    GSTlist.append(GSTLeather)

    print("The maximum amount of product Cigarette is ",max(GSTlist))
    print("Total amount to be paid is: ", total_amount)


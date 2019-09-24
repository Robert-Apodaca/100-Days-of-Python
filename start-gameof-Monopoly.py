def start_game(numberofplayers):
    numberofplayers = int(numberofplayers)
    for i in range(numberofplayers):

        #initialize player bank accounts, location and properties owned.
        playerreference = 1 + i

        x = "Player" + str(playerreference)
        print(x)
        accountname = x + "bank"
        print(accountname)
        accountname = 1500
        locationname = x + "location"
        print(locationaname)
        locationame = 0
        properties_ownedname = x + "properties_owned"
        print(properties_ownedname)
        properties_ownedname = []


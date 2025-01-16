import requests

def get_data(url):
    return requests.get(url)

def menu():
    print("Choix de l'OP")
    print("1. NRJ Mobile")
    print("2. Auchan Telecom")
    #print("3. CDiscount Mobile") CDiscount à un site bizarre, je cherche le paterne
    print("4. Quitter")
    choix = input("Votre choix : ")
    return choix

def check_nrj():
    list_ok_5g = []
    list_ok_4g = []
    for i in range(10,1000,10):
        url5g=f"https://www.nrjmobile.fr/forfait-se/forfait-woot-{i}-go-5g-sans-engagement-0"
        #5g
        response = get_data(url5g)
        if response.status_code == 200:
            print(f"{i} Go 5G : OK")
            list_ok_5g.append(i)
        else:
            print(f"{i} Go 5G: KO")
    for i in range(10,1000,10):
        url4g=f"https://www.nrjmobile.fr/forfait-se/forfait-woot-{i}-go-sans-engagement-0"
        #5g
        response = get_data(url4g)
        if response.status_code == 200:
            print(f"{i} Go 4G : OK")
            list_ok_4g.append(i)
        else:
            print(f"{i} Go 4G: KO")
        
    print("Liste des forfaits 4G NRJ Mobile : ", list_ok_4g)
    print("Liste des forfaits 5G NRJ Mobile : ", list_ok_5g)

def check_auchan():
    list_ok_5g = []
    list_ok_4g = []
    for i in range(10,1000,10):
        url5g=f"https://www.auchantelecom.fr/forfait-se/auchan-telecom-{i}-go-5g-sans-engagement"
        #5g
        response = get_data(url5g)
        if response.status_code == 200:
            print(f"{i} Go 5G : OK")
            list_ok_5g.append(i)
        else:
            print(f"{i} Go 5G: KO")
    for i in range(10,1000,10):
        url4g=f"https://www.auchantelecom.fr/forfait-se/auchan-telecom-{i}-go-sans-engagement"
        #5g
        response = get_data(url4g)
        if response.status_code == 200:
            print(f"{i} Go 4G : OK")
            list_ok_4g.append(i)
        else:
            print(f"{i} Go 4G: KO")
        
    print("Liste des forfaits 4G Auchan Telecom : ", list_ok_4g)
    print("Liste des forfaits 5G Auchan Telecom : ", list_ok_5g)

def main():
    choix = menu()
    if choix == '1':
        check_nrj()
    elif choix == '2':
        check_auchan()
    #elif choix == '3':
    #    check_cdiscount()
    elif choix == '4':
        exit()
    else:
        print("Erreur de saisie")
        main()

main()
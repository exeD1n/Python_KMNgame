import random

KMN = ["Камень", "Бумага", "Ножницы"]

def SiSL(client, machine):
    while True:
        try:
            clientKMN = input("Впишите карту которой играете: ")
            random_index = random.randint(0,len(KMN)-1)
            print(f"Машина выбрала: {KMN[random_index]} а вы выбрали: {clientKMN}")

            if clientKMN=="Камень" and KMN[random_index]=="Бумага":
                machine += 1
            elif clientKMN=="Камень" and KMN[random_index]=="Ножницы":
                client += 1
            elif clientKMN=="Бумага" and KMN[random_index]=="Камень":
                client += 1
            elif clientKMN=="Бумага" and KMN[random_index]=="Ножницы":
                machine += 1
            elif clientKMN=="Ножницы" and KMN[random_index]=="Камень":
                machine += 1
            elif clientKMN=="Ножницы" and KMN[random_index]=="Бумага":
                client += 1
            elif clientKMN==KMN[random_index]:
                machine = machine
                client = client

            print(f"ВЫ {client} : РМ {machine}\n")
            
        except ValueError:
            print("Ну это бан")
    
if __name__ == "__main__":
    SiSL(0,0)
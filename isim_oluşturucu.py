import random
def generate_name():
    first_names = ["Ozan", "Ali", "Ayşe", "Mert", "Fatma", "Zeynep", "Pınar", "Kemal", "Umut", "Gürcan"]

    last_names = ["Öztürk", "Yılmaz" "Ödemiş", "Korkmaz", "Özkan", "Güngör", "Mercan", "Tunç", "Orhan"]
    return "{} {}".format(random.choice(first_names),random.choice(last_names))

for i in range(10):
    print(generate_name())

import time

class ServerQueue:
    # vytvoreni prazdnych bloku pro vstupy
    def __init__(self):
        self.request_queue = []  # prazdna fronta pro pozadavky /empty/
        self.statistika = []  #kostra pro statistiky /empty/

    def add_request(self, user, priority, data):
        timestop = time.time()  # aktualni cas
        
        request = (priority, timestop, user, data)
        # tuple priority, casu, , uzivatele, obsahu

        self._add_to_priority_queue(request)
        # požadavek do vlastni fronty dle zadani

        self.statistika.append(request)
        # ulozeni do statistiky /bude volba 3 - neprehodit!!!!!!!!!!!!!!!!!!!!!!/

    def _add_to_priority_queue(self, request):
    #pridani pozadavku do spravne fronty-dokoncit podminky!!!!!!! - /////dokonceno-funguje/////
        priority = request[0]
        if not self.request_queue:
            self.request_queue.append(request)

        else:
            vlozeno = False
            for i in range(len(self.request_queue)):
                if priority < self.request_queue[i][0]:
                    self.request_queue.insert(i, request)

                    vlozeno = True

                    break

            if not vlozeno:
                self.request_queue.append(request)

    def process_request(self):

        if not self.request_queue:
            print("Žádný požadavek v procesu.")
            return None

        request = self.request_queue.pop(0)  # pro zmenu polozky ve fronte - testovat!!!-//////ok-nemenit//////

        priority, timestamp, user, data = request

        print(f"Požadavek {user} s prioritou {priority}")

        return request

    def print_statistics(self):
        print("Vyvolat statistiku.")

        for priority, timestamp, user, data in self.statistika:
            #u času jsem si musel nechat poradit. neznal jsem zapis casu.
            print(f": {user}, Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}, Priority: {priority}, Data: {data}")

def main():
    server_queue = ServerQueue()

    while True:
        print("\nServer menu:")
        print("1. Přidat:")
        print("2. Request:")
        print("3. Statistiky:")
        print("4. Ukončit")

        choice = input("Vyberte možnost 1-4: ")

        if choice == '1':
            user = input("User name: ")
            priority = int(input("Priority: "))
            data = input("Data: ")
            server_queue.add_request(user, priority, data)
            print("Added.")

        elif choice == '2':
            server_queue.process_request()

        elif choice == '3':
            server_queue.print_statistics()

        elif choice == '4':
            print("Ukončování")
            break

        else:
            print("Nevalidní hodnota. Vyberte 1-4.")

if __name__ == "__main__":
    main()

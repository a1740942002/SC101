class Restaurant:
    def __init__(self, common_ingredient, soup_meat, rice_meat):
        self.c = common_ingredient
        self.s = soup_meat
        self.r = rice_meat

    def give_me_a_soup(self):
        return f"{self.c}{self.s}湯"

    def give_me_a_rice(self):
        return f"{self.c}{self.r}炒飯"



class VIPRestaurant(Restaurant):
    def __init__(self, food1, food2, food3, food4):
        super().__init__(food1, food2, food3)
        self.f4 = food4


    def give_me_hidden_menu(self):
        print(f"{self.f4}燒烤")
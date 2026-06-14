from restaurant import Restaurant, VIPRestaurant


def main():
    r1 = Restaurant("玉米", "培根", "豬肉")
    print(r1.give_me_a_soup()) # 玉米培根湯
    print(r1.give_me_a_rice()) # 玉米豬肉炒飯

    r2 = Restaurant("青菜", "豆腐", "蝦仁")
    print(r2.give_me_a_soup()) # 青菜豆腐湯
    print(r2.give_me_a_rice()) # 青菜蝦仁炒飯

    vip = VIPRestaurant("蘑菇", "龍蝦", "松露", "A5 和牛")
    vip.give_me_hidden_menu()



if __name__ == "__main__":
    main()
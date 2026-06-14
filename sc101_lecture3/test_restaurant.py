from restaurant import Restaurant


def test_restaurant():
    r1 = Restaurant("玉米", "培根", "豬肉")
    assert r1.give_me_a_soup() == "玉米培根湯"
    assert r1.give_me_a_rice() == "玉米豬肉炒飯"

    r2 = Restaurant("青菜", "豆腐", "蝦仁")
    assert r2.give_me_a_soup() == "青菜豆腐湯"
    assert r2.give_me_a_rice() == "青菜蝦仁炒飯"

    print("所有測試通過!")


if __name__ == "__main__":
    test_restaurant()

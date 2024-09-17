def get_reward(times):
    if times <= 10:
        print("Gratulujeme, vyhráváš auto!")
    elif 10 < times <= 25:
        print("Gratulujeme, vyhráváš druhou cenu!")
    elif 25 < times <= 50:
        print("Gratulujeme, vyhráváš třetí cenu!")
    else:
        print("Zkus to jindy...")

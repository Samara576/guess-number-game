import random

def guess_the_number():
    print("Салам! Мен 1ден 100гө чейинки бир санды жашырдым.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Кайсы сан деп ойлойсуң? "))
            attempts += 1
            if guess < secret_number:
                print("Тапкан саның өтө кичине. Кайра аракет кыл.")
            elif guess > secret_number:
                print("Тапкан саның өтө чоң. Кайра аракет кыл.")
            else:
                print(f"Куттуктайм! Сен {attempts} аракет менен таптың!")
                break
        except ValueError:
            print("Санды туура тер! Тамга эмес.")

if __name__ == "__main__":
    guess_the_number()

def find_ans(ans_str):
    if 'y' in ans_str or 'Y' in ans_str or 'Yes' in ans_str or 'yes' in ans_str:
        return True
    elif 'n' in ans_str or 'N' in ans_str or 'No' in ans_str or 'no' in ans_str:
        return False

class profile:
    def __init__(self):
        self.name = input("type your name here :")
        self.age = input("type your age here :")
        self.bir_str = input("have your birthday has passed?(Yes|No) :")


class person_data(profile):
    def introduce(self):
        line = "="*20
        print(f"\n{line}\nHello! {self.name}!\n{line}\n")
    
    def international_age(self):
        find_ans(self.bir_str)
        if find_ans:
            print(f"\nyour international age is {int(self.age)-1}!")
        else:
            print(f"\nAnd your international age is {int(self.age)-2}!")


if __name__ == "__main__":
    p1 = person_data()
    p1.introduce()
    bool_val = find_ans(input("Do you want to know your international age?(Yes|No) :"))
    if bool_val:
        p1.international_age()
    else:
        print("Okay! Good bye :)")
        

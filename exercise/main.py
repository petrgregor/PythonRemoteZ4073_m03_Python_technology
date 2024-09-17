import c
import a.a2.hello as hello  # voláme hello.hello()
#from a.a2.hello import *   # voláme hello()
from b.random_number_generator import generate_number_between, generate_until_drawn
from a import try_again
from a.a1.number_generator import *


#def try_again():
#    return False


def thank_you():
    print("Děkujeme za hru.")


def lotto():
    """

    :return:
    """
    playing = True
    hello.hello()
    #hello()

    while playing:
        number = c.retrieve_number_from_user()
        times = generate_until_drawn(number, 1, 100)
        #print(f"times = {times}")
        c.inform_about_the_result(times)
        c.get_reward(times)
        playing = try_again()

    thank_you()


if __name__ == "__main__":
    lotto()

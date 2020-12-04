from file import double


def test_double():
    assert double(2) == 4


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print(
            "Oops!  That was no valid number.  That was no valid number.  That was no valid number.  That was no valid number.  Try again..."
        )

    the_next_funct()
    print("a thing")


def isPalindrome(nr):
    """
    Determina daca un numar este palindrom.
    :param nr: nr intreg
    :return: Returneaza True daca numarul este palindrom sau False in caz contrar.
    """
    nrNou = 0
    cop = nr
    if nr < 10:
        return True
    else:
        while cop > 0:
            nrNou = nrNou * 10 + cop % 10
            cop = cop // 10
    if nr == nrNou:
        return True
    return False

assert isPalindrome(12) is False
assert isPalindrome(121) is True
assert isPalindrome(12344321) is True

def isPrime(nr):
    """
    Determina daca un numar este prim
    :param nr: nr intreg
    :return: True daca numarul este prim sau False in caz contrar.
    """
    if nr < 2:
        return False
    else:
        for i in range(2,nr // 2 + 1):
            if nr % i == 0:
                return False
    return True

assert isPrime(12) is False
assert isPrime(2) is True
assert isPrime(13) is True

def isSuperPrime(nr):
    """
    Determina daca un numar este superprim.
    :param nr: nr intreg
    :return: True daca numarul este superprim sau False in caz contrar.
    """
    while nr > 0:
        if not isPrime(nr):
            return False
        nr = nr // 10
    return True

assert isSuperPrime(233) is True
assert isSuperPrime(237) is False
assert isSuperPrime(239) is True


def main():

    while True:

        print("1.Determinat daca un numar este palindrom.")
        print("2.Determinati daca un numar este super prim.")
        print("3.Iesire")

        optiune = input("Selectati optiune: ")

        if optiune == "1":
            nr = int(input("Introduceti numar: "))
            print(isPalindrome(nr))
        elif optiune == "2":
            nr2 = int(input("Introduceti numar: "))
            print(isSuperPrime(nr2))
        elif optiune == "3":
            break
        else:
            print("Optiune gresita! Va rugam selectati alta optiune.")


if __name__ == '__main__':
    main()



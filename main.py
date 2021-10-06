
def is_palindrome(nr) -> bool:
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


def test_is_palindrome():
    assert is_palindrome(12) is False
    assert is_palindrome(121) is True
    assert is_palindrome(12344321) is True

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

def is_superprime(nr):
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


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(239) is True


def is_antipalindrome(n) -> bool:
    l = []
    m = 0
    cn = n
    while cn > 0:
        l.append(cn % 10)
        m = m + 1
        cn = cn // 10
    if m % 2 == 1:
        for i in range(0, m // 2 ):
            if l[i] == l[m - i - 1]:
                return False
    else:
        for i in range(0, m // 2):
            if l[i] == l[m - i - 1]:
                return False
    return True


def test_is_antipalindrome():
    assert is_antipalindrome(2783) is True
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(12345) is True


def main():

    test_is_superprime()
    test_is_palindrome()
    test_is_antipalindrome()

    while True:

        print("1.Determinat daca un numar este palindrom.")
        print("2.Determinati daca un numar este super prim.")
        print("3.Determinati daca un numar este antipalindrom.")
        print("4.Iesire")

        optiune = input("Selectati optiune: ")

        if optiune == "1":
            nr = int(input("Introduceti numar: "))
            print(isPalindrome(nr))
        elif optiune == "2":
            nr2 = int(input("Introduceti numar: "))
            print(isSuperPrime(nr2))
        elif optiune == "3":
            nr3 = int(input("Introduceti numar: "))
            print(isAntipalindrome(nr3))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Va rugam selectati alta optiune.")


if __name__ == '__main__':
    main()



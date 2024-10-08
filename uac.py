from pyautogui import click
def main():
    a = input("how many times to click?: ")
    if a.isalpha():
        print("Please Enter An Integer")
        main()
    a = int(a)
    b = input("LMB or RMB?: ").lower()
    if b == "lmb":
        for i in range(a):
            click()
            print(f"Click: {b}, count:{i + 1}")
    elif b == "rmb":
        for i in range(a):
            click(button="right")
            print(f"Click: {b}, count:{i + 1}")
    else:
        print("oops please try again")
        main()
    main()
main()
from os import system
def main():
    system("pip install pyautogui > nul 2>&1")
    a = input("how many times to click?: ")
    from pyautogui import click
    if a.isalpha():
        print("Please Enter An Integer")
    main()
    b = input("LMB or RMB?: ").lower()
    if b == "LMB":
        for i in range(a):
            print(f"Click: {b}, count:{i}")
            click()
    elif b == "RMB":
        for i in range(a):
            click(button="right")
            print(f"Click: {b}, count:{i}")
    else:
        print("oops please try again")
        main()
    print("Done autoclicking")
    main()
main()
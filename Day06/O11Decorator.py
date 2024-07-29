
def outerFun(fnc):

    def helper(amt):
        print("Logging into server......")
        fnc(amt)
        print("Logging out of server........")
        print("-" * 60)

    return helper

@outerFun       #deposit = outerFun(deposit)
def deposit(amt):
    print(f"credited {amt} into account ending ####")


deposit(85000)

@outerFun
def withDraw(amt):
    print(f"Debited {amt} from the account ending ####")

withDraw(30000)






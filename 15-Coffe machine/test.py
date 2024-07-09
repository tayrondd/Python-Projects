

def main(key):
    print('hello')
    return False

answer = input("say something ")
print(type(answer))
if answer == "yei" or answer ==  "ok":
    if main(key=1) == False:
        print('lol')
else:
    print("wrong")



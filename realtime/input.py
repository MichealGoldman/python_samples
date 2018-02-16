
def firstArg():
    print("\tPlease choose environment to push to:\n")
    print("\t1 - Production")
    print("\t2 - QA")
    return getFirstResponse()


def secondArg():
    print("\tEnter full path to file\n")
    return getSecondResponse()
    

def getFirstResponse():
    try:
        env = int(raw_input(""))
        if env == 1:
            print("\tYou chose PROD")
        elif env == 2:
            print("\tYou chose QA")
        else:
            print("\tYou entry is invalid")
            return env
    except Exception as e:
        print("\tInvalid Response")


def getSecondResponse():
        try:
            path = str(raw_input(""))
            if path == "" or path == " ":
                print("\tYou entry is invalid")
            else:
                return path
        except Exception as e:
            print("\tInvalid Response")


if __name__ == "__main__":
    x = firstArg()
    y = secondArg()
    print("\n\tChoices are:")
    print("\t{}".format(x))
    print("\t{}".format(y))
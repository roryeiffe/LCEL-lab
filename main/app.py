from lab.lab import basic_chain_invoke, final_chain_invoke

def main():
    print("===============================================================")
    print("| What would you like to do?                                  |")
    print("| 1 - Learn about a topic                                     |")
    print("| 2 - Find similar movie                                      |")
    print("===============================================================")
    x = int(input("=> "))
    if x == 1:
        print(basic_chain_invoke(input("Enter a topic=> ")))
    elif x == 2:
        print(final_chain_invoke(input("Enter a movie=> ")))
    else:
        print("Not an option, quitting!")
    


if __name__ == "__main__":
    main()

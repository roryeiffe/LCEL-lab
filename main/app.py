from lab.lab import basic_chain

def main():
    topic = input("Enter a topic: ")
    response = basic_chain(topic)
    print(response)
    


if __name__ == "__main__":
    main()
import requests


def get_rand_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers = headers)
    data = response.json()
    joke = data["joke"]
    print(joke)

def main():
    answer = input("would you like to hear a joke? -- type yes or no ")
    while answer == "yes":
        get_rand_joke()
        answer = input("would you like to hear a joke? -- type yes or no ")

if __name__ == "__main__" :
    main()
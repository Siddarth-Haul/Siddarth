

print("Hello World")

myname = "Siddarth"

print(f"Hello {myname}! How are you")

def hello_name(someone):
    print(f"Hello {someone}! This is a funtion.")

def repeat_hello(someone, n_times):
    for i in range(n_times):
        print(f"Hello there {someone}! This is print statement number: {i+1}")

if __name__ == "__main__":
    hello_name("roopa")
    hello_name("function")
    hello_name("soldiers")

    repeat_hello( someone= "roopa the roopeshwari", n_times= 100)
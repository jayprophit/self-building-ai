def add_subscription(user_id, plan):
    with open("public/subscriptions/subscriptions.txt", "a") as f:
        f.write(f"{user_id},{plan}\n")

def get_subscriptions():
    with open("public/subscriptions/subscriptions.txt", "r") as f:
        return f.readlines()

if __name__ == "__main__":
    add_subscription("user123", "premium")
    print(get_subscriptions())
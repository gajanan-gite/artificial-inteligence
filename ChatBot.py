def chatbot():
    print("Welcome to Customer Support Chatbot")
    print("Type 'exit' to end chat\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "exit":
            print("BOT: Thank you, have a great day!")
            break

        elif any(word in user for word in ["hello", "hi", "hii", "hey"]):
            print("BOT: Hello! How can I assist you today?")

        elif "price" in user or "cost" in user:
            print("BOT: Our price range is from ₹500 to ₹5000.")

        elif "product" in user or "items" in user:
            print("BOT: We offer electronics, clothing, and accessories.")

        elif "order" in user or "buy" in user:
            print("BOT: You can place an order on our website.")

        elif "delivery" in user or "shipping" in user:
            print("BOT: Delivery takes 3–4 business days.")

        elif "return" in user or "refund" in user:
            print("BOT: You can return a product within 7 days.")

        elif "payment" in user:
            print("BOT: We accept UPI, credit/debit cards, and net banking.")

        elif "discount" in user or "offer" in user:
            print("BOT: Yes! We have seasonal discounts and offers.")

        elif "contact" in user or "help" in user:
            print("BOT: You can contact us at support@example.com")

        elif "location" in user or "address" in user:
            print("BOT: We are an online store, available all over India.")

        elif "thank" in user:
            print("BOT: You're welcome!")

        else:
            print("BOT: Sorry, I didn't understand. Can you rephrase?")


chatbot()
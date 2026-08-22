import joblib as jb 

spam_pipe=jb.load("model/spam_pred.pkl")
sent_pipe=jb.load("model/sentiment_pre.pkl")

def predict_message(message):
    spam_pred=spam_pipe.predict([message])[0]

    sent_pred=sent_pipe.predict([message])[0]
    sent_prob=sent_pipe.predict_proba([message])[0]

    sentiment_index=list(sent_pipe.classes_).index(sent_pred)
    probability=sent_prob[sentiment_index]

    return {
        "spam": int(spam_pred),
        "sentiment": str(sent_pred),
        "confidence":float(probability)
    }

if __name__ == "__main__":

    while True :

        message=input("Enter the message (exit to quit): ")

        if message.strip().lower() == "exit":
            print("\nProgram over")
            break

        if not message.strip():
            print("please enter a message ") 
            continue

        result = predict_message(message)

        print("\n------------------------------")
        print(f"Message    : {message}")
        print(f"Spam       : {result['spam']}")
        print(f"Sentiment  : {result['sentiment']}")
        print(f"Confidence : {result['confidence']:.2%}")
        print("------------------------------")
import joblib as jb 

spam_pipe=jb.load("model/spam_pred.pkl")
sent_pipe=jb.load("model/sentiment_pre.pkl")


print("======================================")
print("   Spam & Sentiment Classifier")
print("======================================")

while True :
    message=input("\nenter the message (exit for quit ): ")

    if message.strip().lower() == "exit":
        print("\nProgramm over ")
        break

    if not message.strip():
        print("please enter a messsage")
        continue

    spam_pred=spam_pipe.predict([message])[0]
    sent_pred=sent_pipe.predict([message])[0]

    sent_prob=sent_pipe.predict_proba([message])[0]

    sentiment_index = list(sent_pipe.classes_).index(sent_pred)
    probability = sent_prob[sentiment_index]

    print("\n------------------------------")
    print(f"Message   : {message}")
    print(f"Spam      : {spam_pred}")
    print(f"Sentiment : {sent_pred}")
    print(f"Confidence: {probability:.2%}")
    print("------------------------------")


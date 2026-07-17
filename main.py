from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO (r"C:\Users\dell\Desktop\CV projects\UNO deck\runs\detect\UNO_deck-2\weights\best.pt")

    results = model.predict(source = r"C:\Users\dell\Desktop\CV projects\UNO deck\uno deck.mp4", save = True, show = True)
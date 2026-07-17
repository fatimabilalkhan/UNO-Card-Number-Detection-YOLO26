from ultralytics import YOLO

if __name__ == "__main__":

    model = YOLO("yolo26n.pt")


    model.train(
        data=r"C:\Users\dell\Desktop\CV projects\UNO deck\dataset\data.yaml",
        epochs=40,
        imgsz=320,
        batch=8,
        device="cpu",
        name="UNO_deck"
    )

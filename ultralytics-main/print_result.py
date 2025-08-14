from ultralytics import YOLO


if __name__ == "__main__":
    model = YOLO("yolov8n.pt")  # 或你自己的模型
    results = model.val(data="coco8.yaml")

    print(results)

from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("D:/YOLOV8/ultralytics-main/ultralytics-main/ultralytics/cfg/models/v8/yolov8-myCBAM.yaml",verbose=True)
    model.train(data="D:/YOLOV8/ultralytics-main/ultralytics-main/ultralytics/cfg/datasets/african-wildlife.yaml")
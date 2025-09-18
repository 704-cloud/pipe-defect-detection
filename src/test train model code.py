from ultralytics import YOLO
import os


model_path = r"D:\YOLO_results\pipe_defect_yolo21\weights\best.pt"



model = YOLO(model_path)


test_images_folder = r"E:\pipe-defect\test_images"

if not os.path.exists(test_images_folder):
    raise FileNotFoundError(f" {test_images_folder}")


results = model.predict(
    source=test_images_folder,
    conf=0.5,                 
    save=True,                
     
)


for r in results:
    r.show()

import gradio as gr
import cv2
import sys

from ultralytics import YOLO

conversion = float(sys.argv[2])

model = YOLO('best.pt')
path  = [['image_0.jpg'], ['image_1.jpg']]
video_path = [['video.mp4']]

total_area = 0

def show_preds_image(image_path):
    image = cv2.imread(image_path)
    outputs = model.predict(source=image_path)
    results = outputs[0].cpu().numpy()
    for i, det in enumerate(results.boxes.xyxy):
        # print(f"Detected pothole {i}: {det}")
        if i == 0:
            total_area = (conversion * (int(det[2]) - int(det[0]))) * (conversion * (int(det[3]) - int(det[1])))
            print(f"Total area: {total_area}")
        # length in millimeters
        print(f"Length in millimeters: {conversion * (int(det[2]) - int(det[0]))}")
        # height in millimeters
        print(f"Height in millimeters: {conversion * (int(det[3]) - int(det[1]))}")
        cv2.rectangle(
            image,
            (int(det[0]), int(det[1])),
            (int(det[2]), int(det[3])),
            color=(0, 0, 255),
            thickness=2,
            lineType=cv2.LINE_AA
        )
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

show_preds_image(sys.argv[1])

# To view the GUI interface, uncomment the following lines

# inputs_image = [gr.components.Image(type="filepath", label="Input Image"),]
# outputs_image = [gr.components.Image(type="numpy", label="Output Image"),]
# interface_image = gr.Interface(fn=show_preds_image, inputs=inputs_image, outputs=outputs_image,title="Pothole detector app",examples=path,cache_examples=False,)
# gr.TabbedInterface([interface_image],tab_names=['Image inference']).queue().launch()

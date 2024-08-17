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
    if len(results) == 0:
            image_height, image_width, _ = image.shape
            det = [0, 0, image_width/4, image_height/4]
            total_area = (conversion * (int(det[2]) - int(det[0]))) * (conversion * (int(det[3]) - int(det[1])))
            print(f"No pothole detected. Setting length and width to a quarter of the image pixels: {det}")
            print(f"Total area: {total_area}")
    for i, det in enumerate(results.boxes.xyxy):
        
        # print(f"Detected pothole {i}: {det}")
        # if i == 0:
            # total_area = (conversion * (int(det[2]) - int(det[0]))) * (conversion * (int(det[3]) - int(det[1])))
            # Length in millimeters
            # print(f"Length in millimeters: {conversion * (int(det[2]) - int(det[0]))}")
            # Height in millimeters
            # print(f"Height in millimeters: {conversion * (int(det[3]) - int(det[1]))}")

            # print(f"Total area of 1: {total_area}")
        # if i == 1:
            # total_area = (conversion * (int(det[2]) - int(det[0]))) * (conversion * (int(det[3]) - int(det[1])))
            # Length in millimeters
            # print(f"Length in millimeters: {conversion * (int(det[2]) - int(det[0]))}")
            # Height in millimeters
            # print(f"Height in millimeters: {conversion * (int(det[3]) - int(det[1]))}")

            # print(f"Total area of 2: {total_area}")

        bottom_leftmost_x = float('inf')
        bottom_leftmost_y = float('inf')
        top_rightmost_x = float('-inf')
        top_rightmost_y = float('-inf')

        for det in results.boxes.xyxy:
            bottom_leftmost_x = min(bottom_leftmost_x, det[0])
            bottom_leftmost_y = min(bottom_leftmost_y, det[1])
            top_rightmost_x = max(top_rightmost_x, det[2])
            top_rightmost_y = max(top_rightmost_y, det[3])

        total_area = (conversion * (top_rightmost_x - bottom_leftmost_x)) * (conversion * (top_rightmost_y - bottom_leftmost_y))
        # print(f"Total area of combined: {total_area}")
        print(f"Total area: {total_area}")
        # length in millimeters
        # print(f"Length in millimeters: {conversion * (int(det[2]) - int(det[0]))}")
        # height in millimeters
        # print(f"Height in millimeters: {conversion * (int(det[3]) - int(det[1]))}")


        # cv2.rectangle(
        #     image,
        #     (int(38.62),int(113.49)),
        #     (int(388.13),int(348.27)),
        #     color=(0, 0, 255),
        #     thickness=2,
        #     lineType=cv2.LINE_AA
        # )
        
        # cv2.rectangle(
        #     image,
        #     (int(47.72),int(39.664)),
        #     (int(396.57),int(144.62)),
        #     color=(0, 0, 255),
        #     thickness=2,
        #     lineType=cv2.LINE_AA
        # )

        cv2.rectangle(
            image,
            (int(det[0]), int(det[1])),
            (int(det[2]), int(det[3])),
            color=(0, 0, 255),
            thickness=2,
            lineType=cv2.LINE_AA
        )
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# image_path = sys.argv[1]
# image_with_overlay = show_preds_image(image_path)
# cv2.imshow("Image with Overlay", image_with_overlay)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

show_preds_image(sys.argv[1])

# To view the GUI interface, uncomment the following lines

# inputs_image = [gr.components.Image(type="filepath", label="Input Image"),]
# outputs_image = [gr.components.Image(type="numpy", label="Output Image"),]
# interface_image = gr.Interface(fn=show_preds_image, inputs=inputs_image, outputs=outputs_image,title="Pothole detector app",examples=path,cache_examples=False,)
# gr.TabbedInterface([interface_image],tab_names=['Image inference']).queue().launch()

import os
import torch
import logging
from pathlib import Path

# Configure Logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ObjectDetector:
    """
    A class to perform object detection using YOLO.
    """

    def __init__(self, model_weights, image_dir, output_dir):
        self.model = torch.hub.load("ultralytics/yolov5", "custom", path=model_weights)
        self.image_dir = Path(image_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def detect_objects(self):
        """
        Perform object detection on images in the input directory.
        """
        try:
            for image_file in self.image_dir.iterdir():
                if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                    results = self.model(str(image_file))
                    output_path = self.output_dir / f"detected_{image_file.name}"
                    results.save(save_dir=str(output_path.parent))
                    logging.info(
                        f"Processed {image_file.name} and saved results to {output_path}"
                    )
        except Exception as e:
            logging.error(f"Error during object detection: {e}")


if __name__ == "__main__":
    detector = ObjectDetector(
        model_weights="object_detection/yolov5/best.pt",
        image_dir="data/images/",
        output_dir="data/detections/",
    )
    detector.detect_objects()

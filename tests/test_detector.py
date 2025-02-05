import unittest
from unittest.mock import patch
from object_detection.detector import ObjectDetector


class TestObjectDetector(unittest.TestCase):
    @patch("torch.hub.load")
    def test_detect_objects(self, mock_load):
        mock_model = mock_load.return_value
        mock_model.return_value = [{"boxes": [], "labels": [], "scores": []}]

        detector = ObjectDetector(
            model_weights="dummy_path",
            image_dir="data/images/",
            output_dir="data/detections/",
        )
        detector.detect_objects()
        mock_load.assert_called_once()


if __name__ == "__main__":
    unittest.main()

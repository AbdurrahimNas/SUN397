import torch 
import torchvision
from PIL import Image
import matplotlib.pyplot as plt


def get_class_names():
    with open("ClassName.txt", "r") as f:
        class_names = [line.split("/")[2] for line in f.readlines()]
    return class_names
def create_model():
    weights = torchvision.models.ViT_B_16_Weights.IMAGENET1K_SWAG_E2E_V1
    model = torchvision.models.vit_b_16(weights=weights)
    transform = weights.transforms()

    for param in model.parameters():
        param.requires_grad = False
    
    model.heads = torch.nn.Sequential(
        torch.nn.Linear(in_features=768, out_features=397, bias=True)
    )

    return model, transform


def sun_predict(image_path, model_path="./sun397_vit_b_16.pth"):
      
    """
    Predicts on a single image and returns the predicted label.

    Keyword Arguments:
        :arg img_path: Path of the image that would be predicted on.
        :type img_path: str
        :arg model_path: Path of the saved model. Default "./sun397_vit_b_16.pth"
        :type model_path: str

    Example Usage:
        predicted_label = predict(img_path="./img.jpeg",
                              model_path="./sun397_vit_b_16.pth")
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, transform = create_model()
    model.load_state_dict(torch.load(map_location=device, f=model_path))
    model.to(device)
    class_names = get_class_names()
    img = Image.open(image_path)
    transformed_img = transform(img)

    model.eval()
    with torch.inference_mode():
        img_converted = transformed_img.unsqueeze(dim=0)
        img_converted = model(img_converted.to(device))
        pred_label = torch.argmax(torch.softmax(img_converted, dim=1), dim=1)

    return class_names[pred_label].capitalize()

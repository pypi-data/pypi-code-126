__desc__ = "A thin wrapper around keras image classification applications."
__version__ = "0.0.3"

import io
from typing import Tuple, Union

import numpy as np
import PIL as pillow
from tensorflow.keras.applications import *
from tensorflow.keras.applications import VGG16 as _VGG16, VGG19 as _VGG19
from tensorflow.keras.preprocessing.image import img_to_array

XCEPTION = "xception"
VGG16 = "vgg16"
VGG19 = "vgg19"
RESNET50 = "resnet50"
RESNET101 = "resnet101"
RESNET152 = "resnet152"
RESNET50V2 = "resnet50v2"
RESNET101V2 = "resnet101v2"
RESNET152V2 = "resnet152v2"
RESNETRS50 = "resnetrs50"
RESNETRS101 = "resnetrs101"
RESNETRS152 = "resnetrs152"
RESNETRS200 = "resnetrs200"
RESNETRS270 = "resnetrs270"
RESNETRS350 = "resnetrs350"
RESNETRS420 = "resnetrs420"
REGNETX002 = "regnetx002"
REGNETX004 = "regnetx004"
REGNETX006 = "regnetx006"
REGNETX008 = "regnetx008"
REGNETX016 = "regnetx016"
REGNETX032 = "regnetx032"
REGNETX040 = "regnetx040"
REGNETX064 = "regnetx064"
REGNETX080 = "regnetx080"
REGNETX120 = "regnetx120"
REGNETX160 = "regnetx160"
REGNETX320 = "regnetx320"
REGNETY002 = "regnety002"
REGNETY004 = "regnety004"
REGNETY006 = "regnety006"
REGNETY008 = "regnety008"
REGNETY016 = "regnety016"
REGNETY032 = "regnety032"
REGNETY040 = "regnety040"
REGNETY064 = "regnety064"
REGNETY080 = "regnety080"
REGNETY120 = "regnety120"
REGNETY160 = "regnety160"
REGNETY320 = "regnety320"
INCEPTIONV3 = "inceptionv3"
INCEPTIONRESNETV2 = "inceptionresnetv2"
MOBILENET = "mobilenet"
MOBILENETV2 = "mobilenetv2"
MOBILENETV3SMALL = "mobilenetv3small"
MOBILENETV3LARGE = "mobilenetv3large"
DENSENET121 = "densenet121"
DENSENET169 = "densenet169"
DENSENET201 = "densenet201"
NASNETMOBILE = "nasnetmobile"
NASNETLARGE = "nasnetlarge"
EFFICIENTNETB0 = "efficientnetb0"
EFFICIENTNETB1 = "efficientnetb1"
EFFICIENTNETB2 = "efficientnetb2"
EFFICIENTNETB3 = "efficientnetb3"
EFFICIENTNETB4 = "efficientnetb4"
EFFICIENTNETB5 = "efficientnetb5"
EFFICIENTNETB6 = "efficientnetb6"
EFFICIENTNETB7 = "efficientnetb7"
EFFICIENTNETV2B0 = "efficientnetv2b0"
EFFICIENTNETV2B1 = "efficientnetv2b1"
EFFICIENTNETV2B2 = "efficientnetv2b2"
EFFICIENTNETV2B3 = "efficientnetv2b3"
EFFICIENTNETV2S = "efficientnetv2s"
EFFICIENTNETV2M = "efficientnetv2m"
EFFICIENTNETV2L = "efficientnetv2l"

MODULES = {
    XCEPTION: xception,
    VGG16: vgg16,
    VGG19: vgg19,
    RESNET50: resnet50,
    RESNET101: resnet,
    RESNET152: resnet,
    RESNET50V2: resnet_v2,
    RESNET101V2: resnet_v2,
    RESNET152V2: resnet_v2,
    RESNETRS50: resnet_rs,
    RESNETRS101: resnet_rs,
    RESNETRS152: resnet_rs,
    RESNETRS200: resnet_rs,
    RESNETRS270: resnet_rs,
    RESNETRS350: resnet_rs,
    RESNETRS420: resnet_rs,
    REGNETX002: regnet,
    REGNETX004: regnet,
    REGNETX006: regnet,
    REGNETX008: regnet,
    REGNETX016: regnet,
    REGNETX032: regnet,
    REGNETX040: regnet,
    REGNETX064: regnet,
    REGNETX080: regnet,
    REGNETX120: regnet,
    REGNETX160: regnet,
    REGNETX320: regnet,
    REGNETY002: regnet,
    REGNETY004: regnet,
    REGNETY006: regnet,
    REGNETY008: regnet,
    REGNETY016: regnet,
    REGNETY032: regnet,
    REGNETY040: regnet,
    REGNETY064: regnet,
    REGNETY080: regnet,
    REGNETY120: regnet,
    REGNETY160: regnet,
    REGNETY320: regnet,
    INCEPTIONV3: inception_v3,
    INCEPTIONRESNETV2: inception_resnet_v2,
    MOBILENET: mobilenet,
    MOBILENETV2: mobilenet_v2,
    MOBILENETV3SMALL: mobilenet_v3,
    MOBILENETV3LARGE: mobilenet_v3,
    DENSENET121: densenet,
    DENSENET169: densenet,
    DENSENET201: densenet,
    NASNETMOBILE: nasnet,
    NASNETLARGE: nasnet,
    EFFICIENTNETB0: efficientnet,
    EFFICIENTNETB1: efficientnet,
    EFFICIENTNETB2: efficientnet,
    EFFICIENTNETB3: efficientnet,
    EFFICIENTNETB4: efficientnet,
    EFFICIENTNETB5: efficientnet,
    EFFICIENTNETB6: efficientnet,
    EFFICIENTNETB7: efficientnet,
    EFFICIENTNETV2B0: efficientnet_v2,
    EFFICIENTNETV2B1: efficientnet_v2,
    EFFICIENTNETV2B2: efficientnet_v2,
    EFFICIENTNETV2B3: efficientnet_v2,
    EFFICIENTNETV2S: efficientnet_v2,
    EFFICIENTNETV2M: efficientnet_v2,
    EFFICIENTNETV2L: efficientnet_v2,
}

MODELS = {
    XCEPTION: Xception,
    VGG16: _VGG16,
    VGG19: _VGG19,
    RESNET50: ResNet50,
    RESNET101: ResNet101,
    RESNET152: ResNet152,
    RESNET50V2: ResNet50V2,
    RESNET101V2: ResNet101V2,
    RESNET152V2: ResNet152V2,
    RESNETRS50: ResNetRS50,
    RESNETRS101: ResNetRS101,
    RESNETRS152: ResNetRS152,
    RESNETRS200: ResNetRS200,
    RESNETRS270: ResNetRS270,
    RESNETRS350: ResNetRS350,
    RESNETRS420: ResNetRS420,
    REGNETX002: RegNetX002,
    REGNETX004: RegNetX004,
    REGNETX006: RegNetX006,
    REGNETX008: RegNetX008,
    REGNETX016: RegNetX016,
    REGNETX032: RegNetX032,
    REGNETX040: RegNetX040,
    REGNETX064: RegNetX064,
    REGNETX080: RegNetX080,
    REGNETX120: RegNetX120,
    REGNETX160: RegNetX160,
    REGNETX320: RegNetX320,
    REGNETY002: RegNetY002,
    REGNETY004: RegNetY004,
    REGNETY006: RegNetY006,
    REGNETY008: RegNetY008,
    REGNETY016: RegNetY016,
    REGNETY032: RegNetY032,
    REGNETY040: RegNetY040,
    REGNETY064: RegNetY064,
    REGNETY080: RegNetY080,
    REGNETY120: RegNetY120,
    REGNETY160: RegNetY160,
    REGNETY320: RegNetY320,
    INCEPTIONV3: InceptionV3,
    INCEPTIONRESNETV2: InceptionResNetV2,
    MOBILENET: MobileNet,
    MOBILENETV2: MobileNetV2,
    MOBILENETV3SMALL: MobileNetV3Small,
    MOBILENETV3LARGE: MobileNetV3Large,
    DENSENET121: DenseNet121,
    DENSENET169: DenseNet169,
    DENSENET201: DenseNet201,
    NASNETMOBILE: NASNetMobile,
    NASNETLARGE: NASNetLarge,
    EFFICIENTNETB0: EfficientNetB0,
    EFFICIENTNETB1: EfficientNetB1,
    EFFICIENTNETB2: EfficientNetB2,
    EFFICIENTNETB3: EfficientNetB3,
    EFFICIENTNETB4: EfficientNetB4,
    EFFICIENTNETB5: EfficientNetB5,
    EFFICIENTNETB6: EfficientNetB6,
    EFFICIENTNETB7: EfficientNetB7,
    EFFICIENTNETV2B0: EfficientNetV2B0,
    EFFICIENTNETV2B1: EfficientNetV2B1,
    EFFICIENTNETV2B2: EfficientNetV2B2,
    EFFICIENTNETV2B3: EfficientNetV2B3,
    EFFICIENTNETV2S: EfficientNetV2S,
    EFFICIENTNETV2M: EfficientNetV2M,
    EFFICIENTNETV2L: EfficientNetV2L,
}

_loaded_models = {}


def load_model(model: str) -> None:
    global _loaded_models
    if model not in _loaded_models:
        _loaded_models[model] = MODELS[model](
            include_top=True, weights="imagenet", input_tensor=None, input_shape=None
        )


def get_model_target_size(model: str) -> Tuple[int, int]:
    if model == NASNETLARGE:
        return (331, 331)
    elif model in (INCEPTIONV3, XCEPTION, INCEPTIONRESNETV2):
        return (299, 299)
    elif model in (EFFICIENTNETV2B0, EFFICIENTNETV2B1, EFFICIENTNETV2B2, EFFICIENTNETV2B3):
        return (260, 260)
    elif model in (
        EFFICIENTNETB0,
        EFFICIENTNETB1,
        EFFICIENTNETB2,
        EFFICIENTNETB3,
        EFFICIENTNETB4,
        EFFICIENTNETB5,
        EFFICIENTNETB6,
        EFFICIENTNETB7,
    ):
        return (240, 240)
    else:
        return (224, 224)


def preprocess_image(image: pillow.Image.Image, model: str) -> np.ndarray:
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(get_model_target_size(model))
    return MODULES[model].preprocess_input(np.expand_dims(img_to_array(image), axis=0))


def classify(
    image: Union[str, bytes, pillow.Image.Image],
    results: int = 3,
    model: str = INCEPTIONV3,
) -> tuple:
    if results > 5:
        raise ValueError("Keras applications don't give more than five results.")

    if not isinstance(image, pillow.Image.Image):
        if isinstance(image, str):
            to_open = image
        else:
            to_open = io.BytesIO(image)
        image = pillow.Image.open(to_open)
    preprocessed_image = preprocess_image(image, model)

    load_model(model)
    model_object = _loaded_models[model]
    predictions = model_object.predict(preprocessed_image)
    prediction_results = MODULES[model].decode_predictions(predictions)[0]

    return tuple(
        {"imagenet_id": imagenet_id, "label": label, "probability": float(probability)}
        for imagenet_id, label, probability in prediction_results[:results]
    )

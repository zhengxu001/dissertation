import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TENSOR_BOARD = os.path.join(ROOT_DIR, "tensorboard/")

DATASET = os.path.join(ROOT_DIR, "dataset")
CAL101 = os.path.join(ROOT_DIR, "dataset/caltech101")
CAL101_TRAIN = os.path.join(CAL101, "train")
CAL101_VAL = os.path.join(CAL101, "val")

CAL101_TRAIN_WAVE = os.path.join(DATASET, "wave/train")
CAL101_VAL_WAVE = os.path.join(DATASET, "wave/val")

CAL101_TRAIN_SCREAM = os.path.join(DATASET, "scream/train")
CAL101_VAL_SCREAM = os.path.join(DATASET, "scream/val")

CAL101_TRAIN_UDNIE = os.path.join(DATASET, "udnie/train")
CAL101_VAL_UDNIE = os.path.join(DATASET, "udnie/val")

CAL101_TRAIN_LA_MUSE = os.path.join(DATASET, "la_muse/train")
CAL101_VAL_LA_MUSE = os.path.join(DATASET, "la_muse/val")

CAL101_TRAIN_SCREAM_WAVE = os.path.join(DATASET, "scream_wave/train")
CAL101_VAL_SCREAM_WAVE = os.path.join(DATASET, "scream_wave/val")


CAL256 = os.path.join(ROOT_DIR, "dataset/caltech256")
CAL256_TRAIN = os.path.join(CAL256, "train")
CAL256_VAL = os.path.join(CAL256, "val")

CAL256_TRAIN_WAVE = os.path.join(DATASET, "wave256/train")
CAL256_VAL_WAVE = os.path.join(DATASET, "wave256/val")

CAL256_TRAIN_SCREAM = os.path.join(DATASET, "scream256/train")
CAL256_VAL_SCREAM = os.path.join(DATASET, "scream256/val")

CAL256_TRAIN_SCREAM_WAVE = os.path.join(DATASET, "scream_wave256/train")
CAL256_VAL_SCREAM_WAVE = os.path.join(DATASET, "scream_wave256/val")

VALID_EXTS = [".jpg", ".gif", ".png", ".jpeg"]
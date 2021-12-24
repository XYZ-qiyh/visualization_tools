import numpy as np
import cv2
import argparse


def write_normal_img(filename, normal_image):
    normal_image = normal_image / np.linalg.norm(normal_image, axis=2)[:, :, np.newaxis]

    out_normal_image = (((normal_image + 1) / 2) * 255).astype(np.uint8)

    cv2.imwrite(filename, out_normal_image)    
    
# Provided by colmap
def read_array(path):
    with open(path, "rb") as fid:
        width, height, channels = np.genfromtxt(fid, delimiter="&", max_rows=1,
                                                usecols=(0, 1, 2), dtype=int)
        fid.seek(0)
        num_delimiter = 0
        byte = fid.read(1)
        while True:
            if byte == b"&":
                num_delimiter += 1
                if num_delimiter >= 3:
                    break
            byte = fid.read(1)
        array = np.fromfile(fid, np.float32)
    array = array.reshape((width, height, channels), order="F")
    return np.transpose(array, (1, 0, 2)).squeeze()


if __name__ == "__main__":
    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("normal_path")
    args = parser.parse_args()
    normal_path = args.normal_path

    if normal_path.endswith('bin'):
        normal_map = read_array(normal_path)
        normal_map = normal_map * (-1.0)
        print('normal shape: {}'.format(normal_map.shape))
        write_normal_img(normal_path.replace(".bin", ".jpg"), normal_map)


from pathlib import Path
import numpy as np
import cv2

def read_cv2_file(image_path: str, flags: int = cv2.IMREAD_UNCHANGED):
    img = cv2.imdecode(np.fromfile(image_path, np.uint8), flags=flags)
    return img

def run():
    roi_weight = 0.3
    roi_empty=False
    rct_roi = {'x': 27, 'y': 27, 'width': 447, 'height': 447}
    x,y,w,h = rct_roi.get('x'),rct_roi.get('y'),rct_roi.get('width'),rct_roi.get('height')
    roi_path = '/data/annot/666a42dcfb6f7b156a104460/roi.png'
    if Path(roi_path).exists() == True:
        roi = read_cv2_file(roi_path, cv2.IMREAD_COLOR)
        roi = roi.astype(np.float32)
        roi /= 255.0
        roi[np.where(roi==0)] = roi_weight
    else:
        roi = None
        roi_empty=True

    path_src = '/data/project_data/666d3a0507278f1c25eea116/validation/20240704-035405-649/source/raw/images/0-copy-0.png'
    src_cv2 = read_cv2_file(path_src, cv2.IMREAD_COLOR)
    if roi_empty != True and len(src_cv2.shape) > 2 and len(roi.shape) != len(src_cv2.shape):
        roi = cv2.merge((roi, roi, roi))
    if roi_empty!=True and src_cv2.shape == roi.shape:
        src_cv2_roied = cv2.multiply(src_cv2, roi, dtype=cv2.CV_8U)
    else:
        src_cv2_roied = src_cv2
    label_roi = src_cv2_roied
    label = np.zeros(label_roi.shape, dtype='uint8')

    print(label.shape)
    print(label)
    print(label_roi.shape)
    print(label_roi)

    classes = [[251, 184, 99], [94, 236, 254]]
    for i in range(len(classes)):
        label_roi[np.where((label_roi==[i+1,i+1,i+1]).all(axis=2))] = classes[i]
    if x != None and y != None and w != None and h!= None:
        label[y:y+h, x:x+w] = label_roi
    else:
        label = label_roi
    mask = label > 0
    pr = src_cv2_roied.copy()
    pr[mask] = label[mask]
    # write_cv2_file(pr, str(path_img / f'{id}.{img_ext}'))

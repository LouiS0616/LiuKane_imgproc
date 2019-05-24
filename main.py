import logging
import pathlib
import sys

import cv2
import numpy as np


#
#
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler()
_handler.setLevel(logging.DEBUG)
_logger.addHandler(_handler)


#
#
IMG_SUFFIXES = {'.jpg', '.png', '.bmp',}
def is_image(filepath):
    return filepath.suffix in IMG_SUFFIXES    


def gen_overlap_around_view(img, num_of_partitions=16):
    assert img.shape[1] % 16 == 0, '画像サイズが不適'

    head, *tail = np.hsplit(img, 16)
    partitions = [head, *tail, head]

    return map(
        np.hstack, zip(partitions, partitions[1:])
    )


def save_images(imgs, *, form, start=0):
    for i, img in enumerate(imgs):
        dst_path = form.format(no=i)
        cv2.imwrite(dst_path, img)


def maintask(src_dir, dst_dir):
    assert src_dir.is_dir()
    assert dst_dir.is_dir()

    it = filter(
        is_image, src_dir.iterdir()
    )
    for img_path in it:
        img = cv2.imread(f'{img_path.resolve()}')
        assert img is not None, '画像の読み込みに失敗'

        _logger.debug(f'{img_path}を処理中...')
        save_images(
            imgs=gen_overlap_around_view(img),
            form='{dr}/{stem}_{{no:02d}}{ext}'.format(
                dr=dst_dir.resolve(),
                stem=img_path.stem, ext=img_path.suffix
            )
        )


#
#
assert __name__ == '__main__', 'メインモジュール以外の扱いは想定外'

current_dir = pathlib.Path('.').resolve()
src_dir, dst_dir = map(
    lambda p: (current_dir / p).resolve(), (sys.argv + ['.', '.'])[1:3]
)

_logger.debug(f'カレントディレクトリ： {current_dir}')
_logger.debug(f'　　入力ディレクトリ： {src_dir}')
_logger.debug(f'　　出力ディレクトリ： {dst_dir}')

maintask(src_dir, dst_dir)

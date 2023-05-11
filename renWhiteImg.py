import argparse
import os
import PIL
from PIL import Image
# from plyer import notification

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='Process multiple files')
parser.add_argument('files', nargs='+', help='Path to the input files')
args = parser.parse_args()

# ファイルを処理する
for file_path in args.files:
    print('Processing file:', file_path)

    try:
        # 画像の読み込み
        image = Image.open(file_path)
    except PIL.UnidentifiedImageError:
        print('Skip: unsupported format:', file_path)
        continue

    # 白い画像を生成する
    width, height = image.size
    white_image = Image.new('RGB', (width, height), (255, 255, 255))

    # 上書き保存する
    white_image.save(file_path)

    # 元のファイル名に'(2)'を追加して保存する
    # file_name, file_ext = os.path.splitext(file_path)
    # new_file_path = file_name + ' (2)' + file_ext
    # white_image.save(new_file_path)

py_name = os.path.basename(__file__)
# notification.notify(title = py_name, message="Done", timeout=5)

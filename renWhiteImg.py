import argparse
import os
import PIL
from PIL import Image
# from plyer import notification

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='Process multiple files')
parser.add_argument('files', nargs='+', help='Path to the input files')
parser.add_argument('--mode', help='Add: Make a new image, Overwrite, PNG: Save to png format', default='Overwrite')
args = parser.parse_args()

# ファイルを処理する
for file_path in args.files:
    print('Processing file:', file_path)

    # 画像の読み込み
    try:
        image_file = Image.open(file_path)
    except PIL.UnidentifiedImageError:
        print('Skip: unsupported format:', file_path)
        continue
    file_name, file_ext = os.path.splitext(file_path)

    # 白い画像を生成する
    width, height = image_file.size
    white_image = Image.new('RGB', (width, height), (255, 255, 255))

    match args.mode:
        case "Overwrite":
            # 上書き保存する
            white_image.save(file_path)
        case "PNG":
            # PNGで保存して元ファイルは削除する
            white_image.save(file_name + '.png')
            image_file.close()
            if not file_ext == '.png':
                os.remove(file_path)
        case "Add":
            # 元のファイル名に'(2)'を追加して保存する
            new_file_path = file_name + ' (2)' + '.png'
            white_image.save(new_file_path)

py_name = os.path.basename(__file__)
# notification.notify(title = py_name, message="Done", timeout=5)

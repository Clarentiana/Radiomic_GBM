import os
import pydicom

img_root_dir = r"/Users/clarence/Documents/ETP.st/GBM_data/MRI_used/ETP/0740672_YangYinHai/MR"
save_dir_suffix = "_mask"  # 存储脱敏的dicom文件目录后缀

# 获取MR文件夹下的所有子文件夹
subdirs = [x for x in os.listdir(img_root_dir) if os.path.isdir(os.path.join(img_root_dir, x))]

# 遍历子文件夹
for subdir in subdirs:
    img_dir = os.path.join(img_root_dir, subdir)  # 获取DICOM图像存储的子目录
    save_dir = os.path.join(img_root_dir, subdir + save_dir_suffix)  # 获取脱敏后的DICOM图像存储的子目录
    os.makedirs(save_dir, exist_ok=True)  # 如果目录不存在，则创建

    # 遍历DICOM图像
    for img_name in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_name)
        print("img name:", img_name)

        ds = pydicom.dcmread(img_path, force=True)  # 读取Dicom文件信息说明
        print('ds:\n', ds)

        # 数据脱敏
        ds.PatientName = "xxx"  # 姓名
        ds.PatientID = "0000"  # id

        print("ds mask:\n", ds)

        # 保存脱敏后的数据
        save_path = os.path.join(save_dir, img_name)
        ds.save_as(save_path)

        # 删除原始文件
        os.unlink(img_path)

    # 删除原始文件夹
    os.rmdir(img_dir)

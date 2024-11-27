import os
import sys
from XrayClassification.exception.exception import XRayException

## Đồng bộ data Hệ thống và AWS S3
class S3Operation():
    '''
    folder: Đường dẫn đến thư mục cục bộ mà bạn muốn đồng bộ hóa.
    bucket_name: Tên của bucket S3 mà bạn muốn đồng bộ hóa dữ liệu lên.
    bucket_folder_name: Tên thư mục trong bucket S3 nơi dữ liệu sẽ được lưu.
    '''
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        try:
            # Sử dung cmd để đồng bộ hóa data từ hệ thống lên AWS S3
            command: str = (
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ "
            )
            os.system(command)
        except Exception as e:
            raise XRayException(e, sys)
    
    def sync_folder_from_s3(self, folder: str, bucket_name: str, bucket_folder_name: str)->None:
        try:
            # Sử dung cmd để đồng bộ hóa data từ AWS S3 về hệ thống
            command: str = (
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder} "
            )
            os.system(command)
        except Exception as e:
            raise XRayException(e, sys)
     
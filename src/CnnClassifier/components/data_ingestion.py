import os
import boto3
# import urllib.request as request
import zipfile
from dotenv import load_dotenv
from CnnClassifier import logger
from CnnClassifier.utils.mutuals import get_size
from CnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        load_dotenv()

        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            region_name=os.getenv("REGION_NAME")
        )

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Parse S3 URI
            s3_uri = self.config.source_URL  
            assert s3_uri.startswith("s3://"), "Invalid S3 URI"
            s3_uri_parts = s3_uri.replace("s3://", "").split("/", 1)
            bucket_name = s3_uri_parts[0]
            object_key = s3_uri_parts[1]

            self.s3_client.download_file(
                Bucket=bucket_name,
                Key=object_key,
                Filename=self.config.local_data_file
            )
            logger.info(f"{self.config.local_data_file} downloaded from S3!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
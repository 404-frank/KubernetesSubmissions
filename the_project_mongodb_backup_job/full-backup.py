import os
import subprocess
import datetime
from google.cloud import storage
import logging
import sys
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

MONGODB_HOST = os.environ.get('MONGODB_HOSTNAME', 'localhost')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', '9999'))
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', '')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')
MONGO_DATABASE_URL = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"
BUCKET_NAME = "mooc-exercise-backup-bucket"


def dump_mongo():
    try:
        backup_dir = "temp"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{backup_dir}/mongodb_backup_{timestamp}.gz"
        try:
            os.makedirs(backup_dir, exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create backup directory '{backup_dir}")

        dump_cmd = [
            "mongodump",
            f"--uri={MONGO_DATABASE_URL}",
            "--gzip",
            f"--archive={backup_file}",
        ]

        logging.info("Running mongodump...")
        subprocess.run(dump_cmd, check=True, stdout=sys.stdout, stderr=sys.stderr)
        logging.info("MongoDB Backup Completed!")
        return backup_file
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        raise RuntimeError(f"MongoDB backup failed: {error_msg}")

def get_file_content(file_name: str) -> str:
    with open(file_name, 'r') as file_handle:
        return file_handle.read()

def upload_to_gcs(backup_file_path):
    logging.info("starting upload proces")


    try:
        file_name = os.path.basename(backup_file_path)
        client = storage.Client.from_service_account_json(json_credentials_path="config/credentials.json")
        bucket = storage.Bucket(client, BUCKET_NAME)
        blob = bucket.blob(file_name)

        logging.info(
            f"Uploading {file_name} to gs://{BUCKET_NAME}/{file_name} ..."
        )
        blob.upload_from_filename(backup_file_path)
        logging.info("Upload complete!")
    except Exception as e:
        raise RuntimeError(f"Error uploading to GCS: {e}")


if __name__ == "__main__":
    try:
        backup_file = dump_mongo()
        upload_to_gcs(backup_file)
    except Exception as e:
        logging.error(f"Error: {e}")
        exit(1)
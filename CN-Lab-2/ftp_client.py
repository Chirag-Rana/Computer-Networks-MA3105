import ftplib
import os

# --- Configuration ---
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNu31FB!"
LOCAL_FILENAME = "upload_test.txt"
REMOTE_FILENAME = "remote_test.txt"
DOWNLOADED_FILENAME = "downloaded_test.txt"

def run_ftp_session():
    """Runs a full FTP session: connect, list, upload, download, and verify."""

    # 1. Create a dummy local file to upload
    print(f"Creating local file '{LOCAL_FILENAME}' for upload...")
    original_content = "This is a test file for the FTP assignment. 🚀"
    with open(LOCAL_FILENAME, "w") as f:
        f.write(original_content)

    try:
        # 2. Connect to the FTP server
        with ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS) as ftp:
            print(f"✅ Successfully connected to {FTP_HOST}")
            ftp.set_pasv(True) # Use passive mode

            # 3. List directory contents on the server
            print("\n--- Listing remote directory contents ---")
            ftp.dir()

            # 4. Upload the file
            print(f"\n--- Uploading '{LOCAL_FILENAME}' as '{REMOTE_FILENAME}' ---")
            with open(LOCAL_FILENAME, 'rb') as f:
                ftp.storbinary(f'STOR {REMOTE_FILENAME}', f)
            print("✅ File uploaded successfully.")

            # 5. Download the file from the server
            print(f"\n--- Downloading '{REMOTE_FILENAME}' as '{DOWNLOADED_FILENAME}' ---")
            with open(DOWNLOADED_FILENAME, 'wb') as f:
                ftp.retrbinary(f'RETR {REMOTE_FILENAME}', f.write)
            print("✅ File downloaded successfully.")
            
            # 6. Verify its content
            print("\n--- Verifying downloaded file content ---")
            with open(DOWNLOADED_FILENAME, "r") as f:
                downloaded_content = f.read()
            
            if original_content == downloaded_content:
                print("✅ Verification successful! Content matches.")
            else:
                print("❌ Verification failed! Content does not match.")
                
    except ftplib.all_errors as e:
        print(f"❌ FTP Error: {e}")
    finally:
        # 7. Clean up local files
        print("\nCleaning up local files...")
        if os.path.exists(LOCAL_FILENAME):
            os.remove(LOCAL_FILENAME)
        if os.path.exists(DOWNLOADED_FILENAME):
            os.remove(DOWNLOADED_FILENAME)
        print("Done.")

if __name__ == "__main__":
    run_ftp_session()

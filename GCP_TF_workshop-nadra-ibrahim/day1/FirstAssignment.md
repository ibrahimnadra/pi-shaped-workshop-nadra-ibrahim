# Exercise for Day 1: GCP Fundamentals: Compute, Storage & Networking

## Objective
Demonstrate understanding of core GCP services and create basic infrastructure using the GCP Console.

---

## Tasks Completed

### Task 0. Basic Setup
- Created a google cloud account using my email.
  ![account_created.png](screenshots/basic_setup/account_created.png)
- Created a new project named `pi-shaped-workshop` in the Google Cloud Console.
  ![gcp_dashboard.png](screenshots/basic_setup/gcp_dashboard.png)
- Installed the Google Cloud SDK on my local machine.
  ![gcloud_sdk_installed.png](screenshots/basic_setup/gcloud_sdk_installed.png)

---

### Task 1. Create a VM using Compute Engine

- Enabled the Compute Engine API.
  ![compute_engine_api.png](screenshots/vm_creation/compute_engine_api.png)
- Create Instance from Compute Engine Option
  ![vm_creation.png](screenshots/vm_creation/create_instance.png)
- A VM named `demo-vm-linux` was created in region `us-central1-a`.
  ![vm_config_1.png](screenshots/vm_creation/vm_config_1.png)
- Machine type: `E2`
  ![vm_config_2.png](screenshots/vm_creation/vm_config_2.png)
- Firewall: Allow HTTP Traffic
  ![vm_config_3.png](screenshots/vm_creation/vm_config_3.png)
- Check the vm is created
  ![new_created_vm.png](screenshots/vm_creation/new_created_vm.png)

---

### Task 2. Create a Cloud Storage bucket and upload a file

- Created a bucket named `pi-shaped-demo-bucket`
  ![bucket_creation.png](screenshots/bucket_creation/create_bucket.png)
- Check the bucket is created
  ![new_created_bucket.png](screenshots/bucket_creation/new_created_bucket.png)
- Selected the upload Option from the newly created bucket
  ![upload_option_in_bucket.png](screenshots/bucket_creation/upload_option_in_bucket.png)
- Selected the **blog*** file to upload
  ![file_selected_to_upload.png](screenshots/bucket_creation/file_selected_to_upload.png)
- Check the file is uploaded
  ![uploaded_file.png](screenshots/bucket_creation/uploaded_file.png)

---

### Task 3. Configure a VPC with custom subnets
- Created a custom VPC named `demo-vpc` 
  ![vpc_creation.png](screenshots/vpc_creation/vpc_creation.png)
- Subnet `demo-subnet` configured in `us-central1` 
  ![subnet-creation.png](screenshots/vpc_creation/subnet-creation.png)
- Entered the IP range: `10.0.0.0/24`
  ![vpc_ip_range.png](screenshots/vpc_creation/vpc_ip_range.png)
- Check the vpc is created
  ![new_created_vpc.png](screenshots/vpc_creation/new_created_vpc.png)

---

### Task 4. a. Connect to VM and Access File via Browser

- Go to the new created vm: `demo-vm-linux`
- Click "SSH" next to your VM. This opens a browser-based SSH terminal.
  ![ssh_via_browser.png](screenshots/access_file_via-browser/ssh_via_browser.png)
  ![ssh_via_browser_2.png](screenshots/access_file_via-browser/ssh_via_browser_2.png)
- Used `gsutil` to copy and read the file from Cloud Stora
```bash
  gsutil cp gs://pi-shaped-demo-bucket/blog .
  cat blog
 ```
![uploaded_file_access_via_browser.png](screenshots/access_file_via-browser/uploaded_file_access_via_browser.png)![upload

### Task 4. b. Connect to VM and Access File via Gcloud SDK

- Configured the SDK with my project:
  ```bash
  gcloud init
  ```
  ![gcloud_init.png](screenshots/access_file_via_gcloud_sdk/gcloud_init.png)
- Sign in to the gcloud when prompted
  ![signin_gcloud.png](screenshots/access_file_via_gcloud_sdk/signin_gcloud.png)
- Authorize via the browser
  ![signin_gcloud_2.png](screenshots/access_file_via_gcloud_sdk/signin_gcloud_2.png)
- Connected to the VM using `gcloud compute ssh`.
- Used `gsutil` to copy and read the file from Cloud Stora
```bash
  gsutil cp gs://pi-shaped-demo-bucket/blog .
  cat blog
 ```
 ![uploaded_file_access_via_gcloud_sdk.png](screenshots/access_file_via_gcloud_sdk/uploaded_file_access_via_gcloud_sdk.png)
  
### Task 5. Delete Resources

- Deleted the VM `demo-vm-linux` from Compute Engine.
  ![delete_vm.png](screenshots/delete_resources/delete_vm.png)
- Deleted the bucket `pi-shaped-demo-bucket` from Cloud Storage.
  ![delete_bucket.png](screenshots/delete_resources/delete_bucket.png)
- Deleted the VPC `demo-vpc` from VPC Network.
  ![delete_vpc.png](screenshots/delete_resources/delete_vpc.png)


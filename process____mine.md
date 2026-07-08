# RuView Workspace Setup, Docker, & Cloud Deployment Guide

This repository contains local validation testing scripts, client implementation pipes, and environment parameters for processing spatial tracking data matrices via **RuView**.

---

## Part 1: Host Machine Core Setup & Dependencies (Windows 11)

Because Windows 11 accounts can face path limitations, we avoid global system installs and route everything through an isolated, zero-privilege user workspace environment.

### Step 1: Initialize Workspace Directory
Open **Command Prompt** (`cmd`) or **Git Bash** on your host computer and run:
```cmd
cd C:\
mkdir shuvo-projects
cd shuvo-projects
git clone https://github.com
cd RuView
code .
```

### Step 2: Install and Configure Python 3
If your computer lacks Python or displays path tracking errors, execute the following commands inside your terminal to safely extract a local standalone user environment without admin access:

1. Request the Windows central installation manager to fetch the stable engine context:
   ```cmd
   py --version
   ```
2. If it drops an unknown flag or launches a store page, force package ingestion by typing:
   ```cmd
   py -m pip install --upgrade pip
   py -m pip install --only-binary=:all: numpy scipy
   py -m pip install "ruview[client]" --pre
   ```
   *(The `--pre` parameter authorizes your user layout to handle the pre-release core modules efficiently across isolated profiles).*

---

## Part 2: Install & Configure Docker Desktop on Windows 11

To run or test the containerized server locally before shipping it to the cloud, your Windows machine needs Docker Desktop up and running with a Linux backend kernel.

### Step 1: Install Windows Subsystem for Linux (WSL 2)
Docker Desktop on Windows 11 requires WSL 2 to execute Linux containers natively.
1. Open **PowerShell** or **Command Prompt** as **Administrator**.
2. Run this command:
   ```cmd
   wsl --install
   ```
3. **Restart your computer** when the installation finishes to apply system-level changes.

### Step 2: Install Docker Desktop
1. Download the official installer: [Docker Desktop for Windows](https://docker.com).
2. Run the downloaded `.exe` installer.
3. Ensure the option **"Use WSL 2 instead of Hyper-V (recommended)"** is explicitly **checked** during the installation wizard.
4. Click Close and log out/log back in when prompted.

### Step 3: Launch and Verify Docker
1. Open the **Docker Desktop** application from your Windows Start Menu.
2. Accept the terms of service agreement and wait for the status bar in the bottom-left corner to turn **Green (Running)**.
3. Verify that your command prompt can access Docker by running:
   ```cmd
   docker --version
   ```

---

## Part 3: Local Processing Engine Pipeline Proof

Before shifting server loads off your physical desktop architecture, verify that your client math engine processes array streams deterministically.

Execute the static validation tool suite directly inside your project folder:
```cmd
py archive/v1/data/proof/verify.py
```

### Expected Console Verification Target
```text
========================================================================
  SHA-256 HASH COMPARISON
    Computed: f8e76f21a0f9852b70b6d9dd5318239f6b20cbcb4cdd995863263cecdc446f7a
    Expected: f8e76f21a0f9852b70b6d9dd5318239f6b20cbcb4cdd995863263cecdc446f7a
    Status:   MATCH (bit-exact)
========================================================================
  VERDICT: PASS
```

---

## Part 4: Direct Client Stream Wireframe (`stream_test.py`)

Create a file named **`stream_test.py`** in the root of your project directory. This implementation completely bypasses pre-compiled `.pyd` binary architecture blockers by establishing a direct raw string connection hook via standard JSON formatting.

```python
import asyncio
import json
import websockets

async def main():
    # Local testing path. For cloud streams, swap with your secure wss address.
    uri = "ws://127.0.0.1:3001/ws/sensing"
    print(f"Connecting to RuView WebSocket Core at: {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected successfully! Streaming live spatial tracking arrays...\n")
            
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                
                # Intercept key telemetry metrics safely out of the JSON dictionary
                presence = data.get("presence_detected", False)
                count = data.get("person_count", 0)
                
                vitals = data.get("vitals", {})
                breathing = vitals.get("breathing_bpm", 0.0)
                
                print(f"Room Presence: {presence} | "
                      f"Estimated Count: {count} | "
                      f"Breathing Rate: {breathing:.1f} BPM")
                      
    except Exception as e:
        print(f"Connection dropped or failed to bind: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Local Testing Loop
If you ever want to run a quick test on your local PC using Docker, open **PowerShell** and clear your port mappings by launching the network container:
```powershell
docker run -p 3000:3000 -p 3001:3001 -e RUVIEW_BIND_ADDR=0.0.0.0 -e RUVIEW_ALLOW_UNAUTHENTICATED=1 ruvnet/wifi-densepose:latest
```
Then, open a separate terminal pane and execute your script:
```cmd
py stream_test.py
```

---

## Part 5: Persistent Cloud Hosting Infrastructure (Render)

Because tracking systems rely on long-lived real-time WebSocket state connections and continuous data packet bindings, **Serverless platforms like Vercel will fail**. You must utilize a persistent cloud environment layout that supports isolated Docker compilation layers.

### Step 1: Repository Ownership Fork
1. Navigate to the central source repository at: `https://github.com`
2. Click the **Fork** button in the top right corner to attach the repository structure directly to your personal GitHub workspace profile.

### Step 2: Service Provisioning on Render
1. Create a free profile configuration account on [Render.com](https://render.com).
2. From the main management workspace view, click **New +** -> Select **Web Service**.
3. Link your private GitHub profile context and pick your forked repository instance from the selection window.

### Step 3: Deployment Config Environment Grid
Apply the following layout variables into your instance builder configuration settings panel to safely bridge your incoming connection data lanes out to the web:

* **Runtime:** `Docker`
* **Instance Specification:** `Free` or `Starter ($7/mo)` *(Starter tier prevents the environment layer from falling asleep during long tracking idles)*.

#### Advanced Configuration Environment Variables
Click **Advanced** inside the panel and assign these explicit system control configurations:

| Key Field | Value Data Parameter | Purpose |
| :--- | :--- | :--- |
| `RUVIEW_BIND_ADDR` | `0.0.0.0` | Force server engine to listen across public cloud interfaces |
| `RUVIEW_ALLOW_UNAUTHENTICATED` | `1` | Permits open streaming evaluations over network spaces |
| `PORT` | `3000` | Exposes standard UI runtime ports directly to the proxy |

Click **Deploy Web Service**.

---

## Part 6: Connecting From Home to Your Cloud Environment

Once Render displays your deployment service indicator as **`Live`**, it will provide you with a permanent public web address (e.g., `https://onrender.com`). Your local computer is now completely free of hardware risks and container execution loops.

Update the connection string inside your desktop-side client file (**`stream_test.py`**) to hook your machine straight into your public cloud space:

```python
# Replace '://onrender.com' with the exact domain Render generated for you
uri = "wss://://onrender.com/ws/sensing"
```
*(Notice: Secure cloud connection paths automatically convert to `wss://` instead of the local `ws://` blueprint).*

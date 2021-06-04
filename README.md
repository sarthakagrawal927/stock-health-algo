# ec2

Connecting:

```bash
sudo ssh -i ./stocks-health.pem ec2-user@ec2-13-233-112-208.ap-south-1.compute.amazonaws.com
```

Sending File:

```bash
sudo scp -i ./stocks-health.pem <file-path> ec2-user@ec2-13-233-112-208.ap-south-1.compute.amazonaws.com:~/test
```

Hit it on: <http://ec2-13-233-112-208.ap-south-1.compute.amazonaws.com:8000/>

Running a new environment:

```bash
python3 -m venv <name-of-virtual-environment>

source venv/bin/activate

deactivate
```

Listing Port usage:

```bash
sudo ss -tulpn | grep LISTEN

sudo kill -9 `sudo lsof -t -i:8000`
```

Generating and installing requirements.txt

```bash
pip3 freeze > requirements.txt
pip install -r requirements.txt
```

Connecting with Jupyter Notebook:

```bash
jupyter notebook --no-browser

sudo ssh -i ./stocks-health.pem -NL 54321:localhost:8888 ec2-user@ec2-13-233-112-208.ap-south-1.compute.amazonaws.com
```

List all services

```bash
systemctl
```

Removing Services

```bash
sudo systemctl stop [servicename]
sudo systemctl disable [servicename]
sudo rm /etc/systemd/system/[servicename]
sudo rm /etc/systemd/system/[servicename] # and symlinks that might be related
sudo rm /usr/lib/systemd/system/[servicename]
sudo rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
sudo systemctl daemon-reload
sudo systemctl reset-failed
```

To update everything:

```bash
cd helloworld
git pull
sudo systemctl restart helloworld
```

Get Service File:

```bash
sudo nano /etc/systemd/system/helloworld.service
```

Enabling:

```bash
 sudo systemctl daemon-reload
 sudo systemctl start helloworld
 sudo systemctl enable helloworld
```

# Set linux editing mode
set -o emacs

# git

Delete a branch
------------------
remote <br/>
git push origin --delete rkisnah/alarmfixes

local <br/>
git branch -d feature/login


## Create a branch
git checkout -b rkisnah/alarmfixes

## Reset hard
```
git fetch origin
git reset --hard origin/master
```
## Ubuntu Minimize all windows
Ctrl Super D

## setting git bash prompts
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 " (%s)"\$ '

# restart gui ubuntu
sudo systemctl restart systemd-logind<br/>
sudo systemctl restart gdm

# unix timestamps to UTC 


# date - unix time to UTC

https://www.howtogeek.com/410442/how-to-display-the-date-and-time-in-the-linux-terminal-and-use-it-in-bash-scripts/
[rkisnah@compute-ops-01002 ~]$ date --utc --date='@1571249945' 
Wed Oct 16 18:19:05 UTC 2019

-> date -u -d @1571249945

# ubuntu printers
http://localhost:631/printers


# ubuntu tabs are slow
https://askubuntu.com/questions/1249405/ubuntu-18-04-20-04-alt-tab-gets-slow-laggy-after-a-while
killall -SIGQUIT gnome-shell


# verify yubikey
yubico-piv-tool -a verify-pin -P 4251421

# generate fingerprint from a private key
ssh-keygen -E md5 -lf ~/.ssh/<>.pub 
3072 MD5:5e:71:f5:e9: (RSA)

# find sha256 of keys
```
sudo ssh-keygen -E sha256 -lf id_rsa
2048 SHA256:asdfdsf rik.kisnah@hotmail.com (RSA)
ref:https://superuser.com/questions/1377132/get-the-fingerprint-of-an-existing-ssh-public-key/1425908
```

Use this for PEM file especially OCI API keys
```
openssl rsa -pubout -outform DER -in ~/.oci/oci_api_key.pem | openssl md5 -c
```
<br>
ref: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
<br>

# restart sshd
sudo systemctl restart sshd.service

# emacs on Terminate
set -o emacs

# git log one line 
git log --pretty=oneline

# adding identities for github access
```
# Step 1 loads the ssh-agent
eval `ssh-agent`
# Step 2 add the key to the agent
ssh-add ~/.ssh/id_rsa
# Step 3 check the md5sum of the agent
ssh-add -l
```

# get public ip via cli
#Ref: https://dev.to/adityathebe/a-handy-way-to-know-your-public-ip-address-with-dns-servers-4nmn
dig +short myip.opendns.com @resolver1.opendns.com -4

# tmux
set -g mouse on <br/>
set -g mouse-select-pane on

# random password generator
# https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/
openssl rand -base64 32

# open-ssh
## Generate RSA key pair in PEM for API Signing in OCI
openssl genrsa -out ~/.oci/oci_api_key.pem 2048 #-aes128 with cipher 

chmod go-rwx ~/.oci/oci_api_key.pem

openssl rsa -pubout -in ~/.oci/oci_api_key.pem -out ~/.oci/oci_api_key_public.pem  

### SSH KEY Pair
ssh-keygen -t rsa -N "" -b 2048 -C "rik3" -f /tmp/rik3

// Add the key
ssh-add rik3

// Delete the key
ssh-add -d rik3

Ref:
https://security.stackexchange.com/questions/29876/what-are-the-differences-between-ssh-generated-keysssh-keygen-and-openssl-keys
https://docs.oracle.com/en-us/iaas/Content/General/Concepts/credentials.htm#Security_Credentials

ssh-add -d rik3

# Create a qcow image 

 qemu-img convert -O qcow2 /dev/sda /home/ubuntu/image.qcow2
 ref: https://askubuntu.com/questions/853160/create-image-with-dd-command-cow2
 
# update-alternatives 
ref: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux
update-alternatives --list python

update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

update-alternatives --config python

# Encry and decrypt
ref: https://stackoverflow.com/questions/29010967/openssl-unable-to-load-public-key 

// 1. Generate the private key <br/>
openssl genrsa -out key.pem 1024

// 2. Print details of the private key <br/>
openssl rsa -in key.pem -text -noout

// 3. Generate the public key <br/>
openssl rsa -in key.pem -pubout -out pub.pem 

// 4. Encrypt file with the public key <br/>
openssl rsautl -encrypt -inkey pub.pem -pubin -in file.txt -out file.bin

// 5. Decrypt file with the public key <br/>
openssl rsautl -decrypt -inkey key.pem -in file.bin

# journalctl

ref: https://www.howtogeek.com/499623/how-to-use-journalctl-to-read-linux-system-logs/ <br/>

'''
// to follow
journalctl -f
'''

# ag
Find text in specific file extensions <br/>
https://unix.stackexchange.com/questions/343570/how-do-i-use-ag-to-look-for-text-in-files-with-certain-extensions <br/> 
'''
ag "shapeConfigs" --file-search-regex '\.conf'
'''

# vim 
## Open vertically
```
set :ba

# cli
vim -o *.* 
vim -O *.*
```

## tabs
```
1gt btg
```
<br> ref: https://superuser.com/questions/410982/in-vim-how-can-i-quickly-switch-between-tabs <br>

# Add ip to know_hosts ssh
```
ssh-keyscan -H 150.136.35.112 >> ~/.ssh/known_hosts
```
<br> ref: https://www.techrepublic.com/article/how-to-easily-add-an-ssh-fingerprint-to-your-knownhosts-file-in-linux/ <br/>

# Redirects
```
1) Redirect both standard output and standard error to a file
command &>file
```
<br> ref: https://catonmat.net/bash-one-liners-explained-part-three <br/>

# ssh - avoid ssh host verification
```
ssh -o "StrictHostKeyChecking no" opc@grafana
```
ref: https://superuser.com/questions/125324/how-can-i-avoid-sshs-host-verification-for-known-hosts <br>

# Create self signed certs for https
I have used this for this https://community.grafana.com/t/grafana-https-configuration/524 <br>
```
https://linuxize.com/post/creating-a-self-signed-ssl-certificate/
openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out example.crt \
            -keyout example.key

```

# Get ips of IB interfaces 

Step 1 - get interfaces names
``
ibdev2netdev | grep -v "mlx5_1 " | grep -v "mlx5_0 " | grep -v "mlx5_14 "| grep -v "mlx5_15 " | cut -d" " -f 5
interfaces=$(ibdev2netdev | grep -v "mlx5_1 " | grep -v "mlx5_0 " | grep -v "mlx5_14 "| grep -v "mlx5_15 " | cut -d" " -f 5)
``

Step 2 - get private ips
``
for i in ${interfaces[@]}; do ip a show dev $i  ; done  | grep "inet" | awk '{print $2}' | cut -d"/" -f1
``

# Vim on remote server for py

https://vim.fandom.com/wiki/Converting_tabs_to_spaces

``
:set tabstop=4
:set shiftwidth=4
:set expandtab
``

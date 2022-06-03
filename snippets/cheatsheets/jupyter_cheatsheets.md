# Set password 
https://jupyter-notebook.readthedocs.io/en/stable/public_server.html <br>

```
$ jupyter notebook password

Enter password:  ****
Verify password: ****

[NotebookPasswordApp] Wrote hashed password to /Users/you/.jupyter/jupyter_notebook_config.json

c.NotebookApp.password = u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed
```

# Change the file .jupyter/jupyter_notebook_config.py

```
c.NotebookApp.password = u'sha1:82fdded40f08:a06d0cf89877b3a87d809a9d6f9c9057d5871285'  
```

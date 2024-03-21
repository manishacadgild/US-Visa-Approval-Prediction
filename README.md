# US-Visa-Approval-Prediction
#Git Commit
```bash
git status
git add .
git commit -m "Updated"
git push -f origin main 
``` 
```bash 
conda create -n visa python==3.8 -y
conda activate ./visa
```
```bash
pip install -r requirements.txt 

```


```bash
1.constants # Some important varible
2.config_entity # All the folder and files path
3.artifact_entity # Output from the componets
4.component # Data Ingetion to model pusher(Actual stage of the data pipeline)
5.pipeline ## To define pipeline from start to end execution of the pipeline
6.app.py ## End point url define into aap.py
```
# Export the Enviornment variables for window to set in Enviornment and for linux export.
```bash
export MONGODB_URL="mongodb+srv:<>" 

```bash

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

export AWS_ACCESS_KEY_ID="<>"
export AWS_SECRET_ACCESS_KEY="<>"
```
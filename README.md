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
1.constants
2.config_entity # Input entity configuration define in config_entity
3.artifact_entity # Return output entity define in artifact_entity
4.component # Data Ingetion to model pusher
5.pipeline ## To define pipeline from start to end execution
6.app.py ## End point url define into aap.py
```
# Export the Enviornment variables for window to set in Enviornment and for linux export.
```bash
export MONGODB_URL="mongodb+srv:<>" 

```
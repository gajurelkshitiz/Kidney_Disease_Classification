# Kidney_Disease_Classification

## Workflows

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Updata params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/gajurelkshitiz/Kidney_Disease_Classification.mlflow \
MLFLOW_TRACKING_USERNAME=gajurelkshitiz \
MLFLOW_TRACKING_PASSWORD=76ecf22cf8af13e8c79541bb1fa7fe9705463320 \
python script.py


Run this to export :
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/gajurelkshitiz/Kidney_Disease_Classification.mlflow

export MLFLOW_TRACKING_USERNAME=gajurelkshitiz

export MLFLOW_TRACKING_PASSWORD=76ecf22cf8af13e8c79541bb1fa7fe9705463320
```
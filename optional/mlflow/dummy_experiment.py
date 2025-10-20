import mlflow

mlflow.set_experiment("devops-demo")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("optimizer", "adam")
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_metric("loss", 0.08)
    print("Dummy experiment logged to MLFlow")

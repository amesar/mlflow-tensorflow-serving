
from setuptools import setup, find_packages
  
setup(name="mlflow_export_import",
      version="1.0.0",
      author="Andre M",
      description="MLflow TensorFlow Serving",
      url="https://github.com/amesar/mlflow-tensorflow-serving",
      python_requires=">=3.7",
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "mlflow>=1.13.0",
          "wheel"
      ])

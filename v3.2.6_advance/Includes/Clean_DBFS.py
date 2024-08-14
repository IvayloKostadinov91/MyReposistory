# Databricks notebook source
#path
#users_path = "dbfs:/mnt/dbacademy-users/ivaylo.kostadinov@adastragrpbg.onmicrosoft.com/data-engineering-with-databricks"
users_path = "dbfs:/mnt/dbacademy-users/ivaylo.kostadinov@adastragrpbg.onmicrosoft.com/advanced-data-engineering-with-databricks"
datasets_path = "dbfs:/mnt/dbacademy-datasets/data-engineer-learning-path"

# COMMAND ----------

# Function to recursively delete files and subdirectories
def recursive_delete(path):
    try:
        files = dbutils.fs.ls(path)
        for file in files:
            if file.isDir():
                recursive_delete(file.path)
            else:
                dbutils.fs.rm(file.path, False)
        dbutils.fs.rm(path, True)
    except Exception as e:
        print(f"Failed to delete {path}: {e}")

# Define the working directory path
working_dir = users_path

# Recursively delete the working directory
recursive_delete(working_dir)

# COMMAND ----------

# MAGIC %md
# MAGIC # Function to recursively delete files and subdirectories
# MAGIC def recursive_delete(path):
# MAGIC     try:
# MAGIC         files = dbutils.fs.ls(path)
# MAGIC         for file in files:
# MAGIC             if file.isDir():
# MAGIC                 recursive_delete(file.path)
# MAGIC             else:
# MAGIC                 dbutils.fs.rm(file.path, False)
# MAGIC         dbutils.fs.rm(path, True)
# MAGIC     except Exception as e:
# MAGIC         print(f"Failed to delete {path}: {e}")
# MAGIC
# MAGIC # Define the working directory path
# MAGIC working_dir = datasets_path
# MAGIC
# MAGIC # Recursively delete the working directory
# MAGIC recursive_delete(working_dir)

FROM jupyter/pyspark-notebook:latest

WORKDIR /workspace

COPY . /workspace

EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]
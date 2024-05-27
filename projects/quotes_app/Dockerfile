# docker build -t myimage .
# docker run -d --name mycontainer -p 8000:8000 myimage

FROM python:3.10-slim

ARG wheel=quotes_app-0.1.0-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/$wheel /code/$wheel
RUN pip install --no-cache-dir --upgrade /code/$wheel

CMD ["uvicorn", "experiment.fastapi_app.core:app", "--host", "0.0.0.0", "--port", "8000"]

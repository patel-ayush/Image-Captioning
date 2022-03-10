FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade setuptools pip wheel
RUN pip3 install -r requirements.txt


EXPOSE 80

COPY . /app

ENTRYPOINT ["streamlit","run"]

CMD ["main.py"]

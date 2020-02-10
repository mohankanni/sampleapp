# Install 
FROM python:3.7

MAINTAINER Mohan Kanni "vinay.k@fluentgrid.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

#Port
EXPOSE 8092

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml

WORKDIR /app

ENTRYPOINT ["streamlit", "run"]

CMD ["/app.py"]



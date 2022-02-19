FROM python:3

RUN mkdir app
WORKDIR app
COPY . .

RUN pip3 install discord 
RUN pip3 install asyncio 
RUN pip3 install datetime 
RUN pip3 install pytz 

CMD ["python3","main.py"]

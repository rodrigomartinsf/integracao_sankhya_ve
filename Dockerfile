FROM python:3
COPY . .
RUN pip install requests
RUN pip install SQLAlchemy
RUN pip install pymysql
CMD [ "python", "./create_table.py" ]


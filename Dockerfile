FROM python:3.11
ADD /requirement.txt /
ADD /regmodel.pkl / 
ADD /scaler.pkl / 
RUN pip install -r /requirement.txt
ADD California House value Prediction.ipynb /

ENV PYTHONUNBUFFERED=1

CMD [ "python","-m","notebook","./California House value Prediction.ipynb","--allow-root"]
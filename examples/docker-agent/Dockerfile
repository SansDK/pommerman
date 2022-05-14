FROM python:3.6

ADD ./examples/docker-agent /agent

ADD . /pommerman
RUN cd /pommerman && pip install .

EXPOSE 5000

ENV NAME Agent

# Run app.py when the container launches
WORKDIR /agent
ENTRYPOINT ["python"]
CMD ["run.py"]

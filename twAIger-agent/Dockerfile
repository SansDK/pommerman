FROM python:3.6

ADD ./twAIger-agent /agent

ADD . /pommerman
RUN cd /pommerman && pip install .

EXPOSE 5000

ENV NAME Agent

# Run run.py when the container launches
WORKDIR /agent
ENTRYPOINT ["python"]
CMD ["run.py"]

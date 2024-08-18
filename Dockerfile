FROM pypy:latest

COPY Days/mercedes_universe.py /

CMD [ "python", "./mercedes_universe.py" ]
FROM mickahell/quantum_lab_qiskit:latest

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="Quantum Museum" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/quantum_fractals-museum" \
      org.opencontainers.image.url="https://github.com/mickahell/quantum_fractals-museum/tags" \
      org.opencontainers.image.description="Quantum Fractals Museum" \
      org.opencontainers.image.os="Ubuntu Bionic" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq
RUN pip3 install streamlit

ADD conf/* ~/.streamlit/
ADD app/* /opt/museum/

EXPOSE 8501

CMD streamlit run /opt/museum/app.py

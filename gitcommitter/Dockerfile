FROM alpine:latest

ARG EMAIL
ENV USER_EMAIL=${EMAIL}
ARG NAME
ENV USER_NAME=${NAME}

WORKDIR /app

RUN apk add --no-cache bash unzip openssh git
RUN ssh-keygen -t ed25519 -P "" -N '' -C $USER_EMAIL -f ~/.ssh/id_ed25519
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

COPY truecommit.sh /app/

CMD ["bash", "truecommit.sh"]
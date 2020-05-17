FROM debian:stretch

RUN mkdir /mnt/ramdisk

WORKDIR /scripts
ENV PATH="/usr/bin:/scripts:${PATH}"

COPY run /scripts
RUN chmod 755 /scripts/*

VOLUME /mnt/ramdisk

CMD ["run"] 

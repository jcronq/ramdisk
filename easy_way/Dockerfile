FROM debian:stretch

RUN mkdir /mnt/ramdisk

WORKDIR /scripts
ENV PATH="/usr/bin:/scripts:${PATH}"

COPY run /scripts
COPY bash/ramdiskctl /scripts
RUN chmod 755 /scripts/*

CMD ["run"] 

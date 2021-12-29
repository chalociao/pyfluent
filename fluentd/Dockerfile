# FROM fluent/fluentd:v1.14-debian

# USER root
# RUN gem install fluent-plugin-elasticsearch
# USER fluent

FROM fluent/fluentd
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri"]
RUN rm /fluentd/etc/fluent.conf
COPY /config/fluent.conf /fluent/etc

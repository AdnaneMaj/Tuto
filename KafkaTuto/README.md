# Kafka Tuto

This is a very simple kafka tuto


# Motivation behind kafka
Elements of a Database was perceived in the past as **things**, but after it appears that it's better to think in those elements as events, that has **An indication in time**, so we store data in what we called a **log**

    **Log data** is a digital record of events occurring within a system, application or on a network device or endpoint.


**Kafka** comes in handy simply as a tool to manage this events

* **Topic** : <ins>Ordered collection of events</ins> stored in a durable way(*written to disk and ruplicated to ensure that no server failure will cause this data instance to go away*)


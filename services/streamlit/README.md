# Streamlit app

This simple app pulls down data from an API and displays the obtained lat-long coordinates on a map.

Tests and build can be run with `docker-compose build`, and the service brought up with `docker-compose up`. The app should be available on `http://localhost:8080`.

### Other notes

The streamlit app is served via a Tornado webserver. This supports non-blocking IO and networking (i.e. async). Each user that logs on maintains a long running connection to the server in a session, and Streamlit stores the session state on the server. The async nature means that there is plenty of overhead in vertical scaling, although horizontal scaling will need some form of sticky sessions to make sure that a user is constantly in contact with their session state (e.g. [this chat](https://discuss.streamlit.io/t/how-to-really-scale-a-streamlit-app/44662/4)).
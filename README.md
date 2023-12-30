# dashboarding
A play area for various types of dashboard. This repo contains a bunch of simple test examples.

### Properties of various dashboarding apps

Dashboarding apps come in many shapes and sizes. Areas where they tend to differ are:
- Testing frameworks and testability.
- The state being held in the server or client (which often manifests as connections being [http or websocket](https://www.geeksforgeeks.org/what-is-web-socket-and-how-it-is-different-from-the-http/)). This can affect how one would do horizontal scaling (since sticky sessions a.k.a. session affinity might be needed).
- The concurrency support for the app (e.g. asyncio, threading and/or multiple processes/workers). This affects vertical scalability.
- Available connectors to data sources.
- Ability to plumb in existing libraries into the app.

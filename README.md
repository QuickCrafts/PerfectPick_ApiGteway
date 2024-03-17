# PerfectPick API Gateway

This API reference provides details on how to interact with the GraphQL API Gateway of our application. GraphQL is a powerful query language for APIs that allows clients to request exactly the data they need. This reference will cover the available queries, mutations, and types supported by our GraphQL API.

**Base URL**

The base URL for our API Gateway is [http://localhost:8000/graphiql](http://localhost:8000/graphiql).

**Run Project**

Run and deploy project instruction on [Deployment](#deploy).

**API Reference Index**

* [Authentication](#id1)
* [Message Queue](#id2)
* [Queries](#id3)
    * [Get User info](#id3.1)
    * 
    * 
    * 
* [Mutations](#id4)
    * 
    * 
    * 
    * 
* [Types](#id5)
    * 
    * 
    * 
    * 

***
<br />
<br />

## API Reference

<a id="id1"></a>

### Authentication

```http
POST /graphql HTTP/1.1
Host: localhost:8000
Authorization: Bearer BEARER_TOKEN
Content-Type: application/json

{
  "query": "...",
  "variables": { "userId": "1" }
}
```
<a id="id2"></a>

### Message Queue

// to do

<a id="id3"></a>

### Queries

<a id="id3.1"></a>

#### Get User Info
// to do

<a id="id4"></a>

### Mutations

// to do

<a id="id5"></a>

### Types

// to do

***
<br />
<br />

<a id="deploy"></a>

## Deployment

To deploy this project:

```bash
  ## todo
```

### Run Locally

Python is required.

1. Clone the project

```bash
  git clone https://github.com/QuickCrafts/PerfectPick_ag.git
```

2. Go to the project directory

```bash
  cd PerfectPick_ag
```

3. Start the server

```bash
  make run
```

If it's the first time run

```bash
  ./init.sh && make run
```
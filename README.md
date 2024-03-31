# PerfectPick API Gateway

This API reference provides details on how to interact with the GraphQL API Gateway of our application. GraphQL is a powerful query language for APIs that allows clients to request exactly the data they need. This reference will cover the available queries, mutations, and types supported by our GraphQL API.

**Base URL**

The base URL for our API Gateway is [http://localhost:8000/graphiql](http://localhost:8000/graphiql).

**Run Project**

Run and deploy project instruction on [Deployment](#deploy).

<a id="index"></a>

**API Reference Index**

* [Authentication](#id1)
* [Message Queue](#id2)
* [Queries](#id3)
  * [Users Management](#id3.1)
    * [Get user by user id](#id3.1.1)
    * [Get user by email](#id3.1.2)
    * [Get users](#id3.1.3)
    * [Login with email](#id3.1.4)
    * [Login with google](#id3.1.5)
  * [Countries](#id3.2)
    * [Get countries](#id3.2.1)
    * [Get country by id](#id3.2.2)
  * [Likes](#id3.3)
    * [Get preferences by user id](#id3.3.1)
    * [Get preferences by media id](#id3.3.2)
    * [Get wishlist](#id3.3.3)
    * [Get rating by media id](#id3.3.4)
  * [Catalog](#id3.4)
    * [Get books](#id3.4.1) 
    * [Get movies](#id3.4.2)
    * [Get songs](#id3.4.3)
    * [Get book by book id](#id3.4.4)
    * [Get movie by movie id](#id3.4.5)
    * [Get song by song id](#id3.4.6)
  * [Recommendations](#id3.5)
    * [Get recommend](#id3.5.1)
  * [Analysis](#id3.6)
    * [Generate analysis](#id3.6.1)
  * [Ads](#id3.7)
    * [Get user ads](#id3.7.1)
    * [Get company ads](#id3.7.2)
    * [Get ads](#id3.7.3)
    * [Get companies](#id3.7.4)
  * [Payments](#id3.8)
    * [Get bills by company](#id3.8.1)
    * [Get bills by ad](#id3.8.2)
    * [Get bills](#id3.8.3)
    * [Get bill by id](#id3.8.4)
* [Mutations](#id4)
  * [Users Management](#id4.1)
    * [Sign up user with email](#id4.1.1)
    * [Sign up user with google](#id4.1.2)
    * [Verify user account](#id4.1.3)
    * [Forgot Password](#id4.1.4)
    * [Change Password](#id4.1.5)
    * [Update User](#id4.1.6)
    * [Complete setup](#id4.1.7)
    * [Delete User](#id4.1.8)
  * [Countries](#id4.2)
    * [Create country](#id4.2.1)
    * [Update country](#id4.2.2)
    * [Delete country](#id4.2.3)
    * [Import countries data](#id4.2.4)
  * [Likes](#id4.3)
    * [Like media](#id4.3.1)
    * [Dislike media](#id4.3.2)
    * [Delete like/dislike media](#id4.3.3)
    * [Rating media](#id4.3.4)
    * [Update media rating](#id4.3.5)
    * [Add media to wishlist](#id4.3.6)
    * [Remove media from wishlist](#id4.3.7)
  * [Catalog](#id4.4)
    * [Create book](#id4.4.1)
    * [Create movie](#id4.4.2)
    * [Create song](#id4.4.3)
    * [Update book](#id4.4.4)
    * [Update movie](#id4.4.5)
    * [Update song](#id4.4.6)
    * [Delete book](#id4.4.7)
    * [Delete movie](#id4.4.8)
    * [Delete song](#id4.4.9)
    * [Import books data](#id4.4.10)
    * [Import movies data](#id4.4.11)
    * [Import songs data](#id4.4.12)
  * [Recommendations](#id4.5)
    * [Mark Recommend as used](#id4.5.1)
    * [Generate new Recommend](#id4.5.2)
  * [Companies](#id4.6)
    * [Create company](#id4.6.1)
    * [Update company](#id4.6.2)
  * [Ads](#id4.7)
    * [Create ad](#id4.7.1)
    * [Update ad](#id4.7.2)
    * [Delete ad](#id4.7.3)
  * [Release](#id4.8)
    * [Publish Ad](#id4.8.1)
    * [TTPAR](#id4.8.2)
  * [Payments](#id4.9)
    * [Create bill](#id4.9.1)
    * [Delete bill](#id4.9.1)
    * [Pay bill](#id4.9.1)
* [Types](#id5)
  * [Users Management](#id5.1)
    * [User](#id5.1.1)
    * [Country](#id5.1.2)
    * [CreateUser](#id5.1.3)
    * [UpdateUser](#id5.1.4)
    * [CreateCountry](#id5.1.5)
    * [UpdateCountry](#id5.1.6)
  * [Likes](#id5.2)
    * [Like](#id5.2.1)
    * [LikeExtended](#id5.2.2)
    * [Wishlist](#id5.2.3)
  * [Catalog](#id5.3)
    * [Media](#id5.3.1)
  * [Recommendations](#id5.4)
    * [Recommendation](#id5.4.1)
  * [Analysis](#id5.5)
    * [Analysis](#id5.5.1)
    * [GenderAnalysis](#id5.5.2)
    * [NationalityAnalysis](#id5.5.3)
    * [AgeAnalysis](#id5.5.4)
    * [CountLikes](#id5.5.5)
  * [Release](#id5.6)
    * [Company](#id5.6.1)
    * [Ad](#id5.6.2)
  * [Payments](#id5.7)
    * [Bill](#id5.7.1)

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

<!-- @todo -->



<a id="id3"></a>

### Queries

<a id="id3.1"></a>

#### User Management

<a id="id3.1.1"></a>

**Get user by user id**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get user by user id - Users MS

```bash
  GET /users/${id}
```

3. Get country by id - Users MS

```bash
  GET /countries/${id}
```

_Query Example_

```graphql
query {
  userByID(token: str!, id: int!) {
    """
    User Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.

_Query Type Response_

[User](#id5.1.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.1.2"></a>

**Get user by email**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get user by email - Users MS

```bash
  GET /users/email/${email}
```

3. Get country by id - Users MS

```bash
  GET /countries/${id}
```

_Query Example_

```graphql
query {
  userByEmail(token: str!, email: str!) {
    """
    User Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `email` is user email (string) **REQUIRED**.

_Query Type Response_

[User](#id5.1.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.1.3"></a>

**Get all users**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get users filtered - Users MS

```bash
  GET /users?...
```

3. Get country by id for each user - Users MS

```bash
  GET /countries/${id}
```

_Query Example_

```graphql
query {
  allUsers(
    token: str!,
    gender: str,
    country: int,
    low_age: int,
    high_age: int
  ) {
    """
    Array of User Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `gender` is a enum: "M", "F", "O", "P" (string).
* `Country` is the country id (int).
* `low_age` is age range lower limit to filter (int).
* `high_age` is age range upper limit to filter (int).

_Query Type Response_

Array of [User](#id5.1.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.1.4"></a>

**Login with email**

_Logic Steps_

1. Login with email - Users MS

```bash
  POST /users/login
```

_Query Example_

```graphql
query {
  loginWithEmail(email: str!, password: str!) {
    token
  }
}
```

Parameters:
* `password` is user password (string) **REQUIRED**.
* `email` is user email (string) **REQUIRED**.

_Query Type Response_

User token (string).

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.1.5"></a>

**Login with google**

_Logic Steps_

1. Login with google - Users MS

```bash
  POST /users/login
```

_Query Example_

```graphql
query {
  loginWithGoogle(googleToken: str!) {
    token
  }
}
```

Parameters:
* `googleToken` is user auth google token (string) **REQUIRED**.

_Query Type Response_

User token (string).

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---
</br>

<a id="id3.2"></a>

#### Countries

<a id="id3.2.1"></a>

**Get countries**

_Logic Steps_

1. Get countries - Users MS

```bash
  GET /countries
```

_Query Example_

```graphql
query {
  allCountries() {
    """
    Array of Country Type attributes
    """
  }
}
```

_Query Type Response_

[Country](#id5.1.2) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---
<a id="id3.2.2"></a>

**Get country by id**

_Logic Steps_

1. Get country by id - Users MS

```bash
  GET /countries/${id}
```

_Query Example_

```graphql
query {
  countryByID(id: int!) {
    """
    Country Type attributes
    """
  }
}
```

Parameters:
* `id` is country id (int) **REQUIRED**.

_Query Type Response_

[Country](#id5.1.2) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.3"></a>

#### Likes

<a id="id3.3.1"></a>

**Get likes by user id**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get likes by user id - Likes MS

```bash
  GET /likes/user/${id}?...
```

_Query Example_

```graphql
query {
  likesByUserId(token: str!, id: int!, preference: str, media: str) {
    """
    Array of Like Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `preference` is preference type enum: "LK" | "DLK" (string).
* `media` is media type enum: "MOV" | "SON" | "BOO" (string).

_Query Type Response_

Array of [Like](#id5.2.1) type.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.3.2"></a>

**Get likes by media id**

_Logic Steps_

1. Get likes by media id - Likes MS

```bash
  GET /likes/media/${id}?...
```

_Query Example_

```graphql
query {
  likesByMediaId(id: int!, media: str!, preference: str) {
    """
    Array of Like Type attributes
    """
  }
}
```

Parameters:
* `id` is media id (int) **REQUIRED**.
* `media` is media type enum: "MOV" | "SON" | "BOO" (string) **REQUIRED**.
* `preference` is preference type enum: "LK" | "DLK" (string).

_Query Type Response_

Array of [Like](#id5.2.1) type.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.3.3"></a>

**Get wishlist by user id**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get wishlist by user id - Likes MS

```bash
  GET /likes/wishlist/${id}
```

3. Get media info - Catalog MS

* Get movies info

```bash
  GET /movies/${id}
```

* Get books info

```bash
  GET /books/${id}
```

* Get songs info

```bash
  GET /songs/${id}
```

_Query Example_

```graphql
query {
  wishlistByUserId(token: str!, id: int!, media: str) {
    """
    Wishlist Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `media` is media type enum: "MOV" | "SON" | "BOO" (string).

_Query Type Response_

[Wishlist](#id5.2.3) type.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.3.4"></a>

**Get rating by media id**

_Logic Steps_

1. Get rating by media id - Likes MS

```bash
  GET /likes/average/${id}?...
```

_Query Example_

```graphql
query {
  ratingByMediaId(id: int!, media: str!) {
    rating
  }
}
```

Parameters:
* `id` is media id (int) **REQUIRED**.
* `media` is media type enum: "MOV" | "SON" | "BOO" (string) **REQUIRED**.

_Query Type Response_

* `rating` is media average rating (float).


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.4"></a>

#### Catalog

<a id="id3.4.1"></a>

**Get Books**

_Logic Steps_



2. Get books - Catalog MS

```bash
  GET /books
```

3. *If user id inside request, get preference relation of each book - Likes MS

```bash
  GET /likes/media/${id}?media_type=BOO
```

_Query Example_

```graphql
query {
  allBooks(token: string, id: int) {
    """
    Array of Media Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string).
* `id` is user id (int).

_Query Type Response_

Array of [Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.4.2"></a>

**Get movies**

_Logic Steps_

1. *If user id inside request, verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get movies - Catalog MS

```bash
  GET /movies
```

3. *If user id inside request, get preference relation of each movie - Likes MS

```bash
  GET /likes/media/${id}?media_type=MOV
```

_Query Example_

```graphql
query {
  allMovies(token: string, id: int) {
    """
    Array of Media Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string).
* `id` is user id (int).

_Query Type Response_

Array of [Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.4.3"></a>

**Get songs**

_Logic Steps_

1. *If user id inside request, verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get songs - Catalog MS

```bash
  GET /songs
```

3. *If user id inside request, get preference relation of each song - Likes MS

```bash
  GET /likes/media/${id}?media_type=SON
```

_Query Example_

```graphql
query {
  allSongs(token: string, id: int) {
    """
    Array of Media Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string).
* `id` is user id (int).

_Query Type Response_

Array of [Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.


---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.4.4"></a>

**Get Book by id**

_Logic Steps_

1. *If user id inside request, verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get book by id - Catalog MS

```bash
  GET /books/${media_id}
```

3. *If user id inside request, get preference by media id and user id - Likes MS

```bash
  GET /likes/preference?user_id=${user_id}&media_id=${media_id}&media_type=BOO
```

_Query Example_

```graphql
query {
  bookById(media_id: int!, token: string, user_id: int) {
    """
    Media Type attributes
    """
  }
}
```

Parameters:
* `media_id` is media id (int) **REQUIRED**.
* `token` is login token (string).
* `user_id` is user id (int).

_Query Type Response_

[Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.4.5"></a>

**Get movie by id**

_Logic Steps_

1. *If user id inside request, verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get movie by id - Catalog MS

```bash
  GET /movies/${media_id}
```

3. *If user id inside request, get preference by media id and user id - Likes MS

```bash
  GET /likes/preference?user_id=${user_id}&media_id=${media_id}&media_type=MOV
```

_Query Example_

```graphql
query {
  movieById(media_id: int!, token: string, user_id: int) {
    """
    Media Type attributes
    """
  }
}
```

Parameters:
* `media_id` is media id (int) **REQUIRED**.
* `token` is login token (string).
* `user_id` is user id (int).

_Query Type Response_

[Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.4.6"></a>

**Get song by id**

_Logic Steps_

1. *If user id inside request, verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get song by id - Catalog MS

```bash
  GET /songs/${media_id}
```

3. *If user id inside request, get preference by media id and user id - Likes MS

```bash
  GET /likes/preference?user_id=${user_id}&media_id=${media_id}&media_type=SON
```

_Query Example_

```graphql
query {
  songById(media_id: int!, token: string, user_id: int) {
    """
    Media Type attributes
    """
  }
}
```

Parameters:
* `media_id` is media id (int) **REQUIRED**.
* `token` is login token (string).
* `user_id` is user id (int).

_Query Type Response_

[Media](#id5.3.1) type. If user id inside request, media type will have user like relation too.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.5"></a>

#### Recommendations

<a id="id3.5.1"></a>

**Get recommend**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get user recommendation - Recommendation MS

```bash
  GET /recommendation/${id}
```

3. Get media info of the recommend- Catalog MS

* Get movie info of each movie recommended

```bash
  GET /movies/${id}
```

* Get book info of each book recommended

```bash
  GET /books/${id}
```

* Get song info of each song recommended

```bash
  GET /songs/${id}
```

_Query Example_

```graphql
query {
  recommendByUserId(token: string!, id: int!) {
    """
    Recommend Type attributes
    """
  }
}
```

Parameters:
* `id` is user id (int) **REQUIRED**.
* `token` is login token (string) **REQUIRED**.

_Query Type Response_

[Recommendation](#id5.4.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.6"></a>

#### Analysis

<a id="id3.6.1"></a>

**Generate Analysis**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${user_id}
```

2. Get all users - Users MS

```bash
  GET /users
```

3. Get all countries - Users MS

```bash
  GET /countries
```

4. Get likes related with media id - Likes MS

```bash
  GET /likes/media/${media_id}?media_type=${type}
```

5. Get analysis by a given media - Ads MS

```bash
  GET /ads/analysis
```

_Query Example_

```graphql
query {
  getAnalysis(token: string!, user_id: int!, media_id: int!, type: str!) {
    """
    Analysis Type attributes
    """
  }
}
```

Parameters:
* `media_id` is media id (int) **REQUIRED**.
* `type` is media type enum: 'MOV' | 'SON' | 'BOO' (string) **REQUIRED**.
* `token` is login token (string) **REQUIRED**.
* `user_id` is user id (int) **REQUIRED**.

_Query Type Response_

[Analysis](#id5.5.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.7"></a>

#### Ads

<a id="id3.7.1"></a>

**Get user ads**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Get ads active for a given user - Ads MS

```bash
  GET /ads/active/${id}
```

_Query Example_

```graphql
query {
  getUserAds(token: string!, id: int!) {
    """
    Array of Ad Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.

_Query Type Response_

Array of [Ad](#id5.6.2) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.7.2"></a>

**Get company ads**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get ads by company id - Ads MS

```bash
  GET /ads?company=${com_id}
```

_Query Example_

```graphql
query {
  getCompanyAds(token: string!, id: int!, com_id: int!) {
    """
    Array of Ad Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `com_id` is company id (int) **REQUIRED**.

_Query Type Response_

Array of [Ad](#id5.6.2) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.7.3"></a>

**Get ads**

Get ads by company, published state or start and end date.

If exact_date = true is given and start date is given, it returns all the ads that start_date == start date given. If exact_date = true is given and end date is given, it returns all the ads that end_date == end date given.

If only start date is given, it returns all the ads that start_date >= start date given. If only end date is given, it returns all the ads that end_date <= end date given.

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get ads filtered - Ads MS

```bash
  GET /ads?...
```

_Query Example_

```graphql
query {
  allAds(
    token: string!,
    id: int!,
    exact_date: boolean,
    start_date: str,
    end_date: str,
    published: boolean
  ) {
    """
    Array of Ad Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `exact_date` is exact start or end date ad (boolean).
* `start_date` is start date timestamp (string).
* `end_date` is end date timestamp (string).
* `published` is a published ad? yes or no (boolean).

_Query Type Response_

Array of [Ad](#id5.6.2) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.7.4"></a>

**Get companies**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get companies - Ads MS

```bash
  GET /companies
```

_Query Example_

```graphql
query {
  allCompanies(token: string!, id: int!) {
    """
    Array of Company Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.

_Query Type Response_

Array of [Company](#id5.6.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.8"></a>

#### Payments

<a id="id3.8.1"></a>

**Get bills by company**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get bills filtered by company id - Ads MS

```bash
  GET /payment?company_id=${com_id}
```

_Query Example_

```graphql
query {
  billsByCompanyId(token: string!, id: int!, com_id: int!) {
    """
    Array of Bill Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `com_id` is company id (int) **REQUIRED**.

_Query Type Response_

Array of [Bill](#id5.7.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.8.2"></a>

**Get bills by ad**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get bills filtered by ad id - Ads MS

```bash
  GET /payment?ad_id=${ad_id}
```

_Query Example_

```graphql
query {
  billsByAdId(token: string!, id: int!, ad_id: int!) {
    """
    Array of Bill Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `ad_id` is ad id (int) **REQUIRED**.

_Query Type Response_

Array of [Bill](#id5.7.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id3.8.3"></a>

**Get bills**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get bills filtered - Ads MS

```bash
  GET /payment?...
```

_Query Example_

```graphql
query {
  allBills(
    token: string!,
    id: int!,
    status: str
  ) {
    """
    Array of Bill Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `status` is bill status enum: "CREATED" | "PAID" |"CANCELED" (string).

_Query Type Response_

Array of [Bill](#id5.7.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id3.8.2"></a>

**Get bill by id**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Check user role is Admin - Users MS

```bash
  GET /users/verify/role/${id}
```

3. Get bill by id - Ads MS

```bash
  GET /payment/${bill_id}
```

_Query Example_

```graphql
query {
  billById(token: string!, id: int!, bill_id: int!) {
    """
    Bill Type attributes
    """
  }
}
```

Parameters:
* `token` is login token (string) **REQUIRED**.
* `id` is user id (int) **REQUIRED**.
* `bill_id` is bill id (int) **REQUIRED**.

_Query Type Response_

[Bill](#id5.7.1) type.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


</br>

<a id="id4"></a>

### Mutations

<a id="id4.1"></a>

#### Users Management

<a id="id4.1.1"></a>

**Sign up user with email**

_Logic Steps_

1. Sign up User - Users MS

```bash
  POST /users
```

_Mutation Example_

```graphql
mutation {
  signUpUser(user: CreateUser!) {
    id //int
  }
}
```

_Mutation Parameters_

* `user` is user create type input ([CreateUser](#id5.1.3)) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.2"></a>

**Sign up user with google**

_Logic Steps_

1. Sign up User with google - Users MS

```bash
  POST /users/google
```

_Mutation Example_

```graphql
mutation {
  signUpUserGoogle(g_token: str!) {
    id //int
  }
}
```

_Mutation Parameters_

* `g_token` is auth google user token (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.3"></a>

**Verify user account**

_Logic Steps_

1. Confirm user - Users MS

```bash
  POST /users/verify
```

_Mutation Example_

```graphql
mutation {
  verifyUser(email: str!, token: str!) {}
}
```

_Mutation Parameters_

* `email` is user email (string) **REQUIRED**.
* `token` is user token sent by email (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.4"></a>

**Forgot Password**

_Logic Steps_

1. Send forgot password token - Users MS

```bash
  POST /users/auth/forgot/${encodeURIComponent(email)}
```

2. Recover password from forgot - Users MS

```bash
  POST /users/auth/recover
```

_Mutation Example_

```graphql
query {
  forgotPassword(email: str!) {}
}

mutation {
  recoverPassword(email: str!, token: str!, new_pass: str!) {}
}
```

_Mutation Parameters_

* `email` is user email (string) **REQUIRED**.
* `new password` is user new password (string) **REQUIRED**.
* `token` is user token sent by email to change password (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.5"></a>

**Change Password**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Change password - Users MS

```bash
  POST /users/auth/change
```

_Mutation Example_

```graphql
mutation {
  recoverPassword(token: str!, email: str!, pass: str!, new_pass: str!) {}
}
```

_Mutation Parameters_

* `email` is user email (string) **REQUIRED**.
* `password` is user current password (string) **REQUIRED**.
* `new password` is user new password (string) **REQUIRED**.
* `token` is user login token (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.6"></a>

**Update User**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Update user - Users MS

```bash
  PUT /users/${id}
```

_Mutation Example_

```graphql
mutation {
  updateUser(token: str!, id: int!, user: UpdateUser!) {}
}
```

_Mutation Parameters_

* `id` is user id (int) **REQUIRED**.
* `token` is user login token (string) **REQUIRED**.
* `user` is user update type input ([UpdateUser](#id5.1.4)) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.1.7"></a>

**Complete Setup**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Complete user setup - Users MS

```bash
  POST /users/setup/${id}
```

_Mutation Example_

```graphql
mutation {
  completeSetup(token: str!, id: int!) {}
}
```

_Mutation Parameters_

* `id` is user id (int) **REQUIRED**.
* `token` is user login token (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---


<a id="id4.1.8"></a>

**Delete User**

_Logic Steps_

1. Verify user token - Users MS

```bash
  GET /users/verify/${token}
```

2. Delete user - Users MS

```bash
  DELETE /users/${id}
```

3. Delete user - Likes MS

```bash
  DELETE /likes/user/${id}
```

4. Delete user recommendations - Recommendations MS

```bash
  DELETE /recommendation/${id}
```

5. Delete all the user relations with ads - Ads MS

```bash
  DELETE /ads/user/${id}
```

_Mutation Example_

```graphql
mutation {
  deleteUser(token: str!, id: int!) {}
}
```

_Mutation Parameters_

* `id` is user id (int) **REQUIRED**.
* `token` is user login token (string) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.2"></a>

#### Countries

<a id="id4.2.1"></a>

**Create Country**

_Logic Steps_

1. Create country - Users MS

```bash
  POST /countries
```

_Mutation Example_

```graphql
mutation {
  createCountry(country: CreateCountry!) {
    id // int
  }
}
```

_Mutation Parameters_

* `country` is country create type input ([CreateCountry](#id5.1.5)) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.2.2"></a>

**Update Country**

_Logic Steps_

1. Update country - Users MS

```bash
  PUT /countries/${id}
```

_Mutation Example_

```graphql
mutation {
  updateCountry(id: int!, country: UpdateCountry!) {}
}
```

_Mutation Parameters_

* `id` is country id (int) **REQUIRED**.
* `country` is country update type input ([UpdateCountry](#id5.1.6)) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.2.3"></a>

**Delete Country**

_Logic Steps_

1. Delete country - Users MS

```bash
  PUT /countries/${id}
```

_Mutation Example_

```graphql
mutation {
  deleteCountry(id: int!) {}
}
```

_Mutation Parameters_

* `id` is country id (int) **REQUIRED**.

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id4.2.4"></a>

**Import countries data**

_Logic Steps_

1. Import countries data - Users MS

```bash
  PUT /countries
```

_Mutation Example_

```graphql
mutation {
  importCountries() {}
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---




<a id="id4.3"></a>

#### Likes

<!-- @todo -->

<a id="id4.4"></a>

#### Catalog

<!-- @todo -->

<a id="id4.5"></a>

#### Recommendations

<!-- @todo -->

<a id="id4.6"></a>

#### Companies

<!-- @todo -->

<a id="id4.7"></a>

#### Ads

<!-- @todo -->


<a id="id4.8"></a>

#### Release

<!-- @todo -->

<a id="id4.9"></a>

#### Payments

<!-- @todo -->



</br>

<a id="id5"></a>

### Types

<a id="id5.1"></a>

#### Users Management

<a id="id5.1.1"></a>

**User**

```graphql
type User {
  id: int!
  firstname: str
  lastname: str
  avatar_url: str
  birthdate: str
  gender: str // 'M' | 'F' | 'O' | 'P'
  country: Country // Country information - Country Type
  created_time: str
  email: str!
  verified: bool!
  setup: bool!
  role: bool! // 0 -> 'READER' and 1 -> 'ADMIN'
}
```

<a id="id5.1.2"></a>

**Country**

```graphql
type Country {
  id: int!
  name: str! // English name
  code_2: str! //ISO 3166-1 alpha-2
  code_3: str! //ISO 3166-1 alpha-3
}
```

<a id="id5.1.3"></a>

**CreateUser**

```graphql
type CreateUser {
  firstname: str!
  lastname: str!
  email: str!
  password: str!
  role: bool! // 0 -> 'READER' and 1 -> 'ADMIN'
}
```

<a id="id5.1.4"></a>

**UpdateUser**

```graphql
type UpdateUser {
  firstname: str
  lastname: str
  avatar: str
  birthdate: str // string timestamp
  gender: str // 'M' | 'F' | 'O' | 'P'
  country: int
}
```

<a id="id5.1.5"></a>

**CreateCountry**

```graphql
type CreateCountry {
  id: int!
  name: str! // English name
  code_2: str! //ISO 3166-1 alpha-2
  code_3: str! //ISO 3166-1 alpha-3
}
```

<a id="id5.1.5"></a>

**UpdateCountry**

```graphql
type CreateCountry {
  name: str? // English name
  code_2: str? //ISO 3166-1 alpha-2
  code_3: str? //ISO 3166-1 alpha-3
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.2"></a>

#### Likes

<a id="id5.2.1"></a>

**Like**

```graphql
type Like {
  media_id: int!
  user_id: int!
  type: str! // 'MOV' | 'BOO' | 'SON' // Media type
  rating: float
  like_type: str! // 'LK' | 'DLK' | 'BLK' // Preference
  wishlist: boolean
}
```

<a id="id5.2.2"></a>

**LikeExtended**

```graphql
type LikeExtended {
  like: Like!
  media: Media!
}
```

<a id="id5.2.3"></a>

**Wishlist**

```graphql
type Wishlist {
  user_id: int!
  movies: [LikeExtended!]
  songs: [LikeExtended!]
  books: [LikeExtended!]
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.3"></a>

#### Catalog

<a id="id5.3.1"></a>

**Media**

```graphql
type Media {
  type: str! // 'MOV' | 'BOO' | 'SON' // Media type
  id: int!
  info: JSON!
}

extend type Media {
  user_like: Like
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.4"></a>

#### Recommendations

<a id="id5.4.1"></a>

**Recommendation**

```graphql
type Recommendation {
  id_recommend: int!
  id_user: int!
  movies: [Media!]!
  books: [Media!]!
  songs: [Media!]!
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.5"></a>

#### Analysis

<a id="id5.5.1"></a>

**Analysis**

```graphql
type Analysis {
  media_id: int!
  gender: GenderAnalysis!
  nationality: [NationalityAnalysis!]!
  age: [AgeAnalysis!]!
}
```

<a id="id5.5.2"></a>

**GenderAnalysis**

```graphql
type GenderAnalysis {
  f: CountLikes!
  m: CountLikes!
  o: CountLikes!
  p: CountLikes!
}
```

<a id="id5.5.3"></a>

**NationalityAnalysis**

```graphql
type NationalityAnalysis {
  country_id: int!
  country_name: int!
  like: CountLikes!
  code_2: str! //ISO 3166-1 alpha-2
  code_3: str! //ISO 3166-1 alpha-3
}
```

<a id="id5.5.4"></a>

**AgeAnalysis**

```graphql
type AgeAnalysis {
  range: str!
  lower_age: int!
  upper_age: int!
  total: int! // Total users inside the range
  like_info: CountLikes!
}
```

<a id="id5.5.5"></a>

**CountLikes**

```graphql
type CountLikes {
  lk_total: int! // Total of users with type "Like"
  dlk_total: int! // Total of users with type "dislike"
  avr_rating: int! // Average rating of likes
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.6"></a>

#### Release

<a id="id5.6.1"></a>

**Company**

```graphql
type Company {
  company_id: int!
  name: str!
  email: str!
}
```

<a id="id5.6.2"></a>

**Ad**

```graphql
type Ad {
  ad_id: int!
  name: str!
  ad_url: str! // Bucket url to display ad image
  start_date: str! //timestamp of start date to publish ad
  end_date: str! //timestamp of end date to publish ad
  description: str!
  company: Company!
  published: boolean!
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

---

<a id="id5.7"></a>

#### Payments

<a id="id5.7.1"></a>

**Bill**

```graphql
type Bill {
  id: int!
  id_ad: int!
  status: str! // "CREATED" | "PAID" |"CANCELED"
  amount: int!
  createdAt: str! // Timestamp string
}
```

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>


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

---

<p>
<p></p>
<a style="color:white; background-color: gray; padding: 5px; border-radius: 8px;" href="#index">Go to Index ↑</a>
<p></p>
</p>

***

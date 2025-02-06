# Restaurant Review System

A restaurant review system built with Django / Django REST Framework.

## Getting Started

1. Make sure you have [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed.

2. Clone the repository:
```bash
git clone https://github.com/haeter525/restaurant_review_system
```

3. Start the system:
```bash
docker-compose up
```

4. Visit http://localhost:8000 for the API documentation.


## API Endpoints

+ Create restaurant - `POST /api/restaurant`

+ Create restaurant review -  `POST /api/review`

+ Edit review - `PATCH /api/review/{review_id}`

+ Delete review - `DELETE /api/review/{review_id}`

+ Search restaurant and sort by score - `GET /api/restaurant?search={restaurant_name}`

+ List reviews of certain restaurant - `GET /api/review?restaurant={restaurant_id}`

+ List reviews of certain user - `GET /api/review?author={username}`

Please visit the API documentation for more details and examples.

## Authentication
The system defines 3 user roles: **admin user**, **login user**, and **anonymous users**.

+ **Admin users** can create, edit, and delete restaurant/reviews.
+ **Login users** can create, edit, and delete their own reviews.
+ **All users, including anonymous users**, can list or search restaurants and reviews.

Therefore, the system uses HTTP Basic Auth to authenticate users and verify their permissions before processing requests.

## Testing

To facilitate quick testing of API endpoints, the system is pre-configured with one admin user, two login users, and a predefined set of restaurants and reviews.

The usernames and passwords for the admin and login users are as follows:

+ Admin
    + username: admin
    + password: admin
+ User 1
    + username: user1
    + password: password1
+ User 2
    + username: user2
    + password: password2

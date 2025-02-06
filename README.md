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

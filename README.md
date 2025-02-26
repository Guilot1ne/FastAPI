
## Version
**1.0.0**

## Getting Started

### Running the API
To start the API and required services, run the following command:

docker compose up -d


### Accessing the API

- Swagger Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Database Connection

The PostgreSQL database is running inside a Docker container. To connect to the database, use the following credentials:

- **Host**: `localhost` (or `127.0.0.1`)
- **Port**: `5432`
- **Username**: `postgres`
- **Password**: `1234`
- **Database**: `fastapi`

### Making Changes

To modify configurations or services, edit the `docker-compose.yml` file.

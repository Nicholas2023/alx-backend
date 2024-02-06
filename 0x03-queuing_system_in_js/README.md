# Queuing System in Node.js with Redis :smile:

This project implements a queuing system in Node.js using Redis as the backend storage. It includes various components such as Redis clients, publishers, subscribers, job creators, processors, and tests.

## Installation

To run this project, you'll need to have Node.js and Redis installed on your machine.

1. Clone this repository:

```bash
git clone <repository_url>
```

2. Install dependencies:

```bash
npm install
```

3. Start Redis server:

```bash
# Start Redis server
redis-server
```

4. Run the desired script:

```bash
npm run dev <script_name.js>
```

## Project Structure

The project directory structure is as follows:

```
.
├── 0-redis_client.js
├── 1-redis_op.js
├── 2-redis_op_async.js
├── 4-redis_advanced_op.js
├── 5-subscriber.js
├── 5-publisher.js
├── 6-job_creator.js
├── 6-job_processor.js
├── 7-job_creator.js
├── 7-job_processor.js
├── 8-job.js
├── 8-job-main.js
├── 8-job.test.js
└── 9-stock.js
```

## Tasks Completed

1. **Node Redis Client**: Implemented a Redis client in Node.js to connect to the Redis server.

2. **Node Redis Client and Basic Operations**: Implemented basic Redis operations like setting and getting values using callbacks.

3. **Node Redis Client and Async Operations**: Modified operations to use ES6 async/await with promisify.

4. **Node Redis Client and Advanced Operations**: Stored hash values in Redis and displayed them.

5. **Node Redis Client Publisher and Subscriber**: Implemented a publisher and subscriber for Redis channels.

6. **Job Creator**: Created jobs using Kue for queuing tasks.

7. **Job Processor**: Processed jobs using Kue for background tasks.

8. **Track Progress and Errors with Kue**: Tracked job progress and errors using Kue.

9. **Stock Management with Redis**: Managed product stock using Redis.

## Testing

The project includes tests for the job creation function using Mocha.

To run the tests:

```bash
npm test
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

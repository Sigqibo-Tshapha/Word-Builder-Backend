import Hapi from '@hapi/hapi';
import routes from './routes';
import { db } from './database';
import dotenv from 'dotenv';
dotenv.config();

let server;

const start = async () => {
  const server = Hapi.server({
    port: 8080,
    //host: '0.0.0.0',    //server host
    host: 'localhost',
  });

  db.connect();

  routes.forEach(route => server.route(route));

  await server.start();
  console.log(`Server is listening on  ${server.info.uri}`);
}

process.on('unhandledRejection', err => {
  console.log(err);
  process.exit(1);
})

start();

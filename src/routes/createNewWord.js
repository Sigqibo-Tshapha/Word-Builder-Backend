import { db } from '../database';

export const createNewWordRoute = {
  method: 'POST',
  path: '/api/words',
  handler: async (req, h) => {
    const { type = '', word = ''} = JSON.parse( req.payload);

    await db.query(
      `INSERT INTO words (id, type, word) VALUES (null, ?, ?) `,
        [type, word]
    );
    
    return { type, word };
  }
}

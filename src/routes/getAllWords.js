import { db } from "../database";

export const getAllWordsRoute = {
  method: 'GET',
  path: '/api/words',
  handler: async (req, h) => {
    const { results } = await db.query(
      `SELECT type, GROUP_CONCAT(word) as words
      FROM words
      GROUP BY type`
    );
    return results;
  }
}


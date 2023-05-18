import { db } from "../database";

export const getAllSentencesRoute = {
  method: 'GET',
  path: '/api/sentences',
  handler: async(req, h) => {
    const { results } = await db.query(
      'SELECT sentence FROM sentences'
    );
    return results;
  }
}

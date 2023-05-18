import { db } from "../database";

export const createNewSentenceRoute = {
  method: 'POST',
  path: '/api/sentence',
  handler: async (req, h) => {
    console.log(req.payload);
    const sentence = req.payload.sentence;
    await db.query(
      'INSERT INTO sentences (id, sentence) VALUES (null, ?)', 
      sentence
    );

    return sentence;
  }
}


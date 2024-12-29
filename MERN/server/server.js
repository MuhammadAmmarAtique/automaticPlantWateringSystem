import express from 'express';
import bodyParser from 'body-parser';
import { SoilData } from "./model/soilData.model.js"
import { dbConnection } from "./db/dbConnection.js"
dbConnection()

const app = express();
app.use(bodyParser.json());

app.post('/soil-data', async (req, res) => {
    const { moistureValue } = req.body;
    console.log('Received Moisture Value:', moistureValue);
    //saving moisture value in database
    const data = new SoilData({ moistureValue });
    await data.save();
    res.status(200).send('Data Received');
});

app.listen(3000, () => console.log('Server running on port 3000'));

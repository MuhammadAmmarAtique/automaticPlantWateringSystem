import express from 'express';
import bodyParser from 'body-parser';

const app = express();
app.use(bodyParser.json());

app.post('/soil-data', (req, res) => {
    const { moistureValue } = req.body;
    console.log('Received Moisture Value:', moistureValue);
    res.status(200).send('Data Received');
});

app.listen(3000, () => console.log('Server running on port 3000'));
